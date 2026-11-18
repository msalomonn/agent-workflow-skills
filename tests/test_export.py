"""Test observable package integrity and installation boundaries without network access."""
import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('exporter', ROOT / 'scripts/export_skills.py')
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / 'source'
        for directory in ('skills', 'workflow', 'scripts'):
            shutil.copytree(ROOT / directory, self.source / directory)
        for name in ('VERSION', 'LICENSE'):
            shutil.copyfile(ROOT / name, self.source / name)
        self.output = self.base / 'export'

    def export(self, selected=None):
        return exporter.export(self.output, selected, root=self.source)

    def test_installation_survives_removing_source(self):
        names = exporter.catalog(self.source)
        self.export()
        shutil.rmtree(self.source)
        result = exporter.verify(self.output)
        self.assertEqual(result['skills'], names)
        for name in names:
            text = (self.output / name / 'SKILL.md').read_text()
            self.assertNotIn('../../workflow/', text)
            self.assertTrue((self.output / name / 'LICENSE').is_file())
            exporter.check_links(self.output / name)

    def test_selected_skill_is_independent(self):
        self.export(['workflow-handoff'])
        self.assertEqual(set(p.name for p in self.output.iterdir()),
                         {'workflow-handoff', exporter.MANIFEST})
        self.assertEqual(exporter.verify(self.output)['skills'], ['workflow-handoff'])

    def test_unknown_skill_cannot_escape_source(self):
        with self.assertRaises(ValueError):
            self.export(['../../outside'])
        self.assertFalse(self.output.exists())

    def test_existing_installation_is_untouched(self):
        self.output.mkdir()
        sentinel = self.output / 'personal.txt'
        sentinel.write_text('keep my work')
        with self.assertRaises(FileExistsError):
            self.export()
        self.assertEqual(sentinel.read_text(), 'keep my work')
        self.assertEqual(list(self.output.iterdir()), [sentinel])

    def test_broken_destination_symlink_is_untouched(self):
        self.output.symlink_to(self.base / 'missing')
        with self.assertRaises(FileExistsError):
            self.export()
        self.assertTrue(self.output.is_symlink())

    def test_resources_execute_without_source(self):
        skill = self.source / 'skills/workflow-spec'
        (skill / 'scripts').mkdir()
        (skill / 'assets').mkdir()
        (skill / 'assets/message.txt').write_text('portable resource')
        helper = skill / 'scripts/read_asset.py'
        helper.write_text("from pathlib import Path\nprint((Path(__file__).resolve().parents[1] / 'assets/message.txt').read_text())\n")
        helper.chmod(0o755)
        self.export(['workflow-spec'])
        shutil.rmtree(self.source)
        installed = self.output / 'workflow-spec/scripts/read_asset.py'
        result = subprocess.run([sys.executable, str(installed)], cwd=self.base,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), 'portable resource')
        self.assertEqual(installed.stat().st_mode & 0o777, 0o755)
        exporter.verify(self.output)

    def test_source_links_are_rejected(self):
        for relative in ('skills/workflow-spec/SKILL.md', 'workflow/agreement.md', 'LICENSE'):
            with self.subTest(relative=relative):
                file = self.source / relative
                original = file.read_bytes()
                outside = self.base / 'outside'
                outside.write_bytes(original)
                file.unlink()
                file.symlink_to(outside)
                with self.assertRaisesRegex(ValueError, 'Symbolic link'):
                    self.export()
                self.assertFalse(self.output.exists())
                file.unlink()
                file.write_bytes(original)

    def test_nested_resource_links_are_rejected(self):
        resources = self.source / 'skills/workflow-spec/assets'
        resources.mkdir()
        (resources / 'private').symlink_to(self.base)
        with self.assertRaisesRegex(ValueError, 'Symbolic link'):
            self.export()
        self.assertFalse(self.output.exists())

    def test_reserved_resources_are_not_overwritten(self):
        reserved = self.source / 'skills/workflow-spec/references/workflow'
        reserved.mkdir(parents=True)
        sentinel = reserved / 'personal.md'
        sentinel.write_text('keep')
        with self.assertRaisesRegex(ValueError, 'Reserved'):
            self.export()
        self.assertEqual(sentinel.read_text(), 'keep')
        self.assertFalse(self.output.exists())

    def test_missing_or_escaping_links_fail_before_installation(self):
        skill = self.source / 'skills/workflow-spec/SKILL.md'
        original = skill.read_text()
        for target in ('missing.md', '../../../outside.md', '/etc/passwd', '%2e%2e/%2e%2e/outside'):
            with self.subTest(target=target):
                skill.write_text(original + f'\n[Required]({target})\n')
                with self.assertRaises(ValueError):
                    self.export()
                self.assertFalse(self.output.exists())

    def test_references_and_metadata_are_preserved(self):
        skill = self.source / 'skills/workflow-spec'
        (skill / 'agents').mkdir()
        metadata = b'interface:\n  display_name: "Workflow Spec"\n'
        (skill / 'agents/openai.yaml').write_bytes(metadata)
        self.export()
        self.assertEqual((self.output / 'workflow-spec/agents/openai.yaml').read_bytes(), metadata)
        exporter.verify(self.output)

    def test_external_links_are_not_fetched(self):
        doc = self.source / 'workflow/agreement.md'
        doc.write_text(doc.read_text() + '\n[Web](https://example.invalid) [Email](mailto:team@example.invalid)\n')
        self.export()
        exporter.verify(self.output)

    def test_unexpected_root_file_is_not_silently_dropped(self):
        (self.source / 'skills/workflow-spec/secret.txt').write_text('unpackaged')
        with self.assertRaisesRegex(ValueError, 'Unpackaged'):
            self.export()
        self.assertFalse(self.output.exists())

    def test_changed_added_or_missing_files_invalidate_manifest(self):
        self.export()
        path = self.output / 'workflow-spec/SKILL.md'
        original = path.read_bytes()
        path.write_text('changed')
        with self.assertRaisesRegex(ValueError, 'Manifest mismatch'):
            exporter.verify(self.output)
        path.write_bytes(original)
        extra = self.output / 'unexpected.txt'
        extra.write_text('extra')
        with self.assertRaisesRegex(ValueError, 'Manifest mismatch'):
            exporter.verify(self.output)
        extra.unlink()
        path.unlink()
        with self.assertRaisesRegex(ValueError, 'Manifest mismatch'):
            exporter.verify(self.output)

    def test_repeated_selection_exports_once(self):
        self.export(['workflow-audit', 'workflow-audit'])
        self.assertEqual(exporter.verify(self.output)['skills'], ['workflow-audit'])

    def test_source_frontmatter_name_must_match_folder(self):
        skill = self.source / 'skills/workflow-spec/SKILL.md'
        skill.write_text(skill.read_text().replace('name: workflow-spec', 'name: wrong-name'))
        with self.assertRaisesRegex(ValueError, 'frontmatter'):
            self.export()

    def test_export_cannot_mutate_source_directories(self):
        with self.assertRaisesRegex(ValueError, 'outside the source tree'):
            exporter.export(self.source / 'skills/new-skill', root=self.source)
        self.assertFalse((self.source / 'skills/new-skill').exists())

    def test_cli_export_and_verify(self):
        command = [sys.executable, str(self.source / 'scripts/export_skills.py')]
        result = subprocess.run(command + ['--output', str(self.output), '--skill', 'workflow-debug'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run(command + ['--verify', str(self.output)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
