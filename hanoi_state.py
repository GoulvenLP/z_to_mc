class HanoiState:
    
    def __init__(self, n_towers, ndisk=3):
        self.n_towers = n_towers
        self.towers = None
        self.ndisk = ndisk

    # mettre les disques sur la première tige
    def initialiser(self):
        """
            Initialises the hanoi game by putting all disks in the right 
            order on the first tower
        """
        self.towers = [list() for i in range(self.n_towers)]
        for i in range(self.ndisk, 0, -1):
            self.towers[0].append(i)

    def setDisks(self, configuration):
        """
            Sets a hanoi configuration.
            @configuration: a hanoi state, i.e [tower1, tower2, ...,  towern], each tower being lists,
            containing disk(s) or being empty
        """
        self.towers = configuration

    def is_final_state(self):
        """
            Verifies if the game is over, i.e that all disks are in the right order
            on the last tower
        """
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