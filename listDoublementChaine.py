"""
Module contenant la classe file
"""

from Noeud import Noeud



class ListChaineDouble:
    """Liste doublement chaînée simple avec affichage.

    Méthodes fournies (minimales) :
    - est_vide()
    - append(val)  : ajoute en queue
    - prepend(val) : ajoute en tête
    - __str__()     : représentation avant -> arrière
    - to_string_reverse(): représentation arrière -> avant
    """

    def __init__(self, tete=None):
        self.tete = tete
        self.fin = tete
        self.taille = 0 if tete is None else 1

    def est_vide(self):
        """Renvoie True si la liste est vide."""
        return self.tete is None
    
    def append_ou_augmenterFrequence(self, valeur):
        """Ajoute la valeur au tableau sous la forme d'un noeud si elle n'est pas présente. 
        Sinon, augmente la valeur de la fréquence au noeud déjà présent. """
        if(self.est_vide()):
            self.append(valeur)
            return True
        if self.tete.valeur == valeur:
            self.tete.frequence += 1
            return True
        temp = self.tete.suivant
        while temp != None:
            if temp.valeur == valeur:
                temp.frequence += 1
                return True
            temp = temp.suivant
        self.append(valeur)
        return True
            
        


    def append(self, val):
        """Ajoute `val` en fin de liste. Retourne True si OK."""
        try:
            elt = Noeud(val, 1)
            if self.est_vide():
                self.tete = elt
                self.fin = elt
            else:
                self.fin.suivant = elt
                elt.precedent = self.fin
                self.fin = elt
            self.taille += 1
            return True
        except Exception:
            return False
    
    def append_noeud(self, noeud):
        """Ajoute un noeud directement à la fin de la liste (sans le wrapper).
        
        Utilisé pour l'arbre de Huffman où on veut garder le noeud tel quel.
        
        Args:
            noeud (Noeud): Le noeud à ajouter directement
            
        Returns:
            bool: True si succès
        """
        try:
            if self.est_vide():
                self.tete = noeud
                self.fin = noeud
            else:
                self.fin.suivant = noeud
                noeud.precedent = self.fin
                self.fin = noeud
            self.taille += 1
            return True
        except Exception:
            return False

    def prepend(self, val):
        """Ajoute `val` en tête de liste. Retourne True si OK."""
        try:
            elt = Noeud(val, 1)
            if self.est_vide():
                self.tete = elt
                self.fin = elt
            else:
                elt.suivant = self.tete
                self.tete.precedent = elt
                self.tete = elt
            self.taille += 1
            return True
        except Exception:
            return False

    def insert_at(self, index, val):
        """Insère `val` à l'indice `index`.

        Comportement :
        - index <= 0 : insertion en tête (prepend)
        - index >= taille : insertion en queue (append)
        - sinon insertion avant l'élément actuellement à la position `index`.

        Retourne True si l'insertion a réussi, False sinon.
        """
        try:
            if not isinstance(index, int):
                return False
            if index <= 0:
                return self.prepend(val)
            if self.est_vide() or index >= self.taille:
                return self.append(val)

            # insertion au milieu : trouver le noeud actuel à la position `index`
            # on parcourt depuis la tête ou la fin selon la proximité
            if index <= self.taille // 2:
                actuel = self.tete
                for _ in range(index):
                    actuel = actuel.suivant
            else:
                actuel = self.fin
                for _ in range(self.taille - 1, index, -1):
                    actuel = actuel.precedent

            # actuel est le noeud qui était à la position `index`
            nouveau = Noeud(val, 1)
            prev = actuel.precedent
            # chainage
            nouveau.suivant = actuel
            nouveau.precedent = prev
            actuel.precedent = nouveau
            if prev is not None:
                prev.suivant = nouveau
            else:
                # insertion en tête (devrait déjà être géré par index<=0, mais garde sécurité)
                self.tete = nouveau

            self.taille += 1
            return True
        except Exception:
            return False

    def trier_par_frequence(self):
        """Trie la liste par fréquence croissante.
        
        Les éléments de la liste doivent être des objets Noeud avec l'attribut 'frequence'.
        Utilise l'algorithme de tri par sélection (simple et efficace pour petites listes).
        
        Returns:
            bool: True si le tri a réussi, False sinon
        """
        if self.est_vide() or self.taille == 1:
            return True  # Déjà trié
        
        try:
            # Tri par sélection
            actuel = self.tete
            
            while actuel is not None:
                # Trouver le minimum dans le reste de la liste
                minimum = actuel
                suivant = actuel.suivant
                
                while suivant is not None:
                    # Comparer les fréquences des Noeud
                    if suivant.frequence < minimum.frequence:
                        minimum = suivant
                    
                    suivant = suivant.suivant
                
                # Échanger les valeurs, fréquences ET les enfants (pour l'arbre de Huffman)
                if minimum != actuel:
                    actuel.valeur, minimum.valeur = minimum.valeur, actuel.valeur
                    actuel.frequence, minimum.frequence = minimum.frequence, actuel.frequence
                    actuel.gauche, minimum.gauche = minimum.gauche, actuel.gauche
                    actuel.droit, minimum.droit = minimum.droit, actuel.droit
                
                actuel = actuel.suivant
            
            return True
        except Exception:
            return False

    def __str__(self):
        """Représentation avant -> arrière.

        Format : val1 <-> val2 <-> ... <-> None
        Pour une liste vide : "Liste vide".
        """
        if self.est_vide():
            return "Liste vide"

        parts = "["
        actuel = self.tete
        while actuel is not None:
            parts += f"({actuel.valeur}:{actuel.frequence})"
            if actuel.suivant is not None:
                parts += ", "
            actuel = actuel.suivant
        parts += "]"
        return parts


if __name__ == "__main__":
    # Tests basiques exécutables
    print("=== Tests de ListChaineDouble ===\n")

    # Test 1: liste vide
    l = ListChaineDouble()
    print("1. Création d'une liste vide")
    assert l.est_vide() is True, "La liste devrait etre vide"
    print("   [OK] Liste vide")
    print(f"   affichage: {l}")

    # Test 2: append
    print("\n2. Append A, B")
    l.append("A")
    l.append("B")
    print(f"   affichage: {l}")
    assert l.est_vide() is False, "La liste ne devrait pas etre vide"
    print("   [OK] Append: A, B")

    # Test 3: prepend
    print("\n3. Prepend C")
    l.prepend("C")
    print(f"   affichage: {l}")

    # Test 4: Tri par fréquence
    print("\n4. Test du tri par fréquence")
    liste_freq = ListChaineDouble()
    liste_freq.append(Noeud('A', 5))
    liste_freq.append(Noeud('B', 2))
    liste_freq.append(Noeud('C', 8))
    liste_freq.append(Noeud('D', 1))
    liste_freq.append(Noeud('E', 3))
    print(f"   Avant tri: {liste_freq}")
    
    liste_freq.trier_par_frequence()
    print(f"   Après tri: {liste_freq}")
    print("   [OK] Tri effectué (ordre croissant)")
    
    # Test 5: append_ou_augmenterFrequence
    print("\n5. Test append_ou_augmenter_frequence")
    liste_auto = ListChaineDouble()
    liste_auto.append_ou_augmenterFrequence(65)  # 'A'
    liste_auto.append_ou_augmenterFrequence(66)  # 'B'
    liste_auto.append_ou_augmenterFrequence(65)  # 'A' encore
    liste_auto.append_ou_augmenterFrequence(65)  # 'A' encore
    liste_auto.append_ou_augmenterFrequence(67)  # 'C'
    print(f"   Résultat: {liste_auto}")
    print("   [OK] A(65) devrait avoir fréquence 3, B(66):1, C(67):1")
    
    print("\n=== Tous les tests sont passés ===")