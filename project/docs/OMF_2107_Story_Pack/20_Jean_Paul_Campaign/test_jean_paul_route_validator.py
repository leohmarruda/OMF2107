import itertools
import unittest
from dataclasses import replace
from jean_paul_route_validator import (JeanPaulChoices, ESSENTIAL_CLUES,
                                      simulate_jean_paul, interpret)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate


class JeanPaulRouteTests(unittest.TestCase):
    def test_default_no_false_bracket(self):
        r = simulate_jean_paul(False, False)
        self.assertEqual(r['group_rank'], 3)
        self.assertFalse(r['qualified'])
        self.assertFalse(r['semifinal_played'])
        self.assertFalse(r['final_played'])
        self.assertEqual(r['player_elimination_match'], 'GROUP_STAGE')
        self.assertEqual(r['official_champion'], 'Ari')
        self.assertIn('JP-C4.1_NO_QF', r['scenes'])
        self.assertIn('JP-C6.1_SPECTATOR', r['scenes'])

    def test_group_fights_in_order(self):
        r = simulate_jean_paul(False, True)
        ref = simulate('Jean-Paul', (False, True), (False, False, False))
        self.assertEqual(r['official_champion'], ref['champion'])
        self.assertEqual(r['group_order'], ('GD2', 'GD3'))

    def test_two_wins_q4(self):
        r = simulate_jean_paul(True, True)
        self.assertEqual(r['group_rank'], 1)
        self.assertEqual(r['qf_id'], 'Q4')
        self.assertEqual(r['qf_opponent'], 'Lyra')

    def test_second_place_q3(self):
        r = simulate_jean_paul(False, True)
        self.assertEqual(r['group_rank'], 2)
        self.assertEqual(r['qf_id'], 'Q3')
        self.assertEqual(r['qf_opponent'], 'Steffan')

    def test_one_win_can_circular_eliminate(self):
        r = simulate_jean_paul(True, False)
        self.assertEqual(r['group_rank'], 3)
        self.assertTrue(r['group_circular'])
        self.assertFalse(r['qualified'])

    def test_all_32_fight_bit_patterns(self):
        for bits in itertools.product((False, True), repeat=5):
            r = simulate_jean_paul(bits[0], bits[1], bits[2:])
            self.assertEqual(len(r['essential_clues']), len(ESSENTIAL_CLUES))
            self.assertEqual(r['qf_id'] is not None, r['qualified'])
            self.assertEqual(r['final_played'], r['final_opponent'] is not None)
            self.assertIn('JP-C6.3_SPECIAL_NOVA', r['scenes'])
            self.assertEqual(r['nova_encounter'], 'SPECIAL_NOVA_AFTER_OFFICIAL_FINAL')
            self.assertFalse(r['day_13_e5_authenticated'])
            self.assertTrue(r['day_30_e5_authenticated'])

    def test_actual_title_requires_final_win(self):
        r = simulate_jean_paul(True, True, (True, True, True))
        self.assertTrue(r['player_champion'])
        self.assertEqual(r['official_champion'], 'Jean-Paul')

    def test_final_loss_no_title(self):
        r = simulate_jean_paul(True, True, (True, True, False))
        self.assertFalse(r['player_champion'])
        self.assertNotEqual(r['official_champion'], 'Jean-Paul')

    def test_qf_loss_gates_sf_and_final(self):
        r = simulate_jean_paul(True, True, (False, True, True))
        self.assertFalse(r['semifinal_played'])
        self.assertFalse(r['final_played'])

    def test_sf_loss_gates_final(self):
        r = simulate_jean_paul(True, True, (True, False, True))
        self.assertTrue(r['semifinal_played'])
        self.assertFalse(r['final_played'])

    def test_varga_only_with_all_gates(self):
        c = JeanPaulChoices(relationship_intent='varga', varga_boundary='conditional_contact',
            varga_available=True, varga_reciprocates=True, varga_active_consent=True,
            jp_active_consent=True, varga_stopped_collection=True, varga_disclosed=True,
            varga_accepts_oversight=True)
        r = simulate_jean_paul(False, False, choices=c)
        self.assertEqual(r['relationship_ending'], 'varga_conditional_romance')
        self.assertTrue(r['romance_committed'])
        self.assertIn('JP-C5.5_CONSENT_ELIGIBLE', r['scenes'])
        for field in ('varga_available', 'varga_reciprocates', 'varga_active_consent',
                      'jp_active_consent', 'varga_stopped_collection',
                      'varga_disclosed', 'varga_accepts_oversight', 'jp_available',
                      'no_professional_coercion'):
            altered = replace(c, **{field: False})
            self.assertFalse(simulate_jean_paul(False, False, choices=altered)['romance_committed'], field)
        self.assertFalse(simulate_jean_paul(False,False, choices=replace(c, varga_boundary='distance'))['romance_committed'])

    def test_selene_milano_exclusivity(self):
        c = JeanPaulChoices(relationship_intent='selene', selene_available=True,
                           selene_reciprocates=True, selene_active_consent=True,
                           selene_milano_cleared=True, jp_active_consent=True)
        self.assertEqual(simulate_jean_paul(False,False,choices=c)['relationship_ending'],'selene_proposed_romance')
        self.assertFalse(simulate_jean_paul(False,False,choices=replace(c,selene_milano_cleared=False))['romance_committed'])
        self.assertFalse(simulate_jean_paul(False,False,choices=replace(c,selene_available=False))['romance_committed'])

    def test_no_double_romance(self):
        c = JeanPaulChoices(relationship_intent='single')
        self.assertFalse(simulate_jean_paul(False,False,choices=c)['romance_committed'])
        self.assertEqual(simulate_jean_paul(False,False,choices=replace(c,relationship_intent='friendship'))['relationship_ending'], 'friendship')

    def test_varga_misconduct_independent_of_choice(self):
        for intent in ('varga','selene','single','friendship'):
            for evidence in ('protected_release','escrow_negotiation','brokerage'):
                for client in ('independent_audit','sell_to_bidder','war_inside_channel'):
                    c = JeanPaulChoices(relationship_intent=intent, evidence_policy=evidence,
                                        client_policy=client)
                    r = simulate_jean_paul(False,False,choices=c)
                    self.assertTrue(r['varga_ethics_breach'])
                    self.assertTrue(r['evidence_delivered_independently'])
                    self.assertTrue(r['lyra_notice_reachable'])
                    self.assertTrue(r['varga_no_match_fixing'])

    def test_romance_does_not_change_fights(self):
        results = []
        for intent in ('varga','selene','single','friendship'):
            c=JeanPaulChoices(relationship_intent=intent)
            results.append(simulate_jean_paul(True, True, (True,True,True), c)['tournament'])
        self.assertTrue(all(x == results[0] for x in results))

    def test_rescue_precedes_semifinal_and_final(self):
        r = simulate_jean_paul(True,True,(True,True,True))
        events = r['scenes']
        self.assertLess(events.index('JP-C5.1_DAY12_RESCUE'), events.index('JP-C5.2_SF'))
        self.assertLess(events.index('JP-C5.2_SF'), events.index('JP-C6.1_FINAL'))
        self.assertLess(events.index('JP-C6.1_FINAL'), events.index('JP-C6.3_SPECIAL_NOVA'))
        self.assertLess(r['timeline']['NOVA'],r['timeline']['DEVROE_E5'])

    def test_shared_final_irreversible(self):
        r = simulate_jean_paul(False,False)
        self.assertFalse(r['nova_survives_default'])
        self.assertEqual(r['shared_kreissack_last_line'], 'Apparently, I can still surprise you.')

    def test_invalid_values_rejected(self):
        for field in ('approach', 'client_policy', 'evidence_policy', 'varga_boundary',
                      'final_evidence_action','public_stance','relationship_intent'):
            with self.assertRaises(ValueError):
                simulate_jean_paul(False,False, choices=replace(JeanPaulChoices(), **{field:'invented'}))
        with self.assertRaises(ValueError):
            simulate_jean_paul(1,False)
        with self.assertRaises(ValueError):
            simulate_jean_paul(False,0)


if __name__ == '__main__':
    unittest.main()

# Separate static-continuity checks make review-clock invariants visible even
# when optional prose scenes are not dispatched by the executable state model.
class JeanPaulScreenplayClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.script = (Path(__file__).parent / 'Jean_Paul_Playable_Screenplay_v0.1.md').read_text()

    def test_day_11_confrontation_before_day_12_rescue(self):
        script = self.script
        p1 = script.index('### JP-C4.2 —')
        p2 = script.index('### JP-C5.0 —')
        p3 = script.index('### JP-C5.1 —')
        p4 = script.index('### JP-C5.2 —')
        p5 = script.index('### JP-C6.1 —')
        self.assertTrue(p1 < p2 < p3 < p4 < p5)
        self.assertIn('DAY 11', script[p2:p3])
        self.assertIn('DAY 12', script[p3:p4])

    def test_nova_and_day_30_separated(self):
        script = self.script
        self.assertLess(script.index('### JP-C6.3 —'), script.index('### JP-C6.5 —'))
        self.assertIn('E5', script[script.index('### JP-C6.5 —'):])
        self.assertIn('audience-only', script.lower())
