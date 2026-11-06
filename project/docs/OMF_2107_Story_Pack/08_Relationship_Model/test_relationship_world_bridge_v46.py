import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'13_Cross_Campaign_Audit'))
from world_state import WorldState,Event
from relationship_route_validator import StoryState
from relationship_world_bridge import eligible_with_world,relationship_conflicts
class RelationshipBridgeV46Tests(unittest.TestCase):
    def make_world(self, yes_a=True, yes_b=True):
        w=WorldState('Ari')
        for person,partner,yes in [('Ari','Mara',yes_a),('Mara','Ari',yes_b)]:
            w.apply(Event(person+'-decision','decision','group_stage',person,partner,(yes,)))
        return w
    def test_unilateral_choice_insufficient(self):
        local=StoryState('Ari',mutual_attraction=frozenset({'Ari:Mara'}))
        self.assertFalse(eligible_with_world(self.make_world(yes_b=False),local,'Ari:Mara'))
    def test_both_layers_required(self):
        w=self.make_world()
        self.assertFalse(eligible_with_world(w,StoryState('Ari'),'Ari:Mara'))
        self.assertTrue(eligible_with_world(w,StoryState('Ari',mutual_attraction=frozenset({'Ari:Mara'})),'Ari:Mara'))
    def test_cross_pilot_state_rejected(self):
        self.assertFalse(eligible_with_world(self.make_world(),StoryState('Mara',mutual_attraction=frozenset({'Ari:Mara'})),'Ari:Mara'))
    def test_unapproved_pair_cannot_be_enabled(self):
        self.assertEqual(relationship_conflicts(self.make_world(),'Cossette:Milano'),('unsupported_ending_pair',))
if __name__=='__main__':unittest.main()
