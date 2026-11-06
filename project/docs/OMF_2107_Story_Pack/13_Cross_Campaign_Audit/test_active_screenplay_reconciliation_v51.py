import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ActiveScriptReconciliationV51(unittest.TestCase):
 def script(self,path): return (ROOT/path).read_text()
 def test_circular_group_seeding_removed_from_active_pov(self):
  for p in ('09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.8.md','22_Dante_Campaign/Dante_Playable_Screenplay_v0.7.md','16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.9.md'):
   s=self.script(p)
   self.assertNotIn('provisional public seeding',s)
   self.assertNotIn('published provisional order',s)
   self.assertNotIn('provisional seed Mara > Ren > Raven',s)
   self.assertIn('score',s.lower())
 def test_raven_one_win_is_not_automatically_eliminated(self):
  s=self.script('16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.9.md')
  self.assertIn('Raven ranks B1, B2, or B3',s)
  self.assertIn('KNOWLEDGE GATE:',s)
 def test_dante_separation_gate(self):
  s=self.script('22_Dante_Campaign/Dante_Playable_Screenplay_v0.7.md')
  self.assertIn('STATE GATE (Day 5',s)
  self.assertIn('Dante cannot veto',s)
 def test_crystal_remains_unaware_without_independent_evidence(self):
  s=self.script('15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.10.md')
  self.assertIn('Crystal remains unaware',s)
  self.assertIn('independent',s.lower())
if __name__ == '__main__': unittest.main()
