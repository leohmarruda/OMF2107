import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def read(rel): return (ROOT/rel).read_text(encoding='utf-8')

class DanteCrossPOVTests(unittest.TestCase):
    def test_dante_and_steffan_share_private_confrontation_day11(self):
        d=read('22_Dante_Campaign/Dante_Playable_Screenplay_v0.1.md')
        s=read('21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.2.md')
        exact='You wanted me to look at you. So you made her into the message.'
        self.assertIn(exact,d)
        self.assertIn(exact,s)
        self.assertIn('DV5.2',s)
        self.assertLess(s.index('ST5.1b'),s.index('ST5.2'))
        self.assertIn('not the first time',s)

    def test_lyra_chapter_5_chronological_order_repaired(self):
        l=read('09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.4.md')
        self.assertLess(l.index('### L5.1'),l.index('### L5.2'))
        self.assertLess(l.index('### L5.2'),l.index('### L5.0'))
        self.assertLess(l.index('### L5.0'),l.index('### L5.4'))
        self.assertIn('Dante sees what Steffan is hiding',l)

    def test_canon_recognition_vs_reciprocity(self):
        c=read('02_Story_Bibles/Dante_Character_Addendum_v2.2.md')
        self.assertIn('more emotionally mature',c)
        self.assertIn('spite',c)
        self.assertIn('not established',c.lower())
        self.assertIn('private Day-11',c)

    def test_lyra_no_reunion_as_triumph(self):
        d=read('22_Dante_Campaign/Dante_Playable_Screenplay_v0.1.md')
        self.assertIn('She chooses',d) if 'She chooses' in d else self.assertIn('Lyra chooses',d)
        self.assertIn('Lyra is never',d) if 'Lyra is never' in d else self.assertIn('Lyra remains',d)

if __name__=='__main__': unittest.main()
