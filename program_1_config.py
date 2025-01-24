from piece import Piece
from soup import Soup


class Program1Config:

    def __init__(self):
        self.pc = 1
        self.x = 0
        self.parity_count = 0

    def __repr__(self):
        return "pc: " + str(self.pc) + ", x: " + str(self.x)
    
    def __hash__(self):
        return hash((self.pc, self.x))
    
    def __eq__(self, comparative):
        """
            Compares an object to the current one.
            @comparative: the object to compare to the self one
            @return True if both objects are equal, else false
        """
        if (not isinstance(comparative, Program1Config)):
            return False;
        return (self.pc == comparative.pc) and (self.x == comparative.x)
    

def program1():
     
    def ap1(config : Program1Config):
        config.x += 2
        config.pc +=1

    p1 = Piece("p1", lambda config : config.pc == 1, ap1)

    def ap2(config : Program1Config):
        config.x += 3
        config.pc +=1

    p2 = Piece("p2", lambda config : config.pc == 2, ap2)

    return Soup(Program1Config(), [p1, p2])


def program1_parity_check():

    """
    The propriety is verified if the parity count is equal to 3
    """
    def even(step, config : Program1Config):
        config.parity_count += 1

    p1 = Piece("p1", lambda step, config: step[0].pc % 2 == 0, even)

    def odd(step, config : Program1Config):
        pass

    p2 = Piece("p2", lambda step, config: step[0].pc != 0, odd)

    return Soup(Program1Config(), [p1, p2]), lambda config: config.parity_count == 3