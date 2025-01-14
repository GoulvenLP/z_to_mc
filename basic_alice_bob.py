from enum_config_alice_bob import EConfig


class AliceBobBasic:

    def __init__(self, state_alice, state_bob):
        self.tuple_alice_bob = (state_alice, state_bob)
        self.strategy = EConfig.BASIC
    

    def action(self, config):
        """
            returns the possible moves applied to a submitted configuration
            a configuration is made of a tuple (alice, bob)
        """
        nextAlice = None
        nextBob = None
        # possible moves on alice
        if (self.tuple_alice_bob[0] == 'i'):
            nextAlice = 'c'
        elif (self.tuple_alice_bob[0] == 'c'):
            nextAlice = 'i'
       
        
        #possible moves on bob
        if (self.tuple_alice_bob[1] == 'i'):
            nextBob = 'c'
        if (self.tuple_alice_bob[1] == 'c'):
            nextBob = 'i'
        
        return (nextAlice, nextBob)
    


    def execute(self, config):
        move = self.action(config)
        self.tuple_alice_bob = move


    def getTuple(self):
        return self.tuple_alice_bob
    
    def getStateAlice(self):
        return self.tuple_alice_bob[0]
    
    def getStateBob(self):
        return self.tuple_alice_bob[1]

    def __str__(self):
        return f"Alice: {self.getStateAlice()}, Bob: {self.getStateBob()}"



    def main(self, alice, bob):
        self.__init__(alice, bob)
        move = automate.action(automate.getTuple())
        automate.execute(move)
        print(automate)
        

def predicateFinder(graph, predicate):
    pass

if (__name__ == '__main__'):
    main()