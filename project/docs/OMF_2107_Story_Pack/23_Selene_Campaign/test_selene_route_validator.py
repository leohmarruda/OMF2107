from dataclasses import replace
import itertools
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from selene_route_validator import SeleneChoices, EVIDENCE, simulate_selene
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate


class SeleneRouteTests(unittest.TestCase):
    def test_default_eliminated(self):
        s = simulate_selene(False, False)
        self.assertEqual(s['group_rank'], 3)
        self.assertFalse(s['qualified'])
        self.assertFalse(s['final_played'])
        self.assertEqual(s['champion'], 'Ari')
        self.assertEqual(s['player_elimination_match'], 'GROUP_STAGE')

    def test_screen_engine_input_translation(self):
        for a, c in itertools.product((False, True), repeat=2):
            s = simulate_selene(a, c)
            ref = simulate('Selene', (c, a), (False, False, False))
            self.assertEqual(s['tournament'], ref)
            self.assertEqual(s['screen_group_order'], ('GA3', 'GA2'))

    def test_both_wins_first(self):
        s = simulate_selene(True, True)
        self.assertEqual((s['group_rank'], s['qf_id'], s['qf_opponent']), (1, 'Q1', 'Ren'))

    def test_ari_only_second(self):
        s = simulate_selene(True, False)
        self.assertEqual((s['group_rank'], s['qf_id'], s['qf_opponent']), (2, 'Q2', 'Mara'))

    def test_crystal_only_is_circular_and_eliminated(self):
        s = simulate_selene(False, True)
        self.assertTrue(s['group_circular'])
        self.assertEqual(s['group_rank'], 3)
        self.assertFalse(s['qualified'])
        self.assertEqual(s['player_elimination_match'], 'GROUP_STAGE')

    def test_all_32_fight_inputs_no_false_scenes(self):
        for bits in itertools.product((False, True), repeat=5):
            a, c, q, sf, f = bits
            s = simulate_selene(a, c, (q, sf, f))
            games = s['tournament']['matches']
            for game in games:
                self.assertNotEqual(game['winner'], game['loser'])
                self.assertIn(game['winner'], (game['left'], game['right']))
            self.assertEqual(s['qualified'], s['qf_id'] is not None)
            self.assertEqual(s['semifinal_played'], 'SV5.3_SF' in s['scenes'])
            self.assertEqual(s['final_played'], 'SV6.1_FINAL' in s['scenes'])
            self.assertEqual(s['player_champion'], s['champion'] == 'Selene')
            if not s['qualified']:
                self.assertNotIn('SV4.2_QF', s['scenes'])
            if s['qualified']:
                self.assertIn('SV4.2_QF', s['scenes'])

    def test_milano_romance_requires_independent_choices(self):
        b = SeleneChoices(relationship_intent='milano')
        self.assertFalse(simulate_selene(False, False, choices=b)['romance_committed'])
        consent = replace(b, selene_active_consent=True, milano_available=True,
                          milano_reciprocates=True, milano_active_consent=True,
                          milano_business_power_separated=True, meaningful_time_elapsed=True)
        self.assertTrue(simulate_selene(False, False, choices=consent)['romance_committed'])
        for bad in (replace(consent, no_leverage_for_intimacy=False),
                    replace(consent, milano_available=False),
                    replace(consent, no_exclusive_external_commitment=False),
                    replace(consent, milano_business_power_separated=False)):
            self.assertFalse(simulate_selene(False, False, choices=bad)['romance_committed'])

    def test_jp_romance_requires_varga_cleared(self):
        b = SeleneChoices(relationship_intent='jean_paul', selene_active_consent=True,
                          jean_paul_available=True, jean_paul_reciprocates=True,
                          jean_paul_active_consent=True, meaningful_time_elapsed=True)
        self.assertFalse(simulate_selene(False, False, choices=b)['romance_committed'])
        b = replace(b, jean_paul_varga_ended=True)
        self.assertTrue(simulate_selene(False, False, choices=b)['romance_committed'])
        self.assertFalse(simulate_selene(False, False, choices=replace(b, jean_paul_reciprocates=False))['romance_committed'])

    def test_commercial_agency_is_not_evidence_removal(self):
        b = simulate_selene(False, False)
        for investigation, family, business, identity in itertools.product(
            ('independent_audit', 'commercial_leverage', 'withhold_for_now'),
            ('decline_illicit_access', 'negotiate_clean_license', 'seek_illicit_edge'),
            ('independent_competitor', 'conditional_reform', 'opportunistic_acquisition'),
            ('own_identity', 'limited_disclosure', 'deny_then_correct')):
            ch = SeleneChoices(investigation=investigation, family_mandate=family,
                               business_strategy=business, identity_strategy=identity)
            s = simulate_selene(False, False, choices=ch)
            self.assertEqual(s['essential_evidence'], b['essential_evidence'])
            self.assertEqual(s['tournament'], b['tournament'])
            self.assertEqual(s['champion'], 'Ari')

    def test_shared_reveal_timing_and_last_line(self):
        s = simulate_selene(False, False)
        self.assertEqual(s['kreissack_bio_discovery_day'], 9)
        self.assertEqual(s['semifinal_day'], 11)
        self.assertEqual(s['genuine_rescue_day'], 12)
        self.assertLess(s['scenes'].index('SV5.3_SPECTATOR'), s['scenes'].index('SV5.2_DAY12_RESCUE'))
        self.assertEqual(s['nova_veto_reveal_day'], 13)
        self.assertEqual(s['devroe_e5_authentication_day'], 30)
        self.assertFalse(s['devroe_e5_authenticated_day13'])
        self.assertFalse(s['nova_core_survives_default'])
        self.assertTrue(s['nova_boss_separate_from_tournament'])
        self.assertEqual(s['shared_kreissack_final_line'], 'Apparently, I can still surprise you.')
        self.assertEqual(s['essential_evidence'], EVIDENCE)

    def test_semifinal_before_rescue_on_advanced_route(self):
        s = simulate_selene(True, True, (True, False, False))
        self.assertTrue(s['semifinal_played'])
        self.assertLess(s['scenes'].index('SV5.3_SF'), s['scenes'].index('SV5.2_DAY12_RESCUE'))

    def test_invalid_choices_rejected(self):
        for key in ('identity_strategy', 'investigation', 'family_mandate',
                    'business_strategy', 'personal_ending', 'relationship_intent'):
            with self.subTest(key=key), self.assertRaises(ValueError):
                simulate_selene(False, False, choices=replace(SeleneChoices(), **{key: 'INVALID'}))

    def test_non_boolean_fight_rejected(self):
        with self.assertRaises(ValueError):
            simulate_selene(1, False)
        with self.assertRaises(ValueError):
            simulate_selene(False, 'no')


if __name__ == '__main__':
    unittest.main()
