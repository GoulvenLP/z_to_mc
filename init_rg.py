from rooted_graph import RootedGraph

class InitRG(RootedGraph):
    """
    This class is used for the vivavicy properties verification.
    A new RG is initialized from a specific state of an existing Graph,
    in order to identify a loop.
    """

    def __init__(self, op, inits):
        self.op = op
        self.inits = inits
    
    def roots(self):
        return self.inits
    

    def neighbors(self, v):
        return self.op.neighbors(v)