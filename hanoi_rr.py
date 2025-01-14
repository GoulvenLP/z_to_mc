from rooted_relation import RootedRelation
from parent_tracer import ParentTracer
from predicate_finder import predicate_finder
from hanoi_state import HanoiState
from rr2rg import RR2RG

import copy

class HanoiRR(RootedRelation):

    def __init__(self, n_towers, ndisk=3):
        """
        Initialise le jeu de Hanoi avec un état initial basé sur HanoiState.
        :param n_towers: Nombre de tours.
        :param ndisk: Nombre de disques.
        """
        self.state = HanoiState(n_towers=n_towers, ndisk=ndisk)
        self.state.initialiser()  # Crée l'état initial
        self.rs = self.state  # L'état racine initial

    def initial(self):
        return self.rs

    def move(self, configuration, source, dest):
        """
        Vérifie et effectue un déplacement valide dans un état donné.
        :param configuration: Instance de HanoiState représentant l'état actuel.
        :param source: Index de la tour source.
        :param dest: Index de la tour destination.
        :return: Tuple (bool, nouvelle instance de HanoiState).
        """
        if configuration.towers[source] and (
            not configuration.towers[dest] or configuration.towers[source][-1] < configuration.towers[dest][-1]
        ):
            # Créer une nouvelle configuration en copiant l'état actuel
            new_configuration = copy.deepcopy(configuration)
            disk = new_configuration.towers[source].pop()
            new_configuration.towers[dest].append(disk)
            return True, new_configuration
        return False, None

    def actions(self, configuration):
        """
        Génère tous les déplacements possibles depuis une configuration donnée.
        :param configuration: Instance de HanoiState représentant l'état actuel.
        :return: Ensemble des nouvelles instances de HanoiState possibles.
        """
        actions = set()
        for src in range(configuration.n_towers):
            if configuration.towers[src]:  # Si la tour source n'est pas vide
                for dest in range(configuration.n_towers):
                    if src != dest:
                        allowed, new_config = self.move(configuration, src, dest)
                        if allowed:
                            actions.add(new_config)
        return actions

    def execute(self, configuration, action):
        """
            Executes the given action
            We work there on a copy!
            @action: action to execute
        """
        updated_config = copy.deepcopy(configuration)
        updated_config = action
        return updated_config        
        

def main():
    print("------- Hanoi Tower (RootedRelation) -------")

    hanoi_rr = HanoiRR(n_towers=3, ndisk=3)
    graph = ParentTracer(RR2RG(hanoi_rr))

    print("[+] Recherche d'une solution...")

    # Utiliser predicate_finder pour trouver la solution
    solution = predicate_finder(graph, lambda state: state.is_final_state())
    
    if solution:
        print("[+] Solution trouvée !")
        print("[+] Etat final du jeu:")
        print(solution.towers)

        print("[+] Trace de la solution:")
        trace = graph.getTrace(solution)
        for state in trace:
            print(state)
    else:
        print("Aucune solution trouvée.")


if __name__ == "__main__":
    main()
