import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class AuthorClarificationTests(unittest.TestCase):
    def read(self,rel): return (ROOT/rel).read_text(encoding='utf-8')
    def test_dante_prior_knowledge(self):
        for rel in ('22_Dante_Campaign/Dante_Playable_Screenplay_v0.7.md','09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.8.md'):
            s=self.read(rel); self.assertIn('knew each other',s); self.assertIn('before',s)
    def test_crystal_not_spontaneously_aware(self):
        s=self.read('15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.10.md')
        self.assertIn('does **not** spontaneously recognize',s)
        self.assertNotIn('Once she recognizes the pressure, Crystal leaves',s)
    def test_raven_pov_distinguishes_awareness(self):
        s=self.read('16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.9.md')
        self.assertIn('does **not** recognize that Raven engineered',s)
        self.assertIn('**CRYSTAL (on EXPLOIT):**',s)
    def test_authority_and_distinct_knowledge(self):
        s=self.read('02_Story_Bibles/Relationship_Canon_Clarifications_v4.7.md')
        self.assertIn('crystal_knows_raven_manipulation',s)
        self.assertIn('raven_manipulation_occurred',s)

if __name__=='__main__': unittest.main()
