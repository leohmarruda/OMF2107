import unittest
from pathlib import Path
from dataclasses import replace
from dante_route_validator import DanteChoices, simulate_dante
ROOT=Path(__file__).resolve().parents[1]

class DanteV23CanonTests(unittest.TestCase):
    def test_author_established_default_nonromantic(self):
        c=(ROOT/'02_Story_Bibles/Dante_Character_Addendum_v2.3.md').read_text()
        self.assertIn('default',c.lower()); self.assertIn('nonromantic',c.lower())
        self.assertIn('change the course',c)

    def test_active_dante_scenes_present_and_time_order(self):
        d=(ROOT/'22_Dante_Campaign/Dante_Playable_Screenplay_v0.2.md').read_text()
        self.assertLess(d.index('### DV2.3'),d.index('### DV5.2'))
        self.assertLess(d.index('### DV5.2'),d.index('### DV6.4'))
        self.assertIn('default is still nonromantic',d)

    def test_steffan_view_separates_own_attraction_from_dante_default(self):
        s=(ROOT/'21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.3.md').read_text()
        self.assertIn('Dante defaults to nonromantic feelings',s)
        self.assertIn('DV5.2',s)

    def test_romance_is_player_led_but_not_forced_by_intent(self):
        base=DanteChoices(relationship_intent='steffan',respect_response='curiosity',
            day11_contact='listen',later_approach='explore',
            dante_independently_wants_steffan=True,steffan_available=True,
            steffan_independently_recognizes_attraction=True,
            steffan_independently_reciprocates=True,
            steffan_treated_lyra_accountably=True,future_interval_elapsed=True)
        good=simulate_dante(True,False,(False,),base)
        self.assertEqual(good['relationship_ending'],'steffan_future_proposal')
        self.assertTrue(good['dante_steffan_romance_path_developed'])
        for field,bad in [('respect_response','professional'),('day11_contact','boundary'),('later_approach','none')]:
            self.assertFalse(simulate_dante(True,False,(False,),replace(base,**{field:bad}))['romance_achieved'])
        self.assertFalse(simulate_dante(True,False,(False,),replace(base,steffan_independently_reciprocates=False))['romance_achieved'])

    def test_player_romance_does_not_change_fights_or_finale(self):
        a=simulate_dante(True,False,(False,))
        b=simulate_dante(True,False,(False,),DanteChoices(relationship_intent='steffan',respect_response='curiosity',day11_contact='listen',later_approach='explore'))
        self.assertEqual(a['tournament']['matches'],b['tournament']['matches'])
        self.assertEqual(a['official_champion'],b['official_champion'])
        self.assertEqual(a['kreissack_final_line'],b['kreissack_final_line'])
        self.assertLess(b['scenes'].index('DV2.3_CURIOSITY'), b['scenes'].index('DV5.2_CONFRONT_STEFFAN_DAY11'))
        self.assertLess(b['scenes'].index('DV5.2_LISTEN_OPTIONAL'), b['scenes'].index('DV6.4_POSSIBLE_FUTURE_NOT_DEFAULT'))
        self.assertLess(b['scenes'].index('DV6.4_POSSIBLE_FUTURE_NOT_DEFAULT'), b['scenes'].index('DV6.6_E5_DAY30'))
        self.assertTrue(a['day30_e5_authenticated'] and b['day30_e5_authenticated'])

if __name__=='__main__':unittest.main()
