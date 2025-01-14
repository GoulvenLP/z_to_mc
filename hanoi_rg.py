from collections import deque
from rooted_graph import RootedGraph
from parent_tracer import ParentTracer
from hanoi_state import HanoiState
from copy import deepcopy
from predicate_finder import predicate_finder

class HanoiRG(RootedGraph):

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

def main():
    hanoi = HanoiRG(n_towers=3, ndisk=3)
    graph = ParentTracer(hanoi)
    print("------- Hanoi Tower (RootedGraph) -------")
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
