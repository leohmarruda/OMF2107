import unittest
from world_state import Event, StateConflict, WorldState

class CasualRelationshipTests(unittest.TestCase):
    def setup_couple(self):
        w=WorldState('Milano')
        w.apply(Event('d1','decision','day0_1',actor='Cossette',target='Ibrahim',payload=(True,)))
        w.apply(Event('d2','decision','day0_1',actor='Ibrahim',target='Cossette',payload=(True,)))
        w.apply(Event('steady','commit','day0_1',actor='Cossette',target='Ibrahim'))
        return w

    def test_casual_needs_reciprocal_choice_and_cnm(self):
        w=self.setup_couple()
        with self.assertRaises(StateConflict):
            w.apply(Event('casual','casual_connection','day0_1',actor='Cossette',target='Milano'))
        w.apply(Event('c','decision','day0_1',actor='Cossette',target='Milano',payload=(True,)))
        w.apply(Event('m','decision','day0_1',actor='Milano',target='Cossette',payload=(True,)))
        with self.assertRaises(StateConflict):
            w.apply(Event('casual','casual_connection','day0_1',actor='Cossette',target='Milano'))
        w.apply(Event('ia','decision','day0_1',actor='Ibrahim',target='Cossette',payload=(True,)))
        w.apply(Event('agreement','cnm_agreement','day0_1',actor='Cossette',payload=(('Ibrahim','Milano'),)))
        w.apply(Event('casual','casual_connection','day0_1',actor='Cossette',target='Milano'))
        self.assertIn(frozenset(('Cossette','Ibrahim')),w.bonds)
        self.assertNotIn(frozenset(('Cossette','Milano')),w.bonds)
        self.assertIn(frozenset(('Cossette','Milano')),w.casual_connections)

    def test_end_casual_leaves_steady_couple(self):
        w=self.setup_couple()
        w.apply(Event('c','decision','day0_1',actor='Cossette',target='Milano',payload=(True,)))
        w.apply(Event('m','decision','day0_1',actor='Milano',target='Cossette',payload=(True,)))
        w.apply(Event('ia','decision','day0_1',actor='Ibrahim',target='Cossette',payload=(True,)))
        w.apply(Event('agreement','cnm_agreement','day0_1',actor='Cossette',payload=(('Ibrahim','Milano'),)))
        w.apply(Event('casual','casual_connection','group_stage',actor='Cossette',target='Milano'))
        w.apply(Event('end','end_casual_connection','day9_reveal',actor='Cossette',target='Milano'))
        self.assertEqual(len(w.casual_connections),0)
        self.assertEqual(w.bonds,{frozenset(('Cossette','Ibrahim'))})

    def test_cannot_infer_new_commitment_from_casual(self):
        w=self.setup_couple()
        w.apply(Event('c','decision','day0_1',actor='Cossette',target='Milano',payload=(True,)))
        w.apply(Event('m','decision','day0_1',actor='Milano',target='Cossette',payload=(True,)))
        with self.assertRaises(StateConflict):
            w.apply(Event('new','commit','day0_1',actor='Cossette',target='Milano'))
        self.assertEqual(len(w.bonds),1)

if __name__=='__main__': unittest.main()
