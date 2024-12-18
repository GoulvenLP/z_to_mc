from collections import deque
from copy import deepcopy

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
                        if not target or source[-1] < target[-1]:  # Respecter la règle des disques
                            new_towers = deepcopy(self.towers)
                            new_towers[j].append(new_towers[i].pop())
                            new_state = HanoiState(self.n_towers)
                            new_state.setDisks(new_towers)
                            moves.append(new_state)
        return moves

    def is_final_state(self):
        return len(self.towers[-1]) == 3 and self.towers[-1] == sorted(self.towers[-1], reverse=True)
    
    def __repr__(self):
        return str(self.towers)

    def __hash__(self):
        return hash(tuple(tuple(t) for t in self.towers))

    def __eq__(self, other):
        return self.towers == other.towers


def bfs_hanoi(initial_state, is_final_state):
    """
    Recherche en largeur pour résoudre le problème des tours de Hanoï.
    :param initial_state: État initial des tiges.
    :param goal_state: État cible des tiges.
    :return: Le chemin de mouvements vers l'état cible.
    """
    queue = deque([(initial_state, [])]) 
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue
        visited.add(current_state)

        # Vérifie si on a atteint l'état cible
        if is_final_state(current_state):
            return path + [current_state]

        # Explore les états suivants
        for next_state in current_state.possible_moves():
            queue.append((next_state, path + [current_state]))

    return None  # Aucun chemin trouvé




def main():
    # État initial : tous les disques sur la première tige
    initial_state = HanoiState(3)
    initial_state.initialiser() # mettre les disques sur la première tige

    print("Recherche d'une solution...")
    solution = bfs_hanoi(initial_state, HanoiState.is_final_state)

    if solution:
        print("Solution trouvée en {} étapes :".format(len(solution) - 1))
        for step, state in enumerate(solution):
            print(f"Étape {step}: {state}")
    else:
        print("Aucune solution trouvée.")


if __name__ == "__main__":
    main()
