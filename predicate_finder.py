from collections import deque
from rooted_graph import RootedGraph


def predicate_finder(graph: RootedGraph, predicate):
    """
    Recherche en largeur pour résoudre le problème des tours de Hanoï.
    :param graph: Le graphe représentant le jeu.
    :param predicate: La condition pour trouver l'état final.
    :return: L'état final trouvé.
    """
    queue = deque([(state) for state in graph.roots()])

    
    visited = set()

    while queue:
        current_state = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)
        # Vérifie si on a atteint l'état cible
        if predicate(current_state):
            return current_state
        # Explore les états suivants
        for next_state in graph.neighbors(current_state):
            queue.append(next_state)
    return None  # Aucun chemin trouvé