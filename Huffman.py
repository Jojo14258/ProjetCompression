from listDoublementChaine import ListChaineDouble
from Noeud import Noeud

def Analyser_frequence_texte(file):
    listeDoublementChainee = ListChaineDouble()
    with open(file, 'rb') as fichier:
        # Lecture octet par octet
        octet = fichier.read(1)  # Lit 1 octet
        while octet:
          
            
            listeDoublementChainee.append_ou_augmenterFrequence(octet)
            octet = fichier.read(1)
    
    listeDoublementChainee.trier_par_frequence()
    return listeDoublementChainee


if __name__ == "__main__":
    print("=== Test de l'analyseur de fréquences ===\n")
    
    # Créer un fichier de test
    print("1. Création d'un fichier de test...")
    with open("test.txt", "w") as f:
        f.write("ABRACADABRA")
    print("   Fichier créé: 'test.txt' contenant 'ABRACADABRA'\n")
    
    # Analyser les fréquences
    print("2. Analyse des fréquences...")
    liste_freq = Analyser_frequence_texte("test.txt")
    print(f"   Liste des fréquences: {liste_freq}\n")
    
    # Afficher les détails
    print("3. Détails des fréquences:")
    actuel = liste_freq.tete
    while actuel:
        # Afficher le caractère si imprimable
        if 32 <= actuel.valeur[0] <= 126:  # Si c'est imprimable
            print(f"   '{actuel.valeur.decode()}' (octet {actuel.valeur[0]}): {actuel.frequence} fois")
        else:
            print(f"   Octet {actuel.valeur}: {actuel.frequence} fois")
        actuel = actuel.suivant
    
    print("\n=== Test terminé ===\n")
    
    # Résultat attendu pour "ABRACADABRA":
    # A: 5 fois
    # B: 2 fois  
    # R: 2 fois
    # C: 1 fois
    # D: 1 fois
    # Ordre après tri: C(1), D(1), B(2), R(2), A(5)