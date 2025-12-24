class Noeud:
    """Noeud utilisé à la fois pour la liste chaînée et l'arbre de Huffman."""

    def __init__(self, valeur, frequence, gauche=None, droit=None, suivant=None, precedent=None):
        self.valeur = valeur
        self.frequence = frequence
        # Pour l'arbre de Huffman
        self.gauche = gauche
        self.droit = droit
        # Pour la liste doublement chaînée
        self.suivant = suivant
        self.precedent = precedent