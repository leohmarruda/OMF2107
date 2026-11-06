# Regenerate this file from bg_engine.py or run it directly with the catalog files.
import csv, json, pathlib, re, unittest
R=pathlib.Path(__file__).resolve().parents[1]
C=R/'26_Background_Registry'
class TestBackgroundRegistry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog=json.loads((C/'background_registry.json').read_text())['backgrounds']
        cls.codes={i['code']:set(i['variants']) for i in cls.catalog}
        with (C/'scene_background_bindings.csv').open(newline='') as f:
            cls.bindings=list(csv.DictReader(f))
    def test_distinct_catalog_ids(self):
        self.assertEqual(len(self.codes),len(self.catalog))
    def test_manifest_references_exist(self):
        for row in self.bindings:
            for code,state in re.findall(r'(BG-[A-Z0-9-]+)@([A-Z]+)',row['bg_refs']):
                self.assertIn(code,self.codes)
                self.assertIn(state,self.codes[code])
    def test_slugs_have_annotation(self):
        for script in sorted({x['script'] for x in self.bindings}):
            lines=(R/script).read_text().splitlines()
            for i,line in enumerate(lines):
                if re.match(r'^\*\*(INT|EXT|INT/EXT)\.',line):
                    self.assertTrue(i+1<len(lines) and lines[i+1].startswith('**[BG:'),(script,i+1))
    def test_all_active_scripts_in_manifest(self):
        scripts={x['script'] for x in self.bindings}
        self.assertEqual(18,len(scripts))
if __name__=='__main__':unittest.main()
