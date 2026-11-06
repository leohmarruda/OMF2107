import csv,unittest,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INV=ROOT/'31_Cross_POV_Integration/ACTIVE_SCENE_INVENTORY_v3.3.csv'
class InventoryTests(unittest.TestCase):
 def test_all_pilots_covered(self):
  with INV.open() as f: rows=list(csv.DictReader(f))
  self.assertEqual(set(r['pilot'] for r in rows),{'Ari','Lyra','Mara','Ren','Angel','Crystal','Raven','Jean-Paul','Steffan','Dante','Selene','Milano'})
 def test_source_lines_still_match(self):
  with INV.open() as f: rows=list(csv.DictReader(f))
  for r in rows:
   src=ROOT/r['source'];self.assertTrue(src.is_file(),r['source'])
   line=src.read_text().splitlines()[int(r['line'])-1]
   self.assertTrue(line.lstrip().startswith('#'),r)
   self.assertIn(r['scene_id'].lower(),line.lower().replace(' ',''),r)
 def test_unique_source_qualified_ids(self):
  with INV.open() as f: rows=list(csv.DictReader(f))
  keys=[(r['source'],r['scene_id']) for r in rows]
  self.assertEqual(len(keys),len(set(keys)))
 def test_no_falsely_verified_claims(self):
  with INV.open() as f: rows=list(csv.DictReader(f))
  self.assertTrue(all(r['review_status']=='UNREVIEWED' and not r['event_verified'] for r in rows))
if __name__=='__main__':unittest.main()
