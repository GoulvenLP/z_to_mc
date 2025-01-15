from piece import Piece
from soup import Soup


class Program1Config:

    def __init__(self):
        self.pc = 1
        self.x = 0

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
        if (isinstance(comparative, Program1Config) and \
            ((self.pc == comparative.pc) and (self.x == comparative.x))):
                return True
        return False
    

def program1():
     
    def ap1(config : Program1Config):
        config.x += 2
        config.pc +=1

    p1 = Piece("p1", lambda config : config.pc == 1, ap1)

    def ap1(config : Program1Config):
        config.x += 3
        config.pc +=1

    p2 = Piece("p2", lambda config : config.pc == 2, ap1)

    return Soup(Program1Config(), [p1, p2])
