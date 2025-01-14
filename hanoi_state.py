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

    def is_final_state(self):
        return len(self.towers[-1]) == 3 and self.towers[-1] == sorted(
            self.towers[-1], reverse=True
        )

    def __repr__(self):
        return str(self.towers)

    def __hash__(self):
        return hash(tuple(tuple(t) for t in self.towers))

    def __eq__(self, other):
        # Comparer les tours pour déterminer l'égalité
        return isinstance(other, HanoiState) and self.towers == other.towers