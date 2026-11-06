import itertools
import unittest
from dataclasses import replace
from raven_route_validator import RavenChoices, simulate_raven_screen, CORE_CLUES

class RavenTests(unittest.TestCase):
    def test_default_elimination(self):
        r = simulate_raven_screen(False, False)
        self.assertEqual(r['group_rank'], 3)
        self.assertIsNone(r['qf_id'])
        self.assertFalse(r['raven_champion'])
        self.assertEqual(r['champion'], 'Ari')

    def test_single_win_over_mara_eliminates_in_circle(self):
        r = simulate_raven_screen(True, False)
        self.assertEqual(r['group_rank'], 3)
        self.assertIn('B', r['tournament']['circular_groups'])
        self.assertIn('R4.1_NO_QF', r['scene_ids'])

    def test_win_over_ren_qualifies_second(self):
        r = simulate_raven_screen(False, True, (False,))
        self.assertEqual(r['group_rank'], 2)
        self.assertEqual(r['qf_id'], 'Q1')
        self.assertEqual(r['qf_opponent'], 'Crystal')

    def test_two_wins_qualifies_first(self):
        r = simulate_raven_screen(True, True, (False,))
        self.assertEqual(r['group_rank'], 1)
        self.assertEqual(r['qf_id'], 'Q2')
        self.assertEqual(r['qf_opponent'], 'Ari')

    def test_possible_champion(self):
        r = simulate_raven_screen(True, True, (True, True, True))
        self.assertTrue(r['raven_champion'])
        self.assertEqual(r['final_opponent'], 'Lyra')
        self.assertEqual(r['match_ids'][-1], 'FINAL')

    def test_all_32_fight_patterns(self):
        for bits in itertools.product((False, True), repeat=5):
            r = simulate_raven_screen(bits[0], bits[1], bits[2:])
            self.assertEqual(r['qualified'], r['group_rank'] <= 2)
            self.assertEqual(r['raven_champion'], r['tournament']['champion']=='Raven')
            self.assertEqual(r['official_trophy'], r['raven_champion'])
            self.assertEqual(len(r['tournament']['matches']), 19)
            self.assertTrue(all(x['winner'] != x['loser'] for x in r['tournament']['matches']))
            self.assertEqual(r['nova_encounter'], 'SPECIAL_NOVA_AFTER_ACTUAL_FINAL')

    def test_dark_trait_is_always_present(self):
        for p in ('exploit','bargain','disclose','leave'):
            r = simulate_raven_screen(False,False,choices=RavenChoices(crystal_pressure=p))
            self.assertTrue(r['raven_enjoys_exploiting_crystal'])
            self.assertTrue(r['crystal_involuntary_pull_to_raven'])

    def test_exploitation_is_never_consent_or_romance_unlock(self):
        c = self._eligible()
        for pressure in ('exploit','bargain'):
            r = simulate_raven_screen(False,False,choices=replace(c,crystal_pressure=pressure))
            self.assertEqual(r['relationship_ending'],'dark_exposed')
            self.assertFalse(r['consensual_private_ds'])
            self.assertIn('R5.3_INFORMED_NO_INTIMACY',r['scene_ids'])

    def test_full_crystal_gate(self):
        c = self._eligible()
        r=simulate_raven_screen(False,False,choices=c)
        self.assertEqual(r['relationship_ending'],'crystal_consensual_ds')
        self.assertIn('R6.5_POSTHEARING_CONSENSUAL_DS',r['scene_ids'])

    def test_each_consent_and_reciprocity_gate(self):
        c = self._eligible()
        for field in ('independently_verified_disclosure','crystal_free','raven_free',
                      'crystal_reciprocates','chooses_ds','limits_agreed',
                      'crystal_active_consent','raven_active_consent'):
            r=simulate_raven_screen(False,False,choices=replace(c,**{field:False}))
            self.assertNotEqual(r['relationship_ending'],'crystal_consensual_ds',field)
        for field,value in [('gala_behavior','probe'),('money_choice','take_advance'),
                            ('shuttle_statement','false_denial'),('hearing_response','obstruct'),
                            ('final_offer','accept_trace')]:
            r=simulate_raven_screen(False,False,choices=replace(c,**{field:value}))
            self.assertFalse(r['consensual_private_ds'],field)

    def test_mara_independent_gates(self):
        c=RavenChoices(relationship_intent='mara',raven_free=True,mara_adult_verified=True,
            mara_free=True,mara_reciprocates=True,crystal_relationship_closed=True)
        self.assertEqual(simulate_raven_screen(False,False,choices=c)['relationship_ending'],'mara_romance')
        for f in ('raven_free','mara_adult_verified','mara_free','mara_reciprocates','crystal_relationship_closed'):
            r=simulate_raven_screen(False,False,choices=replace(c,**{f:False}))
            self.assertEqual(r['relationship_ending'],'mara_friendship_only')

    def test_investigation_survives_every_misconduct(self):
        for opts in (RavenChoices(crystal_pressure='exploit',money_choice='take_advance'),
                     RavenChoices(shuttle_statement='false_denial',hearing_response='obstruct',final_offer='obstruct'),
                     RavenChoices(relationship_intent='single')):
            r=simulate_raven_screen(False,False,choices=opts)
            self.assertTrue(r['independent_shuttle_inquiry'])
            self.assertEqual(r['core_clues'],CORE_CLUES)

    def test_optional_romance_never_changes_match_results(self):
        base=simulate_raven_screen(True,True,(True,True,True),RavenChoices())
        c=self._eligible()
        other=simulate_raven_screen(True,True,(True,True,True),c)
        self.assertEqual(base['tournament'],other['tournament'])

    def test_scene_and_event_order(self):
        r=simulate_raven_screen(True,True,(True,True,False))
        s=r['scene_ids']
        self.assertLess(s.index('R4.2'),s.index('R5.2'))
        self.assertLess(s.index('R5.2'),s.index('R6.2'))
        self.assertLess(s.index('R6.1_FINAL'),s.index('R6.2'))
        self.assertLess(r['timeline']['S_AB'],r['timeline']['RESCUE'])

    def test_validation_of_invalid_choices(self):
        with self.assertRaises(ValueError):
            simulate_raven_screen(False,False,choices=RavenChoices(crystal_pressure='compel'))

    @staticmethod
    def _eligible():
        return RavenChoices(relationship_intent='crystal',crystal_pressure='disclose',
            independently_verified_disclosure=True,raven_free=True,crystal_free=True,
            crystal_reciprocates=True,chooses_ds=True,limits_agreed=True,
            crystal_active_consent=True,raven_active_consent=True)

if __name__=='__main__':
    unittest.main()
