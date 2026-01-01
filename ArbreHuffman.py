"""
Module contenant la classe ArbreHuffman
"""

from listDoublementChaine import ListChaineDouble
from Noeud import Noeud


class ArbreHuffman:
    """Arbre de Huffman simple pour la compression.

    Arbre où chaque feuille contient un caractère avec sa fréquence.
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
            codes.append_noeud(noeud_code)
            return
        
        # Sinon, continuer à descendre dans l'arbre
        # Gauche = ajouter '0'
        self._generer_codes_recursif(noeud.gauche, code_actuel + "0", codes)
        # Droite = ajouter '1'
        self._generer_codes_recursif(noeud.droit, code_actuel + "1", codes)    
    def afficher(self):
        """Affiche l'arbre de Huffman de manière visuelle.
        
        Affiche l'arbre avec une indentation pour montrer la hiérarchie.
        Format : [freq] valeur
        """
        if self.est_vide():
            print("Arbre vide")
            return
        
        print("=== Structure de l'arbre de Huffman ===\n")
        self._afficher_recursif(self.racine, "", True)
        print()
    
    def _afficher_recursif(self, noeud, prefixe, est_dernier):
        """Fonction récursive privée pour afficher l'arbre.
        
        Args:
            noeud (Noeud): Le noeud actuel
            prefixe (str): Le préfixe d'indentation
            est_dernier (bool): Si c'est le dernier enfant
        """
        if noeud is None:
            return
        
        # Afficher le noeud actuel
        print(prefixe, end="")
        
        # Symbole de branche
        if est_dernier:
            print("└── ", end="")
            nouveau_prefixe = prefixe + "    "
        else:
            print("├── ", end="")
            nouveau_prefixe = prefixe + "│   "
        
        # Afficher la fréquence et la valeur
        if noeud.valeur is None:
            # Noeud interne (pas de valeur)
            print(f"[{noeud.frequence}] (noeud interne)")
        else:
            # Feuille (avec caractère)
            if isinstance(noeud.valeur, bytes):
                if 32 <= noeud.valeur[0] <= 126:
                    print(f"[{noeud.frequence}] '{noeud.valeur.decode()}'")
                else:
                    print(f"[{noeud.frequence}] octet {noeud.valeur[0]}")
            else:
                print(f"[{noeud.frequence}] {noeud.valeur}")
        
        # Afficher les enfants
        if noeud.gauche is not None or noeud.droit is not None:
            # Afficher le fils gauche
            if noeud.gauche is not None:
                self._afficher_recursif(noeud.gauche, nouveau_prefixe, noeud.droit is None)
            
            # Afficher le fils droit
            if noeud.droit is not None:
                self._afficher_recursif(noeud.droit, nouveau_prefixe, True)