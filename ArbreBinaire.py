"""
Module contenant la classe ArbreBinaire
"""


class Noeud:
    """Noeud de l'arbre binaire."""

    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit


class ArbreBinaire:
    """
    Arbre Binaire de Recherche (ABR).
    
    Implémente un arbre binaire de recherche avec les opérations de base.
    Pour chaque noeud: valeurs à gauche < valeur du noeud < valeurs à droite
    
    Attributes:
        racine (Noeud): La racine de l'arbre
    """
    
    def __init__(self, racine=None):
        """
        Constructeur de la classe.
        
        Args:
            racine (Noeud): Noeud racine initial (optionnel)
        """
        self.racine = racine
    
    def est_vide(self):
        """
        Vérifie si l'arbre est vide.
            
        Returns:
            bool: True si l'arbre est vide, False sinon
        """
        return self.racine is None
    
    def inserer(self, valeur):
        """
        Insère une valeur dans l'arbre en respectant l'ordre ABR.
        
        Args:
            valeur: La valeur à insérer
            
        Returns:
            bool: True si l'insertion a réussi, False sinon
        """
        try:
            if self.est_vide():
                self.racine = Noeud(valeur)
                return True
            
            self._inserer_recursif(self.racine, valeur)
            return True
        except Exception:
            return False
    
    def _inserer_recursif(self, noeud, valeur):
        """
        Méthode récursive privée pour insérer une valeur.
        
        Args:
            noeud (Noeud): Noeud actuel
            valeur: Valeur à insérer
        """
        if valeur < noeud.valeur:
            if noeud.gauche is None:
                noeud.gauche = Noeud(valeur)
            else:
                self._inserer_recursif(noeud.gauche, valeur)
        else:
            if noeud.droit is None:
                noeud.droit = Noeud(valeur)
            else:
                self._inserer_recursif(noeud.droit, valeur)
    
    def rechercher(self, valeur):
        """
        Recherche une valeur dans l'arbre.
        
        Args:
            valeur: La valeur à rechercher
            
        Returns:
            bool: True si la valeur est trouvée, False sinon
        """
        return self._rechercher_recursif(self.racine, valeur)
    
    def _rechercher_recursif(self, noeud, valeur):
        """
        Méthode récursive privée pour rechercher une valeur.
        
        Args:
            noeud (Noeud): Noeud actuel
            valeur: Valeur à rechercher
            
        Returns:
            bool: True si trouvé, False sinon
        """
        if noeud is None:
            return False
        
        if valeur == noeud.valeur:
            return True
        elif valeur < noeud.valeur:
            return self._rechercher_recursif(noeud.gauche, valeur)
        else:
            return self._rechercher_recursif(noeud.droit, valeur)
    
    def hauteur(self):
        """
        Calcule la hauteur de l'arbre.
        
        Returns:
            int: La hauteur de l'arbre (0 si vide)
        """
        return self._hauteur_recursif(self.racine)
    
    def _hauteur_recursif(self, noeud):
        """
        Méthode récursive privée pour calculer la hauteur.
        
        Args:
            noeud (Noeud): Noeud actuel
            
        Returns:
            int: Hauteur du sous-arbre
        """
        if noeud is None:
            return 0
        
        hauteur_gauche = self._hauteur_recursif(noeud.gauche)
        hauteur_droite = self._hauteur_recursif(noeud.droit)
        
        return 1 + max(hauteur_gauche, hauteur_droite)
    
    def nombre_noeuds(self):
        """
        Compte le nombre total de noeuds dans l'arbre.
        
        Returns:
            int: Nombre de noeuds
        """
        return self._compter_noeuds_recursif(self.racine)
    
    def _compter_noeuds_recursif(self, noeud):
        """
        Méthode récursive privée pour compter les noeuds.
        
        Args:
            noeud (Noeud): Noeud actuel
            
        Returns:
            int: Nombre de noeuds du sous-arbre
        """
        if noeud is None:
            return 0
        
        return 1 + self._compter_noeuds_recursif(noeud.gauche) + self._compter_noeuds_recursif(noeud.droit)
    
    def parcours_infixe(self):
        """
        Parcours infixe (gauche - racine - droit) de l'arbre.
        Retourne les valeurs dans l'ordre croissant pour un ABR.
        
        Returns:
            list: Liste des valeurs en ordre infixe
        """
        resultat = []
        self._parcours_infixe_recursif(self.racine, resultat)
        return resultat
    
    def _parcours_infixe_recursif(self, noeud, resultat):
        """
        Méthode récursive privée pour le parcours infixe.
        
        Args:
            noeud (Noeud): Noeud actuel
            resultat (list): Liste pour stocker les valeurs
        """
        if noeud is not None:
            self._parcours_infixe_recursif(noeud.gauche, resultat)
            resultat.append(noeud.valeur)
            self._parcours_infixe_recursif(noeud.droit, resultat)
    
    def parcours_prefixe(self):
        """
        Parcours préfixe (racine - gauche - droit) de l'arbre.
        
        Returns:
            list: Liste des valeurs en ordre préfixe
        """
        resultat = []
        self._parcours_prefixe_recursif(self.racine, resultat)
        return resultat
    
    def _parcours_prefixe_recursif(self, noeud, resultat):
        """
        Méthode récursive privée pour le parcours préfixe.
        
        Args:
            noeud (Noeud): Noeud actuel
            resultat (list): Liste pour stocker les valeurs
        """
        if noeud is not None:
            resultat.append(noeud.valeur)
            self._parcours_prefixe_recursif(noeud.gauche, resultat)
            self._parcours_prefixe_recursif(noeud.droit, resultat)
    
    def parcours_postfixe(self):
        """
        Parcours postfixe (gauche - droit - racine) de l'arbre.
        
        Returns:
            list: Liste des valeurs en ordre postfixe
        """
        resultat = []
        self._parcours_postfixe_recursif(self.racine, resultat)
        return resultat
    
    def _parcours_postfixe_recursif(self, noeud, resultat):
        """
        Méthode récursive privée pour le parcours postfixe.
        
        Args:
            noeud (Noeud): Noeud actuel
            resultat (list): Liste pour stocker les valeurs
        """
        if noeud is not None:
            self._parcours_postfixe_recursif(noeud.gauche, resultat)
            self._parcours_postfixe_recursif(noeud.droit, resultat)
            resultat.append(noeud.valeur)
    
    def minimum(self):
        """
        Trouve la valeur minimale dans l'arbre.
        
        Returns:
            La valeur minimale, ou None si l'arbre est vide
        """
        if self.est_vide():
            return None
        
        noeud = self.racine
        while noeud.gauche is not None:
            noeud = noeud.gauche
        return noeud.valeur
    
    def maximum(self):
        """
        Trouve la valeur maximale dans l'arbre.
        
        Returns:
            La valeur maximale, ou None si l'arbre est vide
        """
        if self.est_vide():
            return None
        
        noeud = self.racine
        while noeud.droit is not None:
            noeud = noeud.droit
        return noeud.valeur
    
    def __str__(self):
        """Représentation en string de l'arbre (parcours infixe)."""
        if self.est_vide():
            return "Arbre vide"
        
        valeurs = self.parcours_infixe()
        return "Arbre: [" + ", ".join(map(str, valeurs)) + "]"


