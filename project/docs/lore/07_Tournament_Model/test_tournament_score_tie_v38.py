import unittest
from tournament_validator import simulate, GROUPS

class ScoreTieTests(unittest.TestCase):
    def test_two_way_tie_resolved_by_head_to_head(self):
        # A group: Crystal beats Ari; Ari beats Selene; Selene beats Crystal.
        # Crystal and Ari score 10 each, Selene scores 5. Crystal wins H2H.
        scores = {'GA1': (5, 4), 'GA2': (5, 3), 'GA3': (6, 2)}
        # Selected Crystal loses to Selene (GA2), wins versus Ari (GA1)
        result = simulate('Crystal', (True, False), (False,), group_match_scores=scores)
        a = result['group_standings']['A']
        self.assertEqual(a['ranking_method'], 'group_total_score_then_head_to_head')
        self.assertEqual(a['ranked'], ['Crystal', 'Ari', 'Selene'])
        self.assertNotIn('A', result['audit']['unapproved_cycle_seed_groups'])

    def test_three_way_equal_score_is_unresolved_in_strict_mode(self):
        scores = {'GA1': (5, 5), 'GA2': (5, 5), 'GA3': (5, 5)}
        with self.assertRaisesRegex(ValueError, 'three-way tied'):
            simulate('Crystal', (True, False), (False,), group_match_scores=scores, require_authored=True)

    def test_missing_score_is_not_silently_accepted(self):
        result = simulate('Crystal', (True, False), (False,), group_match_scores={'GA1': (4,3)})
        self.assertIn('A', result['audit']['unapproved_cycle_seed_groups'])

if __name__ == '__main__':
    unittest.main()
