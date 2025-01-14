from collections import deque
from rooted_graph import RootedGraph
from parent_tracer import ParentTracer
from hanoi_state import HanoiState
from copy import deepcopy


class Hanoi(RootedGraph):

    def __init__(self, n_towers, ndisk=3):
        self.state = HanoiState(n_towers=n_towers, ndisk=ndisk)
        self.state.initialiser() 
        self.rs = self.state

    def neighbors(self, v: HanoiState):
        moves = []
        for i, source in enumerate(v.towers):
            if source:  # Si la tige source n'est pas vide
                for j, target in enumerate(v.towers):
                    if i != j:  # Ne pas déplacer vers la même tige
                        if not target or source[-1] < target[-1]:  # Respecter la règle des disques
                            new_towers = deepcopy(v.towers)
                            new_towers[j].append(new_towers[i].pop())

                            # Créez une nouvelle instance de HanoiState
                            new_state = HanoiState(v.n_towers, v.ndisk)
                            new_state.setDisks(new_towers)

                            moves.append(new_state)  # Ajoutez le nouvel état aux voisins
        return moves

    
    def roots(self):
        return [self.rs]




def predicate_finder(graph: RootedGraph, predicate):
    """
    Recherche en largeur pour résoudre le problème des tours de Hanoï.
    :param graph: Le graphe représentant le jeu.
    :param predicate: La condition pour trouver l'état final.
    :return: L'état final trouvé.
    """
    queue = deque([(state) for state in graph.roots()])

    
    visited = set()

    while queue:
        current_state = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)
        # Vérifie si on a atteint l'état cible
        if predicate(current_state):
            return current_state
        # Explore les états suivants
        for next_state in graph.neighbors(current_state):
            queue.append(next_state)
    return None  # Aucun chemin trouvé






def main():
    hanoi = Hanoi(n_towers=3, ndisk=3)
    graph = ParentTracer(hanoi)

    print("[+] Recherche d'une solution...")
    
    # Faire la recherche avec predicate_finder
    solution = predicate_finder(graph, lambda state: state.is_final_state())
    if solution:
        print("[+] Solution trouvée !")
        print("[+] Etat final du jeu:")
        print(solution.towers)

        print("[+] Trace de la solution:")
        trace = graph.getTrace(hanoi.state, solution)
        for state in trace:
            print(state)
    else:
        print("Aucune solution trouvée.")


if __name__ == "__main__":
    main()
