from rooted_dependent_relation import RootedDependentRelation
from copy import deepcopy

class SoupDependantSemantics(RootedDependentRelation):

    def __init__(self, program):
        self.program = program

    def initial(self):
        return self.program.start

    def actions(self, input, config):
        return list(filter(lambda p: p.guard(input, config), self.program.pieces))

    def execute(self, piece, input, config):
        target = deepcopy(config)
        _ = piece.behavior(input, target)
        return target