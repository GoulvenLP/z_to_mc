from rooted_relation import RootedRelation
from rr2rg import RR2RG
from predicate_finder import predicate_finder

class AliceBobBasic(RootedRelation):

    def __init__(self, alice, bob):
        """
            initialisation. States can be 'i' or 'c'
            @alice: initial state of alice
            @bobo: initial state of bob
        """
        self.tuple_alice_bob = [(alice, bob)]  # une liste car l'architecture permet plusieurs états initiaux
    
    def initial(self):
        """
            Initial state of the automate
        """
        return self.tuple_alice_bob


    def actions(self, config):
        """
            returns the possible moves applied to a submitted configuration
            a configuration is made of a tuple (alice, bob), alice and bob 
            being 2 different possible states: 'i' or 'c'
        """
        actions = [] # all possible moves
        next_alice = None
        next_bob = None
        # possible moves on alice
        if (config[0] == 'i'):
            next_alice = 'c'
        elif (config[0] == 'c'):
            next_alice = 'i'
        actions.append((next_alice, config[1])) # config[1] = current bob
        
        #possible moves on bob
        if (config[1] == 'i'):
            next_bob = 'c'
        elif (config[1] == 'c'):
            next_bob = 'i'
        actions.append((config[0], next_bob)) #config[0] = current alice
        
        return actions
    


    def execute(self, config, action):
        """
            executes the move 'action' on config
            @config: config where to apply the action
            @action: action to apply
        """
        return [action]


    def getTuple(self):
        """
            getter
        """
        return self.tuple_alice_bob
    

    def getStateAlice(self):
        """
            getter on alice's state
        """
        return self.tuple_alice_bob[0]
    

    def getStateBob(self):
        """
            getter on bob's state
        """
        return self.tuple_alice_bob[1]

    def __str__(self):
        """
            some pretty method to display one state
        """
        return f"Alice: {self.getStateAlice()}, Bob: {self.getStateBob()}"



def main():
    print("------- Alice & Bob -------")

    # Initialisation de l'automate avec AliceBobConfig
    alice_bob_rr = AliceBobBasic(alice='i', bob='i')

    # Conversion en graphe raciné avec RR2RG
    alice_bob_graph = RR2RG(alice_bob_rr)

    print("[+] Vérification propriété (c, c) interdite...")

    # Utilisation de predicate_finder pour trouver une solution
    solution_interdite = predicate_finder(
        alice_bob_graph, 
        lambda state: state == ('c', 'c')  # État interdit : Alice et Bob à 'c' simultanément
    )

    if solution_interdite:
        print("[+] Un état interdit a été trouvé !")
        print(f"[+] État trouvé : {solution_interdite}")
    else:
        print("[-] Aucun état interdit trouvé.")

    print("[+] Vérification de l'existence de deadlock...")
    
    # Utilisation de predicate_finder pour trouver un deadlock
    deadlock = predicate_finder(
        alice_bob_graph, 
        lambda state: alice_bob_rr.actions(state) == []  # Pas de prochain état car deadlock
    )
    if deadlock:
        print("[+] Un deadlock a été trouvé !")
        print(f"[+] deadlock identifié : {deadlock}")
    else:
        print("[-] Aucun deadlock trouvé.")
        


if (__name__ == '__main__'):
    main()