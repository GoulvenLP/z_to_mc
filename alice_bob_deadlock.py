from enum_config_alice_bob import EConfig


class AliceBobConfig:

    def __init__(self, state_alice, state_bob):
        self.tuple_alice_bob = (state_alice, state_bob)
        self.strategy = EConfig.BASIC
    

    def action(config):
        """
            returns the possible moves applied to a submitted configuration
            a configuration is made of a tuple (alice, bob)
        """
        self.config.action(config)
        
        nextAlice = None
        nextBob = None
        # possible moves on alice
        if (self.tuple_alice_bob[0] == 'i'):
            nextAlice = 'w'
        if (self.tuple_alice_bob[0] == 'w' and self.tuple_alice_bob[1] == 'i' ):
            nextAlice = 'c'
        if (self.tuple_alice_bob[0] == 'c'):
            nextAlice = 'i'
        
        #possible moves on bob
        if (self.tuple_alice_bob[1] == 'i'):
            nextBob = 'w'
        if (self.tuple_alice_bob[0] == 'w' and self.tuple_alice_bob[1] == 'i' ):
            nextBob = 'c'
        if (self.tuple_alice_bob[1] == 'c'):
            nextBob = 'i'
        
        return self.config(nextAlice, nextBob)
    

    def setStrategy(mode: EConfig):
        """
            Sets the chosen strategy for the automate
        """
        self.strategy = mode
        if (mode == EConfig.BASIC):
            #TODO implement
            self.tuple_alice_bob = 
            pass
        elif (mode == EConfig.DEADLOCKS):
            #TODO implement
            pass
        elif (mode == EConfig.ADVANCED):
            #TODO implement something
            pass
    

    def execute(config):
        self.action(config)

    def getTuple():
        return self.tuple_alice_bob


if (__name__ == '__main__'):
    automate = AliceBobConfig('i', 'i')
    automate.setStrategy(EConfig.BASIC)
    automate.action(automate.getTuple())