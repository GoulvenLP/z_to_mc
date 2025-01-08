from rooted_graph import RootedGraph

class ParentTracer(RootedGraph):
    def __init__(self, hanoi_state):
        self.hanoi_state = hanoi_state
        self.parents = dict()

    def neighbors(self):
        moves = self.hanoi_state.possible_moves()
        decorated_moves = []
        for move in moves:
            # Décorez chaque état enfant
            decorated_move = ParentTracer(move)
            # Journalisez le parent
            decorated_move.parents[decorated_move] = self
            decorated_moves.append(decorated_move)
        return decorated_moves

    # TODO FIX THIS (n, k)
    def getTrace(self, final_state):
        """
        Construit la trace complète en partant de l'état final.
        :param final_state: L'état final (instance de HanoiDecorator).
        :return: Une liste des états de la trace.
        """
        trace = []
        current_state = final_state
        while current_state:
            trace.append(current_state.towers)
            current_state = self.parents.get(current_state)
        return list(reversed(trace))  # pour avoir les tours de gauche à droite


    def __getattr__(self, attr):
        # Délègue les appels d'attributs/méthodes non surchargés à l'objet décoré
        return getattr(self.hanoi_state, attr)

    def __hash__(self):
        return hash(self.hanoi_state)

    def __eq__(self, other):
        return self.hanoi_state == other.hanoi_state
