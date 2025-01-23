from rooted_relation import RootedRelation
from copy import deepcopy
from soup import Soup
from program_1_config import program1, program1_parity_check
from rr2rg import RR2RG
from predicate_finder import predicate_finder
from parent_tracer import ParentTracer
from alice_bob_config import alice_and_bob_basic, alice_and_bob_deadlock, alice_and_bob_advanced, AliceBobConfig
from step_semantics_intersection import StepSemanticsIntersection
from n_bits_config import nbits_3even, nbit
from soup_dependent_semantic import SoupDependantSemantics

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
        return target 



def main():
    i = 0
    programs = [program1(), alice_and_bob_basic(), alice_and_bob_deadlock(), alice_and_bob_advanced()]
    for program in programs:
        if (i == 0):
            print("\n------- Program 1  -------")
        elif (i == 1):
            print("\n------- Program Alice and Bob basic  -------")
        elif (i == 2):
            print("\n------- Alice and Bob deadlock  -------")
        elif (i == 3):
            print("\n------- Alice and Bob Advanced -------")
        i += 1

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




def main2():
    """     systeme = nbit()
    proprietes, accept = nbits_3even()
    ss = SoupSemantic(systeme)
    sp = SoupDependantSemantics(proprietes)
    s_inter = StepSemanticsIntersection(ss, sp)
    rr2rg = RR2RG(s_inter)
    parent_tracer = ParentTracer(rr2rg)
    solution = predicate_finder(parent_tracer, lambda config: accept(config[1])) """

    systeme = program1()
    proprietes, accept = program1_parity_check()
    
    ss = SoupSemantic(systeme)
    sp = SoupDependantSemantics(proprietes)
    s_inter = StepSemanticsIntersection(ss, sp)
    rr2rg = RR2RG(s_inter)
    parent_tracer = ParentTracer(rr2rg)
    solution = predicate_finder(parent_tracer, lambda config: accept(config[1]))



if __name__ == '__main__':
    main()