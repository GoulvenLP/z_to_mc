from rooted_relation import RootedRelation
from rr2rg import RR2RG
from predicate_finder import predicate_finder
from parent_tracer import ParentTracer

class AliceBobConfig(RootedRelation):
    def __init__(self, initial_state):
        """
        Initialise l'état initial d'Alice et Bob.
        :param initial_state: tuple représentant l'état initial (Alice, Bob).
        """
        self.tuple_alice_bob = initial_state

    def initial(self):
        """
        Retourne l'état initial de l'automate.
        """
        return self.tuple_alice_bob

    def actions(self, config):
        """
        Retourne les actions possibles pour une configuration donnée.
        Une action change l'état d'Alice ou de Bob tout en respectant les contraintes.
        :param config: Configuration actuelle (Alice, Bob).
        :return: Ensemble des configurations accessibles.
        """
        current_alice, current_bob = config
        actions = []

        # Actions pour Alice
        if current_alice == 'i':
            actions.append(('w', current_bob))  
        elif current_alice == 'w' and current_bob == 'i': 
            actions.append(('c', current_bob))
        elif current_alice == 'c':
            actions.append(('i', current_bob))  # Alice retourne à 'i'

        # Actions pour Bob
        if current_bob == 'i':
            actions.append((current_alice, 'w')) 
        elif current_bob == 'w' and current_alice == 'i':  
            actions.append((current_alice, 'c'))
        elif current_bob == 'c':
            actions.append((current_alice, 'i'))  

        return set(actions)



    def execute(self, config, action):
        """
        Applique une action et retourne le nouvel état.
        :param config: Configuration actuelle (Alice, Bob).
        :param action: Action à appliquer (nouvel état).
        :return: Nouvelle configuration.
        """
        return action


def main():
    print("------- Alice & Bob -------")

    # Initialisation de l'automate avec AliceBobConfig
    alice_bob_rr = AliceBobConfig(initial_state=('i', 'i'))

    # Conversion en graphe raciné avec RR2RG
    alice_bob_graph = ParentTracer(RR2RG(alice_bob_rr))

    print("[+] Vérification de la propriété : (c, c) ")

    # Vérifier si un état interdit est accessible
    solution = predicate_finder(
        alice_bob_graph,
        lambda state: state == ('c', 'c')  # État interdit : Alice et Bob à 'c'
    )

    if solution:
        print("[+] La propriété (c, c) n'est pas respectée.")
        print(f"[+] État trouvé : {solution}")

        print("[+] Trace :")
        trace = alice_bob_graph.getTrace(solution)
        for state in trace:
            print(state)
    else:
        print("[-] La propriété (c, c) est respectée.")

    print("\n[+] Vérification de l'absence de deadlock...")

    # Vérifier s'il existe un état de deadlock
    deadlock_state = predicate_finder(
        alice_bob_graph,
        lambda state: len(alice_bob_rr.actions(state)) == 0  # Deadlock si aucune action n'est possible
    )

    if deadlock_state:
        print("[+] Deadlock détecté.")
        print(f"[+] État de deadlock : {deadlock_state}")

        print("[+] Trace :")
        trace = alice_bob_graph.getTrace(deadlock_state)
        for state in trace:
            print(state)
    else:
        print("[-] Aucun deadlock détecté.")

if __name__ == '__main__':
    main()