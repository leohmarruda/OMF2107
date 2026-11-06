import unittest
from tournament_validator import simulate, GROUPS
from tournament_scene_state import build_scene_state

class BranchConditionalSceneTests(unittest.TestCase):
    def test_champion_cannot_present_own_trophy(self):
        # Crystal can win the bracket when chosen; any NPC route can also
        # produce her victory, so presentation is derived from champion.
        state = build_scene_state(simulate('Crystal', (True, True), (True, True, True)))
        self.assertEqual(state['final_winner'], 'Crystal')
        self.assertEqual(state['ceremony_presenter_rule'], 'independent_awards_official')

    def test_player_champion_and_final_gates(self):
        for pilot in (p for g in GROUPS.values() for p in g):
            winning = build_scene_state(simulate(pilot, (True, True), (True, True, True)))
            self.assertTrue(winning['final_is_playable'])
            self.assertIn('FINAL', winning['played_knockout_ids'])
            self.assertEqual(winning['champion'], pilot)
            eliminated = build_scene_state(simulate(pilot, (False, False), ()))
            self.assertFalse(eliminated['final_is_playable'])
            self.assertNotIn('FINAL', eliminated['played_knockout_ids'])
            self.assertNotEqual(eliminated['champion'], pilot)

    def test_match_ledger_and_state_are_identical(self):
        state = build_scene_state(simulate('Ari', (False, True), (True, True, False)))
        self.assertEqual(state['final_winner'], state['matches_by_id']['FINAL']['winner'])
        self.assertEqual(state['finalists'], (state['matches_by_id']['FINAL']['left'], state['matches_by_id']['FINAL']['right']))

if __name__ == '__main__': unittest.main()
