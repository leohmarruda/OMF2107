import csv,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
PILOTS={'Ari','Lyra','Mara','Ren','Angel','Crystal','Raven','Jean-Paul','Steffan','Dante','Selene','Milano'}
class Day13Tests(unittest.TestCase):
 def test_twelve_unique_pilots_and_sources(self):
  with (HERE/'DAY13_POV_ACCESS_MATRIX_v3.4.csv').open() as f: rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),12)
  self.assertEqual({r['pilot'] for r in rows},PILOTS)
  for r in rows:
   self.assertTrue((ROOT/r['source']).is_file())
   contents=(ROOT/r['source']).read_text()
   for identifier in r['scene_ids'].split(';'):
    self.assertIn(identifier.replace(' ', '').upper(),contents.replace(' ', '').upper())
 def test_statuses_are_not_falsely_closed(self):
  with (HERE/'DAY13_POV_ACCESS_MATRIX_v3.4.csv').open() as f: rows=list(csv.DictReader(f))
  self.assertTrue(all(r['audit_status'] in {'ACCESS_PARTIAL','ROLE_UNCLEAR','BRANCH_CONFLICT'} for r in rows))
 def test_invariants_acyclic(self):
  data=json.loads((HERE/'DAY13_EVENT_INVARIANTS_v3.4.json').read_text())
  events=set(data['required']);edges=data['required_precedence'];self.assertTrue(all(a in events and b in events for a,b in edges))
  reachable={a:{b for x,b in edges if x==a} for a in events}
  for k in events:
   for a in events:
    if k in reachable[a]:reachable[a].update(reachable[k])
  self.assertFalse(any(a in reachable[a] for a in events))
 def test_latch_and_cross_route_clerical_fixes(self):
  mil=(ROOT/'24_Milano_Campaign/Milano_Playable_Screenplay_v0.5.md').read_text()
  dante=(ROOT/'22_Dante_Campaign/Dante_Playable_Screenplay_v0.7.md').read_text()
  self.assertIn('hardwired biological command path, engaging the physical retention latch',mil)
  self.assertIn('other eleven selectable campaigns',dante)
if __name__=='__main__':unittest.main()
