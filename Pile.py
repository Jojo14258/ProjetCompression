"""
Module contenant des classes d'exemple.
"""

class Element:
    """Type de base pour les éléments de la pile"""

    def __init__(self, valeur_element, suivant):
        self.valeur = valeur_element
        self.suivant = suivant

class Pile:
    """
    Description de la classe.
    
    Attributes:
        attribut1 (type): Description de l'attribut1
        attribut2 (type): Description de l'attribut2
    """
    
    # Variable de classe (partagée par toutes les instances)
    variable_classe = "valeur partagée"
    
    def __init__(self, elt):
        """
        Constructeur de la classe.
        
        Args:
            elt (obj): instance de element
        """
        self.tete = elt
    


    def est_vide(self):
        """
        Renvoi true si vide, false sinon
            
        Returns:
            type: boolean
        """
        return self.tete == None
    
    def empiler(self, valeur):
        """
        Empile la valeur en paramètre et renvoie true si
        l'empilement s'est bien effectué, false sinon.
        
        Args:
            arg (valeur): int
            
        Returns:
            type: Boolean 
        """
        try:
                
            tete = Element(valeur, self.tete)
            self.tete = tete
            return True 
        except:
            return False


    def depiler(self):
        """
        Depile et renvoie la valeur qui a été retiré. Renvoi false si le dépilement n'a pas marché.
        
        Args:
            
        Returns:
            type: int
            type: bool 
        """
        if(not(self.est_vide())):
            val = self.tete.valeur
            self.tete = self.tete.suivant 
            return val
        return False 
      
        



    def __str__(self):
        """Représentation en string de l'objet."""
        if self.est_vide():
            return "Pile vide"
        
        resultat = ""
        elementActuel = self.tete 
        while elementActuel != None:
            resultat += str(elementActuel.valeur) + " -> "
            elementActuel = elementActuel.suivant
        resultat += "None"
        return resultat



# Exemple d'utilisation
if __name__ == "__main__":
    print("=== Tests de la Pile ===\n")
    
    # Test 1: Créer une pile vide
    print("1. Création d'une pile vide")
    pile = Pile(None)
    print(f"   Pile vide ? {pile.est_vide()}")
    
    # Test 2: Empiler des valeurs
    print("\n2. Empilement de valeurs")
    pile.empiler("A")
    pile.empiler("B")
    pile.empiler("C")
    print(pile)

    pile.depiler()
    pile.depiler()
    pile.depiler()
    pile.depiler()
    print("\n=== Tests terminés ===")
