from functools import reduce
from rooted_graph import RootedGraph
from rooted_relation import RootedRelation

class RR2RG(RootedGraph):
    def __init__(self, op: RootedRelation):
        self.op = op

    def roots(self):
        return self.op.initial()

    def neighbors(self, c):
        """
        Génère les voisins d'un état donné en appliquant les actions possibles.
        :param c: État actuel (instance de  ou équivalent).
        :return: Liste des états voisins.
        """
        # Actions possibles à partir de l'état actuel
        actions = self.op.actions(c)
        # Exécuter chaque action pour obtenir les états voisins
        neighbors = [self.op.execute(c, action) for action in actions]
        def mylambda(x, xs):
            xs.extend(x)
            return xs

        neighbors = reduce(mylambda, neighbors, [])
        return neighbors


