from copy import deepcopy
from hanoi_decorator import HanoiDecorator

class HanoiState:
    def __init__(self, n_towers, ndisk=3):
        self.n_towers = n_towers
        self.towers = None
        self.ndisk = ndisk

    # mettre les disques sur la première tige
    def initialiser(self):
        self.towers = [list() for i in range(self.n_towers)]
        for i in range(self.ndisk, 0, -1):
            self.towers[0].append(i)

    def setDisks(self, disks):
        self.towers = disks

    def possible_moves(self):
        moves = []
        for i, source in enumerate(self.towers):
            if source:  # Si la tige source n'est pas vide
                for j, target in enumerate(self.towers):
                    if i != j:  # Ne pas déplacer vers la même tige
                        if (
                            not target or source[-1] < target[-1]
                        ):  # Respecter la règle des disques
                            new_towers = deepcopy(self.towers)
                            new_towers[j].append(new_towers[i].pop())

                            # Créez une nouvelle instance de HanoiState
                            new_state = HanoiState(self.n_towers)
                            new_state.setDisks(new_towers)

                            # Décorez l'état avec HanoiDecorator
                            decorated_state = HanoiDecorator(new_state)
                            moves.append(decorated_state)
        return moves

    def is_final_state(self):
        return len(self.towers[-1]) == 3 and self.towers[-1] == sorted(
            self.towers[-1], reverse=True
        )

    def __repr__(self):
        return str(self.towers)

    def __hash__(self):
        return hash(tuple(tuple(t) for t in self.towers))

    def __eq__(self, other):
        return self.towers == other.towers