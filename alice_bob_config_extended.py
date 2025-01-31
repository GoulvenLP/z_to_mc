from piece import Piece
from soup import Soup

class AliceBobConfigExtended:

    def __init__(self, state_alice="i", state_bob="i"):
        self.state_alice = state_alice
        self.state_bob = state_bob
        self.global_turn = None

    def __repr__(self):
        return "Alice: " + str(self.state_alice) + ", Bob: " + str(self.state_bob + ", Turn: " + str(self.global_turn))

    def __hash__(self):
        return hash((self.state_alice, self.state_bob, self.global_turn))

    def __eq__(self, comparative):
        """
        Compares an object to the current one.
        @comparative: the object to compare to the self one
        @return True if both objects are equal, else false
        """
        if not isinstance(comparative, AliceBobConfigExtended):
            return False
        return (self.state_alice == comparative.state_alice) and (
            self.state_bob == comparative.state_bob and self.global_turn == comparative.global_turn
        )
    

def alice_and_bob_petersen():

    def alice_state_i(config: AliceBobConfigExtended):
        config.state_alice = "i"

    def alice_state_w(config: AliceBobConfigExtended):
        config.state_alice = "w"
        config.global_turn = "Bob"

    def alice_state_c(config: AliceBobConfigExtended):
        config.state_alice = "c"

    def bob_state_i(config: AliceBobConfigExtended):
        config.state_bob = "i"

    def bob_state_w(config: AliceBobConfigExtended):
        config.state_bob = "w"
        config.global_turn = "Alice"

    def bob_state_c(config: AliceBobConfigExtended):
        config.state_bob = "c"


    p1 = Piece("Alice i-->w", lambda config: config.state_alice == "i", alice_state_w)

    p2 = Piece(
        "Alice w-->c",
        lambda config: config.state_alice == "w" and (config.state_bob == "i" or config.global_turn == "Alice"),
        alice_state_c,
    )

    p3 = Piece("Alice c-->i", lambda config: config.state_alice == "c", alice_state_i)

    p4 = Piece("Bob i-->w", lambda config: config.state_bob == "i", bob_state_w)

    # the !c was not precise enough. Alice needs to be in the i state and nothing else
    p5 = Piece(
        "Bob w-->c",
        lambda config: config.state_bob == "w" and (config.state_alice == "i" or config.global_turn == "Bob"), 
        bob_state_c,
    )

    p6 = Piece("Bob c-->i", lambda config: config.state_bob == "c", bob_state_i)

    return Soup(AliceBobConfigExtended(), [p1, p2, p3, p4, p5, p6])
