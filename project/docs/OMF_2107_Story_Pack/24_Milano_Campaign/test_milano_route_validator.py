from dataclasses import replace
import itertools
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from milano_route_validator import MilanoChoices, EVIDENCE, simulate_milano, interpret_milano
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate


class MilanoRouteTests(unittest.TestCase):
    def test_default_eliminated_and_nonromantic(self):
        r = simulate_milano(False, False)
        self.assertEqual((r['group_rank'],r['qualified'],r['champion']), (3,False,'Ari'))
        self.assertEqual(r['relationship_ending'],'solo')
        self.assertEqual(r['elimination_match'],'GROUP_STAGE')

    def test_screen_to_engine_adapter(self):
        for l,s in itertools.product((False, True), repeat=2):
            a=simulate_milano(l,s)
            b=simulate('Milano',(s,l),(False,False,False))
            self.assertEqual(a['tournament'], b)
            self.assertEqual(a['screen_group_order'], ('GC3','GC2'))

    def test_lyra_win_steffan_loss_second(self):
        r=simulate_milano(True,False)
        self.assertEqual((r['group_rank'],r['qf_id'],r['qf_opponent']), (2,'Q4','Angel'))

    def test_steffan_win_lyra_loss_circle_eliminated(self):
        r=simulate_milano(False,True)
        self.assertTrue(r['group_circular'])
        self.assertEqual(r['group_rank'],3)
        self.assertFalse(r['qualified'])

    def test_both_wins_first(self):
        r=simulate_milano(True,True)
        self.assertEqual((r['group_rank'],r['qf_id'],r['qf_opponent']), (1,'Q3','Dante'))

    def test_all_32_match_input_combinations(self):
        for inputs in itertools.product((False,True),repeat=5):
            l,s,q,sf,f=inputs
            r=simulate_milano(l,s,(q,sf,f))
            self.assertEqual(r['qualified'],r['qf_id'] is not None)
            self.assertEqual(r['semifinal_played'], 'MA5.3_DAY12_SF' in r['scenes'])
            self.assertEqual(r['final_played'], 'MA6.1_FINAL' in r['scenes'])
            self.assertEqual(r['player_champion'],r['champion']=='Milano')
            self.assertEqual('MA4.1_QF' in r['scenes'],r['qualified'])
            for m in r['tournament']['matches']:
                self.assertNotEqual(m['winner'],m['loser'])
                self.assertIn(m['winner'],(m['left'],m['right']))

    def test_only_winning_actual_final_awards_championship(self):
        r=simulate_milano(True,True,(True,True,True))
        self.assertTrue(r['player_champion'])
        self.assertEqual(r['champion'],'Milano')
        r=simulate_milano(True,True,(True,True,False))
        self.assertTrue(r['final_played'])
        self.assertFalse(r['player_champion'])
        self.assertNotEqual(r['champion'],'Milano')

    def test_eliminated_route_still_reaches_nova(self):
        r=simulate_milano(False,False)
        self.assertIn('MA6.2_DAY13_NOVA',r['scenes'])
        self.assertNotIn('MA6.1_FINAL',r['scenes'])
        self.assertTrue(r['nova_boss_separate_from_official_tournament'])

    def test_selene_interest_alone_not_ending(self):
        b=MilanoChoices(relationship_intent='selene')
        r=simulate_milano(False,False,choices=b)
        self.assertEqual(r['relationship_ending'],'selene_unresolved')
        self.assertFalse(r['romance_committed'])

    def test_selene_romance_requires_external_recipient_choice(self):
        b=MilanoChoices(relationship_intent='selene', milano_active_consent=True,
                        selene_available=True, selene_reciprocates=True,
                        selene_active_consent=True, meaningful_time_elapsed=True,
                        separated_corporate_leverage=True)
        self.assertFalse(simulate_milano(False,False,choices=b)['romance_committed'])
        b=replace(b,selene_chooses_milano=True)
        self.assertTrue(simulate_milano(False,False,choices=b)['romance_committed'])
        for invalid in (replace(b,no_other_exclusive_commitments=False),
                        replace(b,no_coercive_bargain=False),
                        replace(b,separated_corporate_leverage=False),
                        replace(b,selene_active_consent=False),
                        replace(b,selene_available=False),
                        replace(b,meaningful_time_elapsed=False)):
            self.assertFalse(simulate_milano(False,False,choices=invalid)['romance_committed'])

    def test_romance_and_policy_do_not_change_fights_or_evidence(self):
        base=simulate_milano(True,True,(True,True,True))
        alt=simulate_milano(True,True,(True,True,True),
            MilanoChoices(relationship_intent='selene',board_strategy='emergency_takeover',
                          institutional_ending='consolidate',review='bury_waiver'))
        self.assertEqual(base['tournament'],alt['tournament'])
        self.assertEqual(base['essential_evidence'],alt['essential_evidence'])
        self.assertIn('MA6.4_DARK_CONSOLIDATION',alt['scenes'])
        self.assertIn('MA6.4_HISTORICAL_CULPABILITY',alt['scenes'])

    def test_reveals_and_scene_order(self):
        for wins in itertools.product((False,True),repeat=2):
            r=simulate_milano(*wins,(True,True,True))
            scenes=r['scenes']
            anchors=('MA4.3_DAY9_SURVIVAL','MA5.1_DAY11_VARGA','MA5.2_DAY12_RESCUE',
                    'MA5.3_DAY12_SF' if r['semifinal_played'] else 'MA5.3_DAY12_NOT_PLAYING',
                    'MA6.2_DAY13_NOVA','MA6.5_DAY30_E5_AUTHENTICATION')
            self.assertEqual(list(map(scenes.index,anchors)), sorted(map(scenes.index,anchors)))
            self.assertEqual(r['devroe_order_authentication_day'],30)
            self.assertFalse(r['devroe_order_authenticated_by_day13'])
            self.assertFalse(r['nova_core_survives_default'])
            self.assertEqual(r['shared_kreissack_final_line'], 'Apparently, I can still surprise you.')

    def test_history_immutable_even_for_dark_route(self):
        for ending in ('independent_reform','managed_reform','consolidate'):
            r=simulate_milano(False,False,choices=MilanoChoices(institutional_ending=ending))
            self.assertTrue(r['milano_prior_vote_history_fixed'])
            self.assertTrue(r['evidence_independent_of_romance_and_rank'])
            self.assertIn('milano_original_limited_authorization',r['essential_evidence'])

    def test_selene_milano_cross_pov_reciprocity_is_representable(self):
        # Separate local POV contracts can agree on the same independently
        # confirmed romance. This is NOT the missing global save-state layer.
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '23_Selene_Campaign'))
        from selene_route_validator import SeleneChoices, simulate_selene
        milano = MilanoChoices(relationship_intent='selene', milano_active_consent=True,
            selene_available=True,selene_reciprocates=True,selene_chooses_milano=True,
            selene_active_consent=True,meaningful_time_elapsed=True,
            separated_corporate_leverage=True)
        selene = SeleneChoices(relationship_intent='milano',selene_active_consent=True,
            milano_available=True,milano_reciprocates=True,milano_active_consent=True,
            milano_business_power_separated=True,meaningful_time_elapsed=True)
        self.assertTrue(simulate_milano(False,False,choices=milano)['romance_committed'])
        self.assertTrue(simulate_selene(False,False,choices=selene)['romance_committed'])
        self.assertFalse(simulate_selene(False,False,choices=replace(selene,
            milano_available=False))['romance_committed'])
        self.assertFalse(simulate_milano(False,False,choices=replace(milano,
            selene_chooses_milano=False))['romance_committed'])

    def test_invalid_choices_rejected(self):
        with self.assertRaises(ValueError):
            simulate_milano(False,False,choices=MilanoChoices(institutional_ending='becomes_nova'))
        with self.assertRaises(ValueError):
            simulate_milano(1,False)
        with self.assertRaises(ValueError):
            interpret_milano(MilanoChoices(),simulate('Selene',(False,False),()))

    def test_script_has_expected_branch_sections(self):
        script=(Path(__file__).parent/'Milano_Playable_Screenplay_v0.1.md').read_text(encoding='utf8')
        for text in ('MA2.1','MA3.1','MA3.2','MA4.3','MA5.2','MA5.3','MA6.2','MA6.5',
                     'Apparently, I can still surprise you.', 'Day 30'):
            self.assertIn(text,script)

if __name__=='__main__': unittest.main()
