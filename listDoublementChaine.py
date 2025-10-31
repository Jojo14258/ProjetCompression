"""
Module contenant la classe file
"""



class Element:
    """Noeud pour liste doublement chaînée."""

    def __init__(self, valeur_element, suivant=None, precedent=None):
        self.valeur = valeur_element
        self.suivant = suivant
        self.precedent = precedent

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

    def append(self, val):
        """Ajoute `val` en fin de liste. Retourne True si OK."""
        try:
            elt = Element(val)
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

    def prepend(self, val):
        """Ajoute `val` en tête de liste. Retourne True si OK."""
        try:
            elt = Element(val)
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
            nouveau = Element(val)
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
            parts += (str(actuel.valeur))
            if(actuel.suivant != None):
                parts += ","
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
    assert l.est_vide() is False, "La liste ne devrait pas etre vide"
    print("   [OK] Append: A, B")
    print(f"   affichage: {l}")

    # Test 3: prepend
    print("\n3. Prepend C")
    l.prepend("C")
    print(f"   affichage: {l}")

    print("\n=== Tous les tests integrés ont été exécutés ===")

