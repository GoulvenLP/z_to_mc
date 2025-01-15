from rooted_relation import RootedRelation
from copy import deepcopy
from soup import Soup

class SoupSemantic(RootedRelation):

    def __init__(self, program : Soup):
        self.program = program

    def initial(self):
        return self.program.start
    
    def actions(self, config):
        return list(filter(lambda p: p.guard(config), self.program.pieces))
    

    def execute(self, configuration, piece):
        target = deepcopy(configuration)
        _ = piece.behavior(target)
        return [target]


def main():
    pass

    
if __name__ == '__main__':
    main()