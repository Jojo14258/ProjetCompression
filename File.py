"""
Module contenant la classe file
"""



class Element:
    """Type de base pour les éléments de la pile"""

    def __init__(self, valeur_element, suivant):
        self.valeur = valeur_element
        self.suivant = suivant

class File:
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
    
    def enfiler(self, valeur):
        """
        Enfile la valeur en paramètre et renvoie true si
        l'enfilement s'est bien effectué, false sinon.
        
        Args:
            arg (valeur): int
            
        Returns:
            type: Boolean 
        """
        elt = Element(valeur, None)

        try:
            if(self.est_vide()):
                self.debut = elt
                self.fin = elt
                return elt.valeur 
                
            self.fin.suivant = elt
            self.fin = elt
            return elt.valeur 
        except:
            return False


    def defiler(self):
        """
        Defile et renvoie la valeur qui a été retiré. Renvoi false si le défilement n'a pas marché.
        
        Args:
            
        Returns:
            type: int
            type: bool 
        """
        if(not(self.est_vide())):
            val = self.debut.valeur
            self.debut = self.debut.suivant 
            return val
        return False
      
        



    def __str__(self):
        """Représentation en string de l'objet."""
        if self.est_vide():
            return "Pile vide"
        
        resultat = ""
        elementActuel = self.debut
        while elementActuel != None:
            resultat += str(elementActuel.valeur) + " -> "
            elementActuel = elementActuel.suivant
        resultat += "None"
        return resultat



# Exemple d'utilisation
if __name__ == "__main__":
    print("=== Tests de la File avec assertions ===\n")
    
    # Test 1: Créer une file vide
    print("1. Creation d'une file vide")
    file = File(None)
    assert file.est_vide() == True, "La file devrait etre vide"
    print("   [OK] File vide correctement creee")
    
    # Test 2: Enfiler des valeurs
    print("\n2. Enfilement de valeurs")
    file.enfiler("A")
    file.enfiler("B")
    file.enfiler("C")
    assert file.est_vide() == False, "La file ne devrait pas etre vide"
    print("   [OK] Enfile: A, B, C")
    print(f"   File: {file}")
    
    # Test 3: Défiler dans l'ordre FIFO
    print("\n3. Defilement (FIFO)")
    val1 = file.defiler()
    assert val1 == "A", f"Devrait defiler A, mais obtenu {val1}"
    print(f"   [OK] Defile: {val1}")
    
    val2 = file.defiler()
    assert val2 == "B", f"Devrait defiler B, mais obtenu {val2}"
    print(f"   [OK] Defile: {val2}")
    print(f"   File: {file}")
    
    # Test 4: Enfiler à nouveau
    print("\n4. Nouvel enfilement")
    file.enfiler("D")
    print("   [OK] Enfile: D")
    print(f"   File: {file}")
    
    # Test 5: Défiler tout
    print("\n5. Defilement complet")
    val3 = file.defiler()
    assert val3 == "C", f"Devrait defiler C, mais obtenu {val3}"
    print(f"   [OK] Defile: {val3}")
    
    val4 = file.defiler()
    assert val4 == "D", f"Devrait defiler D, mais obtenu {val4}"
    print(f"   [OK] Defile: {val4}")
    
    assert file.est_vide() == True, "La file devrait etre vide maintenant"
    print("   [OK] File completement videe")
    
    print("\n=== [OK] Tous les tests sont passes ===")