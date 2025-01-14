from rooted_graph import RootedGraph
from rooted_relation import RootedRelation

class RR2RG(RootedGraph):
    def __init__(self, op : RootedRelation):
        self.op = op

    def roots(self):
        return [self.op.initial()]
    
    def neighbors(self, c):
        # faire appel à actions et execute
        pass