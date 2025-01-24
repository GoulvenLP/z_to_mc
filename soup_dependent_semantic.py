from rooted_dependent_relation import RootedDependentRelation
from copy import deepcopy
from program_1_config import program1, program1_parity_check
from soup_semantic import SoupSemantic
from step_semantics_intersection import StepSemanticsIntersection
from rr2rg import RR2RG
from predicate_finder import predicate_finder
from parent_tracer import ParentTracer
from alice_bob_config import alice_and_bob_basic, reachability
class SoupDependantSemantics(RootedDependentRelation):

    def __init__(self, program):
        self.program = program

    def initial(self):
        return self.program.start

    def actions(self, input, config):
        def guard(piece):
            a = piece.guard(input, config)
            return a
        return list(filter(guard, self.program.pieces))

    def execute(self, piece, input, config):
        target = deepcopy(config)
        _ = piece.behavior(input, target)
        return [target]
    


def main():

    """     systeme = program1()
    proprietes, accept = program1_parity_check()
    
    ss = SoupSemantic(systeme)
    sp = SoupDependantSemantics(proprietes)
    s_inter = StepSemanticsIntersection(ss, sp)
    rr2rg = RR2RG(s_inter)
    parent_tracer = ParentTracer(rr2rg)
    solution = predicate_finder(parent_tracer, lambda config: accept(config[1]))

    print(solution) """

    system = alice_and_bob_basic()
    properties, accept = reachability()
    ss = SoupSemantic(system)
    sp = SoupDependantSemantics(properties)
    s_inter = StepSemanticsIntersection(ss, sp)
    rr2rg = RR2RG(s_inter)
    parent_tracer = ParentTracer(rr2rg)
    solution = predicate_finder(parent_tracer, lambda config: accept(config[1]))

    if(solution):
        print("The property not(alice@c and bob@c) is not verified !")

if __name__ == "__main__":
    main()