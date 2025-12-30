"""
Module contenant la classe ArbreHuffman
"""

from listDoublementChaine import ListChaineDouble
from Noeud import Noeud


class ArbreHuffman:
    """Arbre de Huffman simple pour la compression.
    
    L'arbre de Huffman n'est PAS un arbre binaire de recherche.
    C'est un arbre où chaque feuille contient un caractère avec sa fréquence.
    """
    
    def __init__(self, racine=None):
        """Crée un arbre de Huffman.
        
        Args:
            racine (Noeud): La racine de l'arbre (optionnel)
        """
        self.racine = racine
    
    def est_vide(self):
        """Vérifie si l'arbre est vide.
        
        Returns:
            bool: True si l'arbre est vide, False sinon
        """
        return self.racine is None
    
    def generer_codes(self):
        """Génère les codes binaires pour chaque caractère.
        
        Parcourt l'arbre et crée les codes :
        - Aller à gauche = ajouter '0'
        - Aller à droite = ajouter '1'
        
        Returns:
            ListChaineDouble: Liste de Noeud(caractère, code_binaire)
        """
        codes = ListChaineDouble()
        
        if not self.est_vide():
            self._generer_codes_recursif(self.racine, "", codes)
        
        return codes
    
    def _generer_codes_recursif(self, noeud, code_actuel, codes):
        """Fonction récursive privée pour générer les codes.
        
        Args:
            noeud (Noeud): Le noeud actuel
            code_actuel (str): Le code en cours de construction
            codes (ListChaineDouble): La liste pour stocker les codes
        """
        # Si le noeud n'existe pas, on s'arrête
        if noeud is None:
            return
        
        # Si c'est une feuille (pas d'enfants), on a trouvé un caractère
        if noeud.gauche is None and noeud.droit is None:
            # Créer un noeud pour stocker : (caractère, code)
            noeud_code = Noeud(noeud.valeur, code_actuel)
            codes.append(noeud_code)
            return
        
        # Sinon, continuer à descendre dans l'arbre
        # Gauche = ajouter '0'
        self._generer_codes_recursif(noeud.gauche, code_actuel + "0", codes)
        # Droite = ajouter '1'
        self._generer_codes_recursif(noeud.droit, code_actuel + "1", codes)
