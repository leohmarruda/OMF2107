import itertools
import unittest
from dataclasses import replace
from christian_secondary_state import (
    ChristianChoices, christian_secondary_arc, evidence_known_by_christian,
    HISTORICAL_FACTS, INDEPENDENT_EVIDENCE
)

class ChristianSecondaryTests(unittest.TestCase):
    def test_evidence_knowledge_gating(self):
        self.assertEqual(len(evidence_known_by_christian(0)),0)
        for day, n in [(4,0),(5,1),(7,1),(8,2),(9,2),(10,3),(11,4),(13,4)]:
            self.assertEqual(len(evidence_known_by_christian(day)),n)
        with self.assertRaises(ValueError): evidence_known_by_christian(-1)

    def test_history_independent_of_raven_and_pilot(self):
        for pilot, rv, elim in itertools.product(
            ['Ari','Lyra','Mara','Ren','Angel','Crystal','Raven'],
            ['full','selective','false_denial'], [True,False]):
            arc=christian_secondary_arc(selected_pilot=pilot,raven_disclosure=rv,pilot_eliminated=elim)
            self.assertEqual(arc['historical_facts'],HISTORICAL_FACTS)
            self.assertEqual(arc['evidence_immutable'],INDEPENDENT_EVIDENCE)
            self.assertEqual(len(arc['evidence_by_day'][13]),4)
            self.assertFalse(arc['tournament_modified'])
            self.assertTrue(arc['unproven_but_for_rescue'])
            self.assertFalse(arc['kill_order_signer_unknown'])
            self.assertFalse(arc['kill_order_signer_known_by_day'][13])
            self.assertTrue(arc['kill_order_signer_known_by_day'][30])
            self.assertTrue(arc['legal_outcome_unresolved'])

    def test_order_is_increasing(self):
        arc=christian_secondary_arc()
        days=[arc['scene_days'][name] for name in arc['scene_ids']]
        self.assertEqual(days,sorted(days))

    def test_order_of_four_discoveries(self):
        arc=christian_secondary_arc()
        scene=arc['scene_ids']
        ids=['CH2.3_E1_CUSTODY_GAP','CH3.1_E2_SIGNED_RELAY_HOLD',
            'CH4.1_E3_LETHAL_COMMAND_FORENSIC','CH5.1_E4_RESTORE_REQUEST']
        self.assertEqual([arc['scene_days'][id] for id in ids],[5,8,10,11])
        self.assertEqual([scene.index(x) for x in ids], sorted(scene.index(x) for x in ids))

    def test_rescue_before_nova_secret_veto(self):
        arc=christian_secondary_arc()
        s=arc['scene_ids']; self.assertLess(s.index('CH5.2_GENUINE_NOVA_RESCUE'),s.index('CH6.1_POST_FINAL_NOVA_VETO'))

    def test_unverified_romance_cannot_trigger(self):
        c=ChristianChoices(romance_intent='leena')
        self.assertFalse(christian_secondary_arc(c)['leena_romance'])

    def test_full_mutual_posthearing_romance_requires_recusal(self):
        c=ChristianChoices(romance_intent='leena',both_adults_confirmed=True,
            leena_independently_reciprocates=True,christian_reciprocates=True,
            leena_editor_recusal_accepted=True,leena_recusal_day=12)
        a=christian_secondary_arc(c)
        self.assertTrue(a['leena_romance'])
        self.assertFalse(a['day10_kiss'])
        self.assertIn('CH6.3_LEENA_RECIPROCAL_ROMANCE',a['scene_ids'])
        self.assertNotIn('CH4.3_OPTIONAL_MUTUAL_KISS',a['scene_ids'])

    def test_prehearing_kiss_gated_by_earlier_recusal(self):
        c=ChristianChoices(romance_intent='leena',both_adults_confirmed=True,
            leena_independently_reciprocates=True,christian_reciprocates=True,
            leena_editor_recusal_accepted=True,leena_recusal_day=9,dance_kiss_intent=True)
        self.assertTrue(christian_secondary_arc(c)['day10_kiss'])
        self.assertFalse(christian_secondary_arc(replace(c,leena_recusal_day=11))['day10_kiss'])

    def test_conflicting_partners_block_leena_romance(self):
        c=ChristianChoices(romance_intent='leena',both_adults_confirmed=True,
            leena_independently_reciprocates=True,christian_reciprocates=True,
            leena_editor_recusal_accepted=True,leena_recusal_day=9,dance_kiss_intent=True)
        for key in ('leena_has_partner','christian_has_partner','leena_other_route_reserved'):
            a=christian_secondary_arc(replace(c, **{key: True}))
            self.assertFalse(a['leena_romance']); self.assertFalse(a['day10_kiss'])

    def test_family_boundary_cost_does_not_change_evidence(self):
        base=christian_secondary_arc()
        assertive=christian_secondary_arc(ChristianChoices(family_dynamic='intrusive'))
        self.assertFalse(base['family_trust_cost'])
        self.assertTrue(assertive['family_trust_cost'])
        self.assertEqual(base['evidence_by_day'],assertive['evidence_by_day'])
        self.assertFalse(assertive['crystal_romance_determined_by_christian'])

    def test_all_career_endings_unlocked_without_romance(self):
        for career in ('records_service','fieldwork','music_break'):
            arc=christian_secondary_arc(ChristianChoices(after_hearing=career))
            self.assertEqual(arc['christian_ending'],career)
            self.assertFalse(arc['leena_romance'])
            self.assertEqual(len(arc['evidence_by_day'][30]),5)

    def test_pressure_and_investigator_meeting_do_not_gate_truth(self):
        for p,m,fam in itertools.product(
                ('methodical','public_pressure'),
                ('formal','demand_meeting','avoid_face_to_face'),
                ('collaborate','parallel','private','intrusive')):
            arc=christian_secondary_arc(ChristianChoices(records_approach=p,raven_meeting=m,family_dynamic=fam))
            self.assertEqual(arc['evidence_immutable'],INDEPENDENT_EVIDENCE)

    def test_invalid_choice_rejected(self):
        with self.assertRaises(ValueError): christian_secondary_arc(ChristianChoices(after_hearing='arrest_raven'))
        with self.assertRaises(ValueError): christian_secondary_arc(selected_pilot='Christian')
        with self.assertRaises(ValueError): christian_secondary_arc(raven_disclosure='vindicated')

    def test_romance_does_not_change_nova_or_case(self):
        c=ChristianChoices(romance_intent='leena',both_adults_confirmed=True,
            leena_independently_reciprocates=True,christian_reciprocates=True,
            leena_editor_recusal_accepted=True,leena_recusal_day=9)
        a=christian_secondary_arc(c); b=christian_secondary_arc()
        for key in ('evidence_by_day','historical_facts','new_nova_veto_proven_day','kill_order_signer_unknown','kill_order_signer_known_by_day'):
            self.assertEqual(a[key],b[key])

if __name__ == '__main__': unittest.main()
