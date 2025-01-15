
class Program1Config:

    def __init__(self):
        self.pc = 1
        self.x = 0

    def __hash__(self):
        return hash(tuple(self.pc, self.x))
    

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
    

