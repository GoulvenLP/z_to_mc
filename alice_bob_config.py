from piece import Piece
from soup import Soup


class AliceBobConfig:

    def __init__(self, state_alice="i", state_bob="i"):
        self.state_alice = state_alice
        self.state_bob = state_bob

        self.forbiden_state =False

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

class ReachabilityConfig:
    
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
        if (not isinstance(comparative, ReachabilityConfig)):
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


def reachability():

    def init(step, config: ReachabilityConfig):
        config.state = "i"

    def fordiden_state(step, config: ReachabilityConfig):
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
        fordiden_state,
    )

    return (
        Soup(ReachabilityConfig(), [p1, p2]),
        lambda config: config.state == "w",
    )
