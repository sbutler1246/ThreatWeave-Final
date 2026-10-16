import json
from pathlib import Path
import tempfile
import unittest

from reproduce_results import local_path, equal


class PortablePaths(unittest.TestCase):
    def test_schema_comment_semicolon_cannot_be_executed_as_cypher(self):
        from portable import schema_statements
        statements = schema_statements('// Neo4j schema; explanation is not a query.\nCREATE (n:Example);\n// trailing note;\n')
        self.assertEqual(statements, ['CREATE (n:Example)'])

    def test_recorded_root_is_mapped_to_reader_checkout(self):
        root = Path(tempfile.gettempdir()).resolve() / 'reader-checkout'
        self.assertEqual(local_path(root, r'S:\ThreatWeave\docs\ratings.json'), root / 'docs/ratings.json')
        self.assertEqual(local_path(root, r'work\run\receipt.json'), root / 'work/run/receipt.json')

    def test_foreign_absolute_and_escape_rejected(self):
        root = Path(tempfile.gettempdir()).resolve() / 'reader-checkout'
        for name in (r'C:\Users\someone\secret.json', '../outside.json', '/etc/passwd', r'Z:relative.json', r'S:\ThreatWeave\..\outside.json'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                local_path(root, name)

    def test_nested_numeric_and_missingness_checks(self):
        equal({'mean': .1 + .2, 'missing': None}, {'mean': .3, 'missing': None}, 'test')
        with self.assertRaises(ValueError):
            equal({'missing': 0}, {'missing': None}, 'test')


class PortableSources(unittest.TestCase):
    def test_complete_scope_works_without_historical_work_folders(self):
        from portable_sources import check
        source = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'data/portable').mkdir(parents=True)
            (root / 'config.json').write_bytes((source / 'config.json').read_bytes())
            for name in ('manifest.json', 'development_sources.json'):
                (root / 'data/portable' / name).write_bytes((source / 'data/portable' / name).read_bytes())
            bundle, projection, _ = check(root)
            self.assertEqual((len(bundle['profiles']), len(bundle['references'])), (53, 139))
            self.assertEqual((len(projection['nodes']), len(projection['edges'])), (142, 245))
            self.assertFalse((root / 'work').exists())
            raw = root / 'data/portable/development_sources.json'
            raw.write_bytes(raw.read_bytes() + b' ')
            with self.assertRaisesRegex(ValueError, 'checksum'):
                check(root)


if __name__ == '__main__':
    unittest.main()
