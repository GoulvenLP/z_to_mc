from collections import deque
from rooted_graph import RootedGraph
from hanoi_decorator import HanoiDecorator
from hanoi_state import HanoiState


class Hanoi(RootedGraph):

    def __init__(self, n_towers, ndisk=3):
        self.initial_state = HanoiState(n_towers=n_towers, ndisk=ndisk)
        self.initial_state.initialiser() 


    def bfs_hanoi(self, initial_state, is_final_state):
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
                return current_state

            # Explore les états suivants
            for next_state in current_state.possible_moves():
                queue.append((next_state, path + [current_state]))
        return None  # Aucun chemin trouvé

    def neighbors(self, v : HanoiState):
        return v.possible_moves()
    
    def roots(self):
        return [self.initial_state]

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
            current_state = current_state.parents.get(current_state)
        return list(reversed(trace))  # pour avoir les tours de gauche à droite





def main():

    hanoi_game = Hanoi(n_towers=3, ndisk=3)

    print("[+] Recherche d'une solution...")
    decorated_state = HanoiDecorator(hanoi_game.initial_state)
    solution = hanoi_game.bfs_hanoi(decorated_state, HanoiState.is_final_state)

    if solution:
        print("[+] Solution trouvée !")
        # Affiche les états visités grâce au décorateur
        print("[+] Trace des états visités :")
        print("-------------------------------")
        solution_path = hanoi_game.getTrace(solution)
        number_of_moves = len(solution_path)
        print("[+] Moves : " + str(number_of_moves))
        for state in hanoi_game.getTrace(solution):
            print("|->" + str(state))
        print("-------------------------------")
    else:
        print("Aucune solution trouvée.")


if __name__ == "__main__":
    main()
