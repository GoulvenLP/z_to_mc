from soup import Soup
from piece import Piece


class NBitsConfig:

    def __init__(self):
        self.bits = 0


    def __hash__(self):
        return hash(self.bits)
    

    def __eq__(self, object):
        """
            Verifies the equivalence between two objects, based on
            the value of the 'bits' variable
        """
        if not isinstance(object, NBitsConfig):
            return False
        return object.bits == self.bits
    

    def create_n_bits_soup(self, n):
        soup = Soup(NBitsConfig())
        def flip(x): # function that creates another function!
            def behaviour(c):
                c.bits = c.bits^(1 << x)
            return behaviour
        for i in range(n):
            soup.add(Piece(f"flip({i})"), lambda c: True, flip(i))
        return soup



# TODO VERIFY IF THIS WORKS... #gros chantier
def nbits_3even():
    def p1a(input, config):
        source, action, target = i
        config.pc += 1

    p1 = Piece("even": lambda step: 
               source, action, target = step
               return (source % 2 == 0, p1a)    #input = (source, action, target)
    )


    def p2a(step, config):
        source, action, target = step

    p2 = Piece("Not even", lambda config:
               source, action, target = step
               return (source % 2 != 0, p2a)
               )
    soup = Soup(configP1, [p1, P2])       #configP1: class that contains
    return (soup, lambda config: config.pc == 3)