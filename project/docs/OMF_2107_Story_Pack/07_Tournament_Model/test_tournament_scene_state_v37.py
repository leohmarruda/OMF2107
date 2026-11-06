import unittest
from tournament_validator import simulate, GROUPS
from tournament_scene_state import build_scene_state

class TournamentScreenBindings(unittest.TestCase):
    def test_bindings_across_all_playable_pilots(self):
        for pilot in (p for group in GROUPS.values() for p in group):
            for group_wins in ((False,False),(True,False),(False,True),(True,True)):
                result=simulate(pilot,group_wins,(True,True,True))
                state=build_scene_state(result)
                self.assertEqual(state['champion'],result['matches'][-1]['winner'])
                self.assertEqual(state['selected_pilot_is_champion'],state['champion']==pilot)
                self.assertIn(state['champion'],state['finalists'])
                self.assertTrue(state['official_tournament_over_before_nova'])

if __name__=='__main__':unittest.main()
