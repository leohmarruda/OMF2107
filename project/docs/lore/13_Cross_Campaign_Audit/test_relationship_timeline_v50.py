import unittest
from world_state import Event, StateConflict, WorldState
from relationship_timeline import new_canonical_world, relationship_view

class TimelineV50Tests(unittest.TestCase):
    def test_baselines_all_pilots_independent(self):
        for pilot in ('Ari','Dante','Lyra','Crystal','Milano','Raven','Selene'):
            w=new_canonical_world(pilot)
            v=relationship_view(w,'day0_1')
            self.assertIn(frozenset(('Dante','Lyra')),v.committed)
            self.assertIn(frozenset(('Cossette','Ibrahim')),v.committed)
            self.assertIn(frozenset(('Cossette','Milano')),v.casual)
            self.assertNotIn(frozenset(('Cossette','Milano')),v.committed)
            self.assertFalse(v.cnm_terms_specified)
            self.assertFalse(v.crystal_knows_raven_manipulation)
        a=new_canonical_world('Ari'); b=new_canonical_world('Lyra')
        a.apply(Event('lyra_decides','decision','group_stage','Lyra','Dante',(False,)))
        self.assertNotIn(('Lyra','Dante'),b.decisions)

    def test_earlier_scenes_do_not_see_later_breakup(self):
        w=new_canonical_world('Lyra')
        w.apply(Event('lyra_no','decision','day11_ab_semifinal','Lyra','Dante',(False,)))
        w.apply(Event('breakup','separate','day11_ab_semifinal','Lyra','Dante'))
        pair=frozenset(('Lyra','Dante'))
        self.assertIn(pair,relationship_view(w,'group_stage').committed)
        self.assertIn(pair,relationship_view(w,'day11_ab_semifinal',through_event_id='lyra_no').committed)
        self.assertNotIn(pair,relationship_view(w,'day11_ab_semifinal',through_event_id='breakup').committed)
        self.assertNotIn(pair,relationship_view(w,'epilogue').committed)

    def test_casual_end_does_not_end_couple(self):
        w=new_canonical_world('Milano')
        w.apply(Event('fling_ended','end_casual_connection','group_stage','Cossette','Milano'))
        self.assertNotIn(frozenset(('Cossette','Milano')),relationship_view(w,'group_stage').casual)
        self.assertIn(frozenset(('Cossette','Ibrahim')),relationship_view(w,'epilogue').committed)
        self.assertIn(frozenset(('Cossette','Milano')),relationship_view(w,'day0_1').casual)

    def test_crystal_knowledge_only_after_independent_clue(self):
        w=new_canonical_world('Crystal')
        w.apply(Event('evidence','clue','day12_rescue','Crystal','raven_manipulation',('independent evidence',)))
        self.assertFalse(relationship_view(w,'day11_ab_semifinal').crystal_knows_raven_manipulation)
        self.assertTrue(relationship_view(w,'day12_rescue').crystal_knows_raven_manipulation)

    def test_invalid_boundary_does_not_modify_world(self):
        w=new_canonical_world('Dante')
        before=list(w.events)
        with self.assertRaises(StateConflict): w.as_of('day0_1',through_event_id='missing')
        with self.assertRaises(StateConflict): w.as_of('day0_1',through_event_id='future')
        self.assertEqual(w.events,before)

    def test_baseline_rejects_arbitrary_pair_and_late_insertion(self):
        w=WorldState('Ari')
        with self.assertRaises(StateConflict):
            w.apply(Event('bad','baseline_bond','day0_1','Ari','Lyra',('author_relationship_canon_v4.7_v4.8',)))
        w=new_canonical_world('Ari')
        w.apply(Event('x','story','day9_reveal',target='misc'))
        with self.assertRaises(StateConflict):
            w.apply(Event('late','baseline_bond','day9_reveal','Dante','Lyra',('author_relationship_canon_v4.7_v4.8',)))

if __name__ == '__main__': unittest.main()
