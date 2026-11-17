import itertools
import sys
import unittest
from dataclasses import replace
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate
from steffan_route_validator import SteffanChoices, simulate_steffan, interpret


class SteffanRouteTests(unittest.TestCase):
    def test_default_canonical_bracket(self):
        r = simulate_steffan(True,True,(True,False))
        self.assertEqual((r['group_rank'],r['qf_id'],r['qf_opponent']), (1,'Q3','Dante'))
        self.assertTrue(r['semifinal_played'])
        self.assertEqual(r['semifinal_opponent'], 'Lyra')
        self.assertFalse(r['final_played'])
        self.assertEqual(r['official_champion'], 'Ari')

    def test_engine_screen_order(self):
        for milano,lyra in itertools.product((False, True),repeat=2):
            s = simulate_steffan(milano,lyra)
            base = simulate('Steffan',(lyra,milano),(False,False,False))
            self.assertEqual(s['official_champion'],base['champion'])
            self.assertEqual(s['tournament']['group_standings'],base['group_standings'])

    def test_both_group_losses_no_qf(self):
        r=simulate_steffan(False,False)
        self.assertFalse(r['qualified'])
        self.assertIn('ST4.1_NO_QF',r['scenes'])
        self.assertFalse(r['semifinal_played'])

    def test_full_victory_player_champion(self):
        r=simulate_steffan(True,True,(True,True,True))
        self.assertTrue(r['steffan_champion'])
        self.assertEqual(r['official_champion'],'Steffan')
        self.assertTrue(r['final_played'])

    def test_default_pairing_never_guaranteed_in_alt_scenarios(self):
        r=simulate_steffan(True,False,(True,False))
        self.assertEqual(r['qf_id'],'Q4')
        self.assertNotEqual(r['qf_opponent'],'Dante')

    def test_all_32_binary_patterns(self):
        for bits in itertools.product((False,True), repeat=5):
            r=simulate_steffan(bits[0],bits[1],bits[2:])
            self.assertEqual(r['qualified'],r['qf_id'] is not None)
            self.assertEqual(r['semifinal_played'],r['semifinal_opponent'] is not None)
            self.assertEqual(r['final_played'],r['final_opponent'] is not None)
            self.assertIn('ST5.2_DAY12_RESCUE',r['scenes'])
            self.assertIn('ST6.3_SPECIAL_NOVA',r['scenes'])
            self.assertTrue(r['lyra_chooses_independently'])
            self.assertFalse(r['day13_e5_known'])
            self.assertTrue(r['day30_e5_authenticated'])
            self.assertFalse(r['nova_default_survives'])
            self.assertEqual(r['kreissack_final_line'],'Apparently, I can still surprise you.')
            self.assertTrue(all(m['winner']!=m['loser'] for m in r['tournament']['matches']))

    def test_lyra_future_romance_requires_many_gates(self):
        base=SteffanChoices(relationship_intent='lyra', lyra_chose_steffan_earlier=True,
            lyra_dante_commitment_cleared=True, lyra_reciprocal_future_choice=True,
            lyra_post_tournament_repair=True, lyra_available=True,
            future_time_elapsed=True, private_behavior='respect_and_wait',
            day11_response='full_admission')
        self.assertEqual(simulate_steffan(True,True,(False,),base)['romance_ending'],'lyra_future_proposal')
        for field in ('lyra_reciprocal_future_choice','lyra_post_tournament_repair','future_time_elapsed','lyra_available','lyra_dante_commitment_cleared'):
            r=simulate_steffan(True,True,(False,),replace(base,**{field:False}))
            self.assertFalse(r['romance_achieved'])
        self.assertFalse(simulate_steffan(True,True,(False,),replace(base,coercive_control_recorded=True))['romance_achieved'])
        self.assertFalse(simulate_steffan(True,True,(False,),replace(base,private_behavior='press_for_control'))['romance_achieved'])

    def test_dante_future_romance_requires_active_consent(self):
        base=SteffanChoices(relationship_intent='dante',dante_truth='name_attraction',
            dante_available=True,dante_reciprocates=True,dante_independent_consent=True,
            dante_harm_addressed=True,future_time_elapsed=True,
            private_behavior='respect_and_wait')
        self.assertEqual(simulate_steffan(True,True,(False,),base)['romance_ending'],'dante_future_proposal')
        for field in ('dante_reciprocates','dante_independent_consent','dante_harm_addressed','future_time_elapsed','dante_available'):
            self.assertFalse(simulate_steffan(True,True,(False,),replace(base,**{field:False}))['romance_achieved'])
        self.assertFalse(simulate_steffan(True,True,(False,),replace(base,dante_truth='deny'))['romance_achieved'])
        self.assertFalse(simulate_steffan(True,True,(False,),replace(base,coercive_control_recorded=True))['romance_achieved'])

    def test_lyra_history_blocks_dante_without_commitment_clearance(self):
        ch=SteffanChoices(relationship_intent='dante',dante_truth='name_attraction',
            dante_available=True,dante_reciprocates=True,dante_independent_consent=True,
            dante_harm_addressed=True,future_time_elapsed=True,
            private_behavior='respect_and_wait',lyra_chose_steffan_earlier=True)
        self.assertFalse(simulate_steffan(True,True,(False,),ch)['romance_achieved'])

    def test_romance_cannot_affect_fight_results(self):
        for ch in (SteffanChoices(),SteffanChoices(relationship_intent='dante'),
            SteffanChoices(relationship_intent='lyra'),
            SteffanChoices(public_persona='precision',private_behavior='respect_and_wait')):
            s=simulate_steffan(True,True,(True,False),ch)
            self.assertEqual(s['official_champion'],'Ari')
            self.assertEqual(s['tournament']['matches'],simulate('Steffan',(True,True),(True,False))['matches'])

    def test_separate_nova_and_e5(self):
        s=simulate_steffan(False,False)
        self.assertTrue(s['nova_not_official_match'])
        t=s['timeline']
        self.assertLess(t['VARGA_NOTICE'],t['RESCUE'])
        self.assertLessEqual(t['RESCUE'],t['SF'])
        self.assertLess(t['SF'],t['OFFICIAL_FINAL'])
        self.assertEqual(t['NOVA'],t['OFFICIAL_FINAL'])
        self.assertLess(t['NOVA'],t['E5'])

    def test_bad_inputs_rejected(self):
        with self.assertRaises(ValueError):
            simulate_steffan(1,True)
        with self.assertRaises(ValueError):
            simulate_steffan(True,True,choices=replace(SteffanChoices(),relationship_intent='both'))
        with self.assertRaises(ValueError):
            interpret(SteffanChoices(),simulate('Lyra',(True,True),()))

if __name__ == '__main__':unittest.main()
