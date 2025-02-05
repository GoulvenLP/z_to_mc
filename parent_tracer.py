from rooted_graph import RootedGraph

class ParentTracer(RootedGraph):
    def __init__(self, operand):
        self.operand = operand
        self.parents = {}

    def neighbors(self, v):
        moves = self.operand.neighbors(v)
        for move in moves:
            if move not in self.parents:
                self.parents[move] = [v]
        return moves

    def roots(self):
        roots = self.operand.roots()
        for root in roots:
            self.parents[root] = []
        return roots



    def getTrace(self, final_state):
        """
        Construit la trace complète en partant de l'état final.
        :param final_state: L'état final (instance de HanoiState).
        :return: Une liste des états de la trace.
        """
        path = []
        state = final_state
        while self.parents[state] !=  []: # l'etat est un etat initial
            path.append(state)
            state = self.parents[state][0]
        path.append(state)
        return list(reversed(path))
        
    def __getattr__(self, attr):
        # Délègue les appels d'attributs/méthodes non surchargés à l'objet décoré
        return getattr(self.operand, attr)

    def __hash__(self):
        return hash(self.operand)

    def __eq__(self, other):
        return self.operand == other.hanoi_state
