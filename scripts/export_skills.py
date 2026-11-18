#!/usr/bin/env python3
"""Export selected workflow skills, or verify an exported bundle. Python 3.9+."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'workflow-manifest.json'
PREFIX = '../../workflow/'
RESOURCE_DIRS = ('references', 'scripts', 'assets', 'agents')


def regular_tree(path):
    """Reject links and special files before reading or copying package resources."""
    if path.is_symlink():
        raise ValueError(f'Symbolic link is not a package resource: {path}')
    if path.is_file():
        return
    if not path.is_dir():
        raise ValueError(f'Missing or unsupported resource: {path}')
    for child in path.iterdir():
        regular_tree(child)


def catalog(root):
    folder = root / 'skills'
    regular_tree(folder)
    names = []
    for directory in sorted(folder.iterdir()):
        if not directory.is_dir():
            raise ValueError(f'Expected a skill directory: {directory}')
        name = directory.name
        if not re.fullmatch(r'workflow-[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            raise ValueError(f'Invalid skill name: {name}')
        # This repository uses a deliberately small, JSON-quoted YAML style.
        text = (directory / 'SKILL.md').read_text(encoding='utf-8')
        match = re.match(r'\A---\nname: ([^\n]+)\ndescription: ("[^\n]*")\n---\n', text)
        if not match or match[1] != name:
            raise ValueError(f'Invalid frontmatter: {directory}')
        description = json.loads(match[2])
        if not description.strip() or len(description) > 1024:
            raise ValueError(f'Invalid description: {directory}')
        allowed = {'SKILL.md', *RESOURCE_DIRS}
        for child in directory.iterdir():
            if child.name not in allowed:
                raise ValueError(f'Unpackaged file in skill source: {child}')
            if child.name in RESOURCE_DIRS and not child.is_dir():
                raise ValueError(f'Expected resource directory: {child}')
        names.append(name)
    if not names:
        raise ValueError('No skills found')
    return names


def check_links(folder, paths=None):
    """Validate local inline Markdown links in the package's simple link format."""
    boundary = folder.resolve()
    for path in folder.rglob('*.md') if paths is None else paths:
        text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            parsed = urlsplit(link)
            if parsed.scheme in ('https', 'http', 'mailto', 'tel') or link.startswith('#'):
                continue
            if parsed.scheme or parsed.netloc:
                raise ValueError(f'Unsupported resource link in {path}: {link}')
            target = (path.parent / unquote(parsed.path)).resolve()
            if boundary not in target.parents or not target.is_file():
                raise ValueError(f'Missing or escaping resource in {path}: {link}')


def inventory(folder):
    return {
        p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(folder.rglob('*')) if p.is_file() and p != folder / MANIFEST
    }


def export(output, selected=None, root=ROOT):
    root = Path(root)
    available = catalog(root)
    names = list(dict.fromkeys(selected)) if selected else available
    unknown = set(names) - set(available)
    if unknown:
        raise ValueError('Unknown skills: ' + ', '.join(sorted(unknown)))
    for resource in ('workflow', 'LICENSE', 'VERSION'):
        regular_tree(root / resource)
    version = (root / 'VERSION').read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?', version):
        raise ValueError('Invalid VERSION')
    output = Path(os.path.abspath(Path(output).expanduser()))
    if os.path.lexists(output):
        raise FileExistsError(f'Destination already exists; choose a new directory: {output}')
    resolved_output = output.resolve()
    if resolved_output == root.resolve() or root.resolve() in resolved_output.parents:
        # A dist directory is fine; writing into the sources is not.
        if (root.resolve() / 'dist') not in resolved_output.parents:
            raise ValueError('Export outside the source tree or into dist/<new-directory>')
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.workflow-export-', dir=output.parent))
    try:
        for name in names:
            source = root / 'skills' / name
            reserved = source / 'references' / 'workflow'
            if os.path.lexists(reserved):
                raise ValueError(f'Reserved shared-resource path: {reserved}')
            target = stage / name
            shutil.copytree(source, target)
            entry = target / 'SKILL.md'
            entry.write_text(entry.read_text(encoding='utf-8').replace(
                PREFIX, 'references/workflow/'), encoding='utf-8')
            shutil.copytree(root / 'workflow', target / 'references' / 'workflow')
            shutil.copyfile(root / 'LICENSE', target / 'LICENSE')
            check_links(target)
        (stage / MANIFEST).write_text(json.dumps({
            'format': 1, 'version': version, 'skills': names,
            'sha256': inventory(stage),
        }, indent=2) + '\n', encoding='utf-8')
        # mkdir is the exclusive reservation: never merge into an existing folder.
        output.mkdir()
        try:
            for child in stage.iterdir():
                shutil.move(str(child), output / child.name)
        except OSError as error:
            raise RuntimeError(f'Incomplete export; inspect {output}: {error}') from error
    finally:
        shutil.rmtree(stage)
    return output


def verify(folder):
    folder = Path(folder)
    regular_tree(folder)
    data = json.loads((folder / MANIFEST).read_text(encoding='utf-8'))
    if (not isinstance(data, dict) or type(data.get('format')) is not int
            or data['format'] != 1 or not isinstance(data.get('sha256'), dict)):
        raise ValueError('Unsupported manifest format')
    version = data.get('version')
    if not isinstance(version, str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?', version):
        raise ValueError('Invalid or missing manifest version')
    names = data.get('skills')
    if not isinstance(names, list) or not names or any(
        not isinstance(n, str) or not re.fullmatch(r'workflow-[a-z0-9]+(?:-[a-z0-9]+)*', n)
        for n in names
    ) or len(names) != len(set(names)):
        raise ValueError('Invalid manifest skill list')
    if inventory(folder) != data['sha256']:
        raise ValueError('Manifest mismatch: files were changed, added, or removed')
    if {p.name for p in folder.iterdir()} != {*names, MANIFEST}:
        raise ValueError('Unexpected bundle entries')
    for name in names:
        skill = folder / name
        if not (skill / 'SKILL.md').is_file() or not (skill / 'LICENSE').is_file():
            raise ValueError(f'Incomplete skill: {name}')
        check_links(skill)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--output', type=Path, help='New export directory; never overwritten')
    group.add_argument('--verify', type=Path, help='Check an existing export against its manifest')
    group.add_argument('--list', action='store_true', help='List available skills')
    parser.add_argument('--skill', action='append', help='Export one skill; repeat to select several')
    args = parser.parse_args()
    if args.skill and not args.output:
        parser.error('--skill requires --output')
    try:
        if args.list:
            print('\n'.join(catalog(ROOT)))
        elif args.verify:
            data = verify(args.verify)
            print(f"Verified {len(data['skills'])} skills, version {data['version']}")
        else:
            result = export(args.output, args.skill)
            data = verify(result)
            print(f"Exported {len(data['skills'])} skills to {result}")
    except (OSError, ValueError, RuntimeError) as error:
        parser.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
