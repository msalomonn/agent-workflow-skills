#!/usr/bin/env python3
"""Run repository checks without installing skills or contacting remote services."""
from pathlib import Path
import subprocess
import sys
import tempfile

from export_skills import ROOT, catalog, check_links, export, verify


def main():
    names = catalog(ROOT)
    # The source docs use local inline links; validate those as well as exports.
    check_links(ROOT)
    with tempfile.TemporaryDirectory() as temporary:
        bundle = export(Path(temporary) / 'bundle')
        verify(bundle)
    result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)
    print(f'Validated {len(names)} skills, local links, portable export, and package tests.')


if __name__ == '__main__':
    main()
