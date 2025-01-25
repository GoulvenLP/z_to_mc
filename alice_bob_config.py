from piece import Piece
from soup import Soup
from stutter import Stutter


class AliceBobConfig:

    def __init__(self, state_alice="i", state_bob="i"):
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
        if not isinstance(comparative, AliceBobConfig):
            return False
        return (self.state_alice == comparative.state_alice) and (
            self.state_bob == comparative.state_bob
        )

class PropertyConfig:
    
    def __init__(self):
        self.state = "i"

    def __repr__(self):
        return "state: " + str(self.state)
    
    def __hash__(self):
        return hash(self.state)
    
    def __eq__(self, comparative):
        """
            Compares an object to the current one.
            @comparative: the object to compare to the self one
            @return True if both objects are equal, else false
        """
        if (not isinstance(comparative, PropertyConfig)):
            return False;
        return (self.state == comparative.state)


def alice_and_bob_basic():

    def alice_state_c(config: AliceBobConfig):
        config.state_alice = "c"

    def alice_state_i(config: AliceBobConfig):
        config.state_alice = "i"

    def bob_state_c(config: AliceBobConfig):
        config.state_bob = "c"

    def bob_state_i(config: AliceBobConfig):
        config.state_bob = "i"

    p1 = Piece("Alice c", lambda config: config.state_alice == "i", alice_state_c)
    p2 = Piece("Alice i", lambda config: config.state_alice == "c", alice_state_i)

    p3 = Piece("Bob c", lambda config: config.state_bob == "i", bob_state_c)
    p4 = Piece("Bob i", lambda config: config.state_bob == "c", bob_state_i)

    return Soup(AliceBobConfig(), [p1, p2, p3, p4])


def alice_and_bob_deadlock():

    def alice_state_i(config: AliceBobConfig):
        config.state_alice = "i"

    def alice_state_w(config: AliceBobConfig):
        config.state_alice = "w"

    def alice_state_c(config: AliceBobConfig):
        config.state_alice = "c"

    def bob_state_i(config: AliceBobConfig):
        config.state_bob = "i"

    def bob_state_c(config: AliceBobConfig):
        config.state_bob = "c"

    def bob_state_w(config: AliceBobConfig):
        config.state_bob = "w"

    p1 = Piece("Alice w", lambda config: config.state_alice == "i", alice_state_w)
    p2 = Piece(
        "Alice c",
        lambda config: config.state_alice == "w" and config.state_bob == "i",
        alice_state_c,
    )

    p3 = Piece("Bob w", lambda config: config.state_bob == "i", bob_state_w)
    p4 = Piece(
        "Bob c",
        lambda config: config.state_bob == "w" and config.state_alice == "i",
        bob_state_c,
    )

    p5 = Piece("Alice i", lambda config: config.state_alice == "c", alice_state_i)
    p6 = Piece("Bob i", lambda config: config.state_bob == "c", bob_state_i)

    return Soup(AliceBobConfig(), [p1, p2, p3, p4, p5, p6])


def alice_and_bob_advanced():
    def alice_state_i(config: AliceBobConfig):
        config.state_alice = "i"

    def alice_state_w(config: AliceBobConfig):
        config.state_alice = "w"

    def alice_state_c(config: AliceBobConfig):
        config.state_alice = "c"

    def bob_state_i(config: AliceBobConfig):
        config.state_bob = "i"

    def bob_state_c(config: AliceBobConfig):
        config.state_bob = "c"

    def bob_state_w(config: AliceBobConfig):
        config.state_bob = "w"

    p1 = Piece("Alice w", lambda config: config.state_alice == "i", alice_state_w)
    p2 = Piece("Alice i", lambda config: config.state_alice == "c", alice_state_i)
    p3 = Piece(
        "Alice c",
        lambda config: config.state_alice == "w" and config.state_bob != "c",
        alice_state_c,
    )

    p4 = Piece("Bob w", lambda config: config.state_bob == "i", bob_state_w)
    p5 = Piece(
        "Bob i",
        lambda config: config.state_bob == "w" and config.state_alice == "w",
        bob_state_i,
    )
    p6 = Piece(
        "Bob c",
        lambda config: config.state_bob == "w" and config.state_alice != "c",
        bob_state_c,
    )
    p7 = Piece("Bob i", lambda config: config.state_bob == "c", bob_state_i)

    return Soup(AliceBobConfig(), [p1, p2, p3, p4, p5, p6, p7])




# #########################
# Properties automata     #
# #########################
def reachability():
    """
    Property: not(alice@c and bob@c)
                                            
    The automata have two state, the init state, and the final state.
    If the automata to be verified reach the config (c,c), then the property automata goes to the 'w' state.    
    """

    def init(step, config: PropertyConfig):
        config.state = "i"

    def accept_state(step, config: PropertyConfig):
        config.state = "w"
        

    p1 = Piece(
        "not(alice@c and bob@c)",
        lambda step,config: not (
            step[0].state_alice == "c" and step[0].state_alice == "c"
        ),
        init,
    )

    p2 = Piece(
        "alice@c and bob@c",
        lambda step,config: step[0].state_alice == "c" and step[0].state_bob == "c",
        accept_state,
    )

    return (
        Soup(PropertyConfig(), [p1, p2]),
        lambda config: config.state == "w",
    )

def deadlock():

    """
    Property: not(deadlock)

    """

    def init(step, config: PropertyConfig):
        config.state = "i"

    def deadlock_state(step, config: PropertyConfig):
        print("Deadlock state")
        config.state = "w"

    p1 = Piece(
        "not(deadlock)",
        lambda step,config: len(step[0].state_alice) != 0 or len(step[0].state_bob) != 0,
        init,
    )

    p2 = Piece(
        "deadlock",
        lambda step,config: isinstance(step[1],Stutter),
        deadlock_state,
    )

    return (
        Soup(PropertyConfig(), [p1, p2]),
        lambda config: config.state == "w",
    )

def vivacity():
    """
    Property: alice@c or bob@c
    """

    def init(step, config: PropertyConfig):
        config.state = "x"

    def accept_state(step, config: PropertyConfig):
        config.state = "y"

    p1 = Piece(
        "x---q--->x",
        lambda step,config: config.state == "x" and step[0].state_alice == "c" or step[0].state_bob == "c",
        init,
    )

    p2 = Piece(
        "x---!q--->x",
        lambda step,config: config.state == "x" and not(step[0].state_alice == "c" or step[0].state_bob == "c"),
        init,
    )

    p3 = Piece(
        "x---!q--->y",
        lambda step,config: config.state == "x" and not(step[0].state_alice == "c" or step[0].state_bob == "c"),
        accept_state,
    )

    p4 = Piece(
        "y---!q--->y",
        lambda step,config: config.state == "y" and not(step[0].state_alice == "c" or step[0].state_bob == "c"),
        accept_state,
    )

    return (
        Soup(PropertyConfig(), [p1, p2, p3, p4]),
        lambda config: config.state == "y",
    )


