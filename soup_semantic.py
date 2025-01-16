from rooted_relation import RootedRelation
from copy import deepcopy
from soup import Soup
from program_1_config import program1
from rr2rg import RR2RG
from predicate_finder import predicate_finder
from parent_tracer import ParentTracer

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
    print("------- Program 1  -------")

    program = program1()
    soup_semantic = SoupSemantic(program)

    graph = ParentTracer(RR2RG(soup_semantic))

    print("[+] Recherche d'un deadlock...")

    is_deadlock = predicate_finder(graph, lambda state: len(soup_semantic.actions(state)) == 0)
    
    if is_deadlock:
        print("[+] Deadlock trouvée !")


        print("[+] Trace du deadlock:")
        trace = graph.getTrace(is_deadlock)
        for state in trace:
            print(state)
    else:
        print("Aucun deadlock trouvé.")


if __name__ == '__main__':
    main()