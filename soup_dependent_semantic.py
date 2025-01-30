from rooted_dependent_relation import RootedDependentRelation
from copy import deepcopy
from program_1_config import program1, program1_parity_check
from soup_semantic import SoupSemantic
from step_semantics_intersection import StepSemanticsIntersection
from rr2rg import RR2RG
from predicate_finder import predicate_finder
from parent_tracer import ParentTracer
from alice_bob_config import alice_and_bob_advanced, alice_and_bob_basic, alice_and_bob_deadlock, deadlock, reachability, vivacity
from init_rg import InitRG

class SoupDependantSemantics(RootedDependentRelation):

    def __init__(self, program):
        self.program = program

    def initial(self):
        return self.program.start

    def actions(self, input, config):
        def guard(piece):
            return piece.guard(input, config)
        possibles_actions = list(filter(guard, self.program.pieces))
        return possibles_actions

    def execute(self, piece, input, config):
        target = deepcopy(config)
        piece.behavior(input, target)
        return [target]


def verify_property(system, properties, accept, description):
    print(f"\n[+] {description}")
    ss = SoupSemantic(system)
    sp = SoupDependantSemantics(properties)
    s_inter = StepSemanticsIntersection(ss, sp)
    rr2rg = RR2RG(s_inter)
    parent_tracer = ParentTracer(rr2rg)
    solution = predicate_finder(parent_tracer, lambda config: accept(config[1]))
    if solution:
        print("-> The property is not verified!")
        print("-> The counter example is:")
        trace = parent_tracer.getTrace(solution)
        for state in trace:
            print(f" - {state}")
    else:
        print("-> The property is verified!")





def main():
    test_cases = [
        {"description": "alice&bob_basic", "system": alice_and_bob_basic()},
        {"description": "alice&bob_deadlock", "system": alice_and_bob_deadlock()},
        {"description": "alice&bob_advanced", "system": alice_and_bob_advanced()},
    ]

    # P1: not (alice@c and bob@c)
    print("--------------------------------")
    print("---- not(alice@c and bob@c) ----")
    properties, accept = reachability()
    for case in test_cases:
        verify_property(case["system"], properties, accept, case["description"])

    # P2: not (deadlock)
    print("\n--------------------------------")
    print("--------- not(deadlock) --------")
    properties, accept = deadlock()
    for case in test_cases:
        verify_property(case["system"], properties, accept, case["description"])

    # P3: alice@c or bob@c
    print("\n--------------------------------")
    print("--------- alice@c or bob@c --------")
    system = alice_and_bob_advanced()
    properties, accept = vivacity()
    ss = SoupSemantic(system)
    sp = SoupDependantSemantics(properties)
    s_inter = StepSemanticsIntersection(ss, sp)
    rr2rg = RR2RG(s_inter)
    parent_tracer = ParentTracer(rr2rg)

    def pred(config):
        if accept(config[1]): # vient de l'automate de Bushi (contient des états d'acceptation)
            inits = parent_tracer.neighbors(config)
            rooted_graphc = InitRG(parent_tracer, inits)

            assessment = predicate_finder(rooted_graphc, lambda cx: cx == config)
            return assessment
        return False
    
    solution = predicate_finder(parent_tracer, pred)
    if solution:
        print("-> The property is not verified!")
        print("-> The counter example is:")
        trace = parent_tracer.getTrace(solution)
        for state in trace:
            print(f" - {state}")
    else:
        print("-> The property is verified!")

if __name__ == "__main__":
    main()
