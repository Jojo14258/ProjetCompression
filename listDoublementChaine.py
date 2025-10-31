"""
Module contenant la classe file
"""



class Element:
    """Type de base pour les éléments de la pile"""

    def __init__(self, valeur_element, suivant, precedent):
        self.valeur = valeur_element
        self.suivant = suivant
        self.precedent = precedent

class ListChaineDouble:
    """
    Description de la classe.
    
    Attributes:
        attribut1 (type): Description de l'attribut1
        attribut2 (type): Description de l'attribut2
    """
    
    # Variable de classe (partagée par toutes les instances)
    
    def __init__(self, elt):
        """
        Constructeur de la classe.
        
        Args:
            debut (obj): instance de l'objet element
        """
        self.debut = elt
        self.fin = elt 
    
    def est_vide(self):
        """
        Renvoi true si vide, false sinon
            
        Returns:
            type: boolean
        """
        return self.debut == None
    
    def append(self, val):
        """
        Ajoute la valeur en paramètre en début de list.
        Renvoi true si tout s'est bien passé, false sinon.
        
        Args:
            arg (val): int
            
        Returns:
            type: Boolean 
        """
        elt = Element(val,self.debut, None)
        if(not(self.est_vide())):
            self.debut.precedent = elt 
            self.debut = elt
            return True 
        self.debut = elt
        return True

