class HanoiDecorator:
    def __init__(self, hanoi_state):
        self.hanoi_state = hanoi_state
        self.parents = dict()


    def possible_moves(self):
        moves = self.hanoi_state.possible_moves()
        decorated_moves = []
        for move in moves:
            # Décorez chaque état enfant
            decorated_move = HanoiDecorator(move)
            # Journalisez le parent
            decorated_move.parents[decorated_move] = self
            decorated_moves.append(decorated_move)
        return decorated_moves

    def __getattr__(self, attr):
        # Délègue les appels d'attributs/méthodes non surchargés à l'objet décoré
        return getattr(self.hanoi_state, attr)

    def __hash__(self):
        return hash(self.hanoi_state)

    def __eq__(self, other):
        return self.hanoi_state == other.hanoi_state
