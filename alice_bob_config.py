from piece import Piece
from soup import Soup


class AliceBobConfig:

    def __init__(self, state_alice = 'i', state_bob = 'i'):
        self.state_alice = state_alice
        self.state_bob = state_bob

    def __repr__(self):
        return "Alice: " + str(self.state_alice) + ", Bob: " + str(self.state_bob)
    
    def __hash__(self):
        return hash((self.state_alice, self.state_bob))
    
    def __eq__(self, comparative):
        """
            Compares an object to the current one.
            @comparative: the object to compare to the self one
            @return True if both objects are equal, else false
        """
        if (not isinstance(comparative, AliceBobConfig)):
            return False;
        return (self.state_alice == comparative.state_alice) and (self.state_bob == comparative.state_bob)
    

def alice_and_bob_basic():
     
    def alice_state_c(config : AliceBobConfig):
        config.state_alice = 'c'

    def alice_state_i(config : AliceBobConfig):
        config.state_alice = 'i'

    def bob_state_c(config : AliceBobConfig):
        config.state_bob = 'c'

    def bob_state_i(config : AliceBobConfig):
        config.state_bob = 'i'

    p1 = Piece("Alice c", lambda config : config.state_alice == 'i', alice_state_c)
    p2 = Piece("Alice i", lambda config : config.state_alice == 'c', alice_state_i)
    
    p3 = Piece("Bob c", lambda config : config.state_bob == 'i', bob_state_c)
    p4 = Piece("Bob i", lambda config : config.state_bob == 'c', bob_state_i)

    return Soup(AliceBobConfig(), [p1, p2, p3, p4])


def alice_and_bob_deadlock():
     
    def alice_state_i(config : AliceBobConfig):
        config.state_alice = 'i'

    def alice_state_w(config : AliceBobConfig):
        config.state_alice = 'w'

    def alice_state_c(config : AliceBobConfig):
        config.state_alice = 'c'

    def bob_state_i(config : AliceBobConfig):
        config.state_bob = 'i'

    def bob_state_c(config : AliceBobConfig):
        config.state_bob = 'c'

    def bob_state_w(config : AliceBobConfig):
        config.state_bob = 'w'


    p1 = Piece("Alice w", lambda config : config.state_alice == 'i', alice_state_w)
    p2 = Piece("Alice c", lambda config : config.state_alice == 'w' and config.state_bob == 'i', alice_state_c)

    p3 = Piece("Bob w", lambda config : config.state_bob == 'i', bob_state_w)
    p4 = Piece("Bob c", lambda config : config.state_bob == 'w' and config.state_alice == 'i', bob_state_c)

    p5 = Piece("Alice i", lambda config : config.state_alice == 'c', alice_state_i)
    p6 = Piece("Bob i", lambda config : config.state_bob == 'c', bob_state_i)

    return Soup(AliceBobConfig(), [p1, p2, p3, p4, p5, p6])


def alice_and_bob_advanced():
    def alice_state_i(config : AliceBobConfig):
        config.state_alice = 'i'

    def alice_state_w(config : AliceBobConfig):
        config.state_alice = 'w'

    def alice_state_c(config : AliceBobConfig):
        config.state_alice = 'c'

    def bob_state_i(config : AliceBobConfig):
        config.state_bob = 'i'

    def bob_state_c(config : AliceBobConfig):
        config.state_bob = 'c'

    def bob_state_w(config : AliceBobConfig):
        config.state_bob = 'w'

    p1 = Piece("Alice w", lambda config : config.state_alice == 'i', alice_state_w)
    p2 = Piece("Alice c", lambda config : config.state_alice == 'w', alice_state_c)

    p3 = Piece("Bob w", lambda config : config.state_bob == 'i', bob_state_w)
    p4 = Piece("Bob i", lambda config : config.state_bob == 'w' and config.state_alice == 'c', bob_state_i)
    p5 = Piece("Bob c", lambda config : config.state_bob == 'w' and config.state_alice != 'c', bob_state_c)

    p6 = Piece("Alice i", lambda config : config.state_alice == 'c', alice_state_i)
    p7 = Piece("Bob i", lambda config : config.state_bob == 'c', bob_state_i)

    return Soup(AliceBobConfig(), [p1, p2, p3, p4, p5, p6, p7])