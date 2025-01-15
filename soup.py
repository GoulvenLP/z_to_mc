

class Soup:

    def __init__(self, start, pieces):
        """
            initial state
            @start: starting point
            @pieces: Piece object(s)
        """
        self.start = start
        self.pieces = pieces

    def add_piece(self, piece):
        """
            adds a piece to the pieces
            @piece: the piece to add
        """
        self.pieces.append(piece)

    def add_pieces(self, more_pieces):
        """
            adds pieces to the pieces
            @more_pieces: the pieces to add
        """
        self.pieces.extend(more_pieces)

    
        