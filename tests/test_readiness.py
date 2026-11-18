"""Regressions found while reviewing the public installation path."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadinessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / 'source'
        for directory in ('scripts', 'skills', 'workflow', 'docs', 'examples'):
            shutil.copytree(ROOT / directory, self.source / directory,
                            ignore=shutil.ignore_patterns('__pycache__'))
        for path in ROOT.glob('*.md'):
            shutil.copyfile(path, self.source / path.name)
        for name in ('LICENSE', 'VERSION'):
            shutil.copyfile(ROOT / name, self.source / name)
        (self.source / 'tests').mkdir()
        # Run the original package suite in the copy without recursively running this test.
        shutil.copyfile(ROOT / 'tests/test_export.py', self.source / 'tests/test_export.py')
        self.bundle = self.base / 'bundle'

    def run_script(self, name, *args):
        return subprocess.run([sys.executable, str(self.source / 'scripts' / name), *args],
                              cwd=self.source, text=True, capture_output=True)

    def test_ignored_local_notes_do_not_break_repository_checks(self):
        for folder in ('.workflow-local', '.venv', 'dist/old-export'):
            target = self.source / folder / 'unfinished.md'
            target.parent.mkdir(parents=True)
            target.write_text('[Draft reference](not-written-yet.md)\n')
        result = self.run_script('check_repository.py')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_real_broken_documentation_still_fails(self):
        (self.source / 'docs/broken.md').write_text('[Required](missing.md)\n')
        result = self.run_script('check_repository.py')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('missing.md', result.stderr)

    def test_malformed_manifest_reports_a_controlled_error(self):
        exported = self.run_script('export_skills.py', '--output', str(self.bundle))
        self.assertEqual(exported.returncode, 0, exported.stderr)
        manifest = self.bundle / 'workflow-manifest.json'
        valid = json.loads(manifest.read_text())
        for data in ([], None, {'format': 1, 'sha256': {}},
                     {k: v for k, v in valid.items() if k != 'version'},
                     dict(valid, version=123), dict(valid, version='not-a-version'),
                     dict(valid, format=True)):
            with self.subTest(data_type=type(data).__name__, version=data.get('version') if isinstance(data, dict) else None):
                manifest.write_text(json.dumps(data))
                result = self.run_script('export_skills.py', '--verify', str(self.bundle))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('Error:', result.stderr)
                self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
