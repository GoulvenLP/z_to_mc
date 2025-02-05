from rooted_relation import RootedRelation
from copy import deepcopy
from soup import Soup
from rr2rg import RR2RG
from predicate_finder import predicate_finder
from parent_tracer import ParentTracer
from alice_bob_config import alice_and_bob_basic, alice_and_bob_deadlock, alice_and_bob_advanced, AliceBobConfig

class SoupSemantic(RootedRelation):

    def __init__(self, program : Soup):
        super().__init__()
        self.program = program

    def initial(self):
        return self.program.start
    
    def actions(self, config):
        elements = list(filter(lambda p: p.guard(config), self.program.pieces))
        return elements

    def execute(self, configuration, piece):
        target = deepcopy(configuration)
        _ = piece.behavior(target)
        return [target] 




def verify_properties(program, description):
    """
    Verify the properties P1 and P2 on the given program.
    """
    print(f"\n------- {description} -------")

    soup_semantic = SoupSemantic(program)
    graph = ParentTracer(RR2RG(soup_semantic))

    print("[+] Recherche d'un deadlock...")
    is_deadlock = predicate_finder(graph, lambda state: len(soup_semantic.actions(state)) == 0)

    if is_deadlock:
        print("[+] Deadlock trouvé !")
        print("[+] Trace du deadlock:")
        trace = graph.getTrace(is_deadlock)
        for state in trace:
            print(state)
    else:
        print("Aucun deadlock trouvé.")

    print("[+] Recherche du cas (c,c)...")
    forbiden_state = predicate_finder(graph, lambda state: state == AliceBobConfig('c', 'c'))

    if forbiden_state:
        print("[+] état interdit trouvé !")
        print("[+] Trace :")
        trace = graph.getTrace(forbiden_state)
        for state in trace:
            print(state)
    else:
        print("Aucun état interdit trouvé.")

def main():
    programs = [
        (alice_and_bob_basic(), "Alice and Bob basic"),
        (alice_and_bob_deadlock(), "Alice and Bob deadlock"),
        (alice_and_bob_advanced(), "Alice and Bob Advanced")
    ]

    for program, description in programs:
        verify_properties(program, description)

if __name__ == '__main__':
    main()
