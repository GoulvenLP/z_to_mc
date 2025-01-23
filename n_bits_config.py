from soup import Soup
from piece import Piece


class NBitsConfig:
    def __init__(self):
        # valeur initial des bits (1101)
        self.bits = 1101
        self.pc = 0  # Ajout d'un compteur pour suivre les étapes (utilisé dans nbits_3even)

    def __hash__(self):
        return hash(self.bits)

    def __repr__(self):
        return f"bits: {self.bits}"

    def __eq__(self, other):
        """
        Vérifie l'équivalence entre deux objets, basée sur la valeur de 'bits'.
        """
        if not isinstance(other, NBitsConfig):
            return False
        return other.bits == self.bits

"""     def create_n_bits_soup(self, n):
        soup = Soup(NBitsConfig(), [])
        def flip(x):  # Fonction qui crée un comportement pour chaque bit
            def behaviour(c):
                c.bits = c.bits ^ (1 << x)  # Inverse le bit `x` de `c.bits`
            return behaviour

        for i in range(n):
            soup.add_piece(Piece(f"flip({i})", lambda c: True, flip(i)))
        return soup """




# ############################################################################################################
# NOT WORKING, AND DONT KNOW WHY
# THE BEHAVIOR FUNCTION IS NOT RECORGANIZED IN THE PIECE OBJECT
# ############################################################################################################
def nbit():

    def flip(config : NBitsConfig):
        config.bits = config.bits ^ 1
    
    p1 = Piece("flip", lambda config : True, flip)
    soup = Soup(NBitsConfig(), [p1])
    return soup



def nbits_3even():
    """
    Automate de propriété qui vérifie que le bit actuel est pair.
    """

    # Pièce qui vérifie si le nombre est pair
    def p1a(step, config : NBitsConfig):
        source, action, target = step
        config.pc += 1  # Incrémenter le compteur si la transition est validée

    p1 = Piece(
        "even",
        lambda step: step[0].bits % 2 == 0,  # Vérifie si `bits` est pair
        p1a
    )

    # Pièce qui vérifie si le nombre n'est pas pair
    def p2a(step, config : NBitsConfig):
        source, action, target = step

    p2 = Piece(
        "not even",
        lambda step: step[0].bits % 2 != 0,  # Vérifie si `bits` est impair
        p2a
    )

    soup = Soup(NBitsConfig(), [p1, p2])  # création de la soupe oh miam 

    return soup, lambda config: config.pc == 3  # La propriété est satisfaite si `pc == 3`

