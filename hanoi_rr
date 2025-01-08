from rooted_relation import RootedRelation

class HanoiRR(RootedRelation):

    def __init__(self, towers, disks, init_cases: set):
        """
            Initialisation of the constructor with 
            a set of initial cases in the Hanoi game.
            init_cases: set of cases
        """
        self.towers = towers
        self.disks = disks
        self.initial_cases = init_cases

    def initial(self):
        return self.initial_cases

    def move(self, configuration, source, dest):
        """
            Verifies if a move is allowed depending on the Hanoi principles.
            A disk can move to an empty tower if the tower is empty or only if
            the disk is lighter than the destination's top disk.
            Returns a tuple (True, config) if the move is allowed, else (False, None)
        """
        if (configuration[source][-1] and not configuration[dest]) or \
            (configuration[source][-1] < configuration[dest][-1]):
            disk = configuration[source][-1]
            next_possible_config = configuration[source][-1].pop()
            next_possible_config[dest].append(disk)
            return True, next_possible_config
        return False, None



    def actions(self, configuration)-> set:
        """
            Searchs and returns all the next possible 
            configurations after one move on the 
            given configuration
            @configuration: current configuration
        """
        actions = set()
        for src_tower in configuration:
            if src_tower: # not empty
                for dest_tower in self.towers:
                    if dest_tower != src_tower:
                        allowed, next_possible_config = \
                            self.move(configuration, self.towers.index(src_tower), \
                                 self.towers.index(dest_tower))

                if (allowed):
                    actions.append(next_possible_config)
        

        return actions

    def execute(self, hanoi, action):
        """
            Executes the given action
            @action: action to execute
        """
        pass