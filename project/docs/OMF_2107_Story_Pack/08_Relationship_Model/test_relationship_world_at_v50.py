import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "13_Cross_Campaign_Audit"))
from world_state import Event
from relationship_timeline import new_canonical_world
from relationship_world_bridge import relationship_conflicts

class TimeAwareBridgeTest(unittest.TestCase):
    def test_future_decision_not_visible_before_scene(self):
        w=new_canonical_world('Ari')
        w.apply(Event('a_yes','decision','day12_rescue','Ari','Mara',(True,)))
        w.apply(Event('m_yes','decision','day12_rescue','Mara','Ari',(True,)))
        self.assertIn('Ari:no_independent_yes',relationship_conflicts(w.as_of('group_stage'),'Ari:Mara'))
        self.assertEqual(relationship_conflicts(w.as_of('day12_rescue'),'Ari:Mara'),())

if __name__=='__main__': unittest.main()
