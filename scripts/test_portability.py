"""Regression checks for UTF-8 I/O and Windows Markdown link generation."""
from pathlib import Path
import ntpath
import shutil
import tempfile
import unittest
from unittest.mock import patch

import build_mindmap
import build_views
import check_package


class PortabilityTests(unittest.TestCase):
    def test_windows_links_match_published_views(self):
        expected = (build_views.ROOT / 'docs/formulas.md').read_text(encoding='utf-8')
        with patch('os.path.relpath', ntpath.relpath):
            self.assertEqual(build_views.render(), expected)

    def test_build_and_check_with_gbk_default(self):
        # Work on a copy so the test never regenerates the user's repository.
        original_open = Path.open

        def gbk_open(path, mode='r', buffering=-1, encoding=None, errors=None, newline=None):
            if 'b' not in mode and encoding is None:
                encoding = 'gbk'
            return original_open(path, mode, buffering, encoding, errors, newline)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'repo'
            shutil.copytree(build_views.ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            expected = {name: (root / name).read_bytes() for name in
                        list(build_views.GENERATED) + list(build_mindmap.VIEWS)}
            with patch.object(build_views, 'ROOT', root), \
                    patch.object(Path, 'open', gbk_open), patch('os.path.relpath', ntpath.relpath):
                build_views.main()
                check_package.check()
            for name, content in expected.items():
                self.assertEqual((root / name).read_bytes(), content)


if __name__ == '__main__':
    unittest.main()
