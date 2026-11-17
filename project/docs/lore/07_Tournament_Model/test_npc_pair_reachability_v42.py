import unittest
from npc_pair_reachability import reachability,review_rows
from tournament_validator import GROUPS, DEFAULT_KNOCKOUT_WINNERS

class StructuralReachabilityTests(unittest.TestCase):
    def test_every_pair_reachable(self):
        rows = review_rows()
        self.assertEqual(len(rows), 66)
        self.assertTrue(all(x['structurally_reachable']=='yes' for x in rows))
    def test_stage_counts(self):
        possible = reachability()
        self.assertEqual(sum('quarterfinal' in v for v in possible.values()), 18)
        self.assertEqual(sum('semifinal' in v for v in possible.values()), 30)
        self.assertEqual(sum('final' in v for v in possible.values()), 36)
    def test_approval_flags(self):
        rows = review_rows()
        self.assertEqual(sum(x['needs_individual_approval']=='yes' for x in rows), 59)
        self.assertEqual(sum(bool(x['canon_default_winner']) for x in rows), len(DEFAULT_KNOCKOUT_WINNERS))
    def test_cross_bracket_final_only(self):
        row = next(x for x in review_rows() if {x['fighter_a'], x['fighter_b']} == {'Ari','Lyra'})
        self.assertEqual((row['quarterfinal_possible'],row['semifinal_possible'],row['final_possible']), ('no','no','yes'))

if __name__ == '__main__': unittest.main()
