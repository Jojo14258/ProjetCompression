from listDoublementChaine import ListChaineDouble
from Noeud import Noeud
from ArbreHuffman import ArbreHuffman


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

def construire_arbre_huffman(liste_freq):
    """Construit l'arbre de Huffman à partir des fréquences.
    
    Algorithme simple :
    1. Tant qu'il reste plus d'un noeud dans la liste
    2. Prendre les 2 noeuds avec les plus petites fréquences
    3. Créer un noeud parent avec ces 2 noeuds comme enfants
    4. Réinsérer le parent dans la liste
    5. Le dernier noeud est la racine de l'arbre
    
    Args:
        liste_freq (ListChaineDouble): Liste triée des noeuds par fréquence
        
    Returns:
        ArbreHuffman: L'arbre de Huffman construit
    """
    
    # Tant qu'il reste plus d'un noeud
    while liste_freq.taille > 1:
        
        # Étape 1 : Retirer le premier noeud (plus petite fréquence)
        noeud1 = liste_freq.tete
        liste_freq.tete = noeud1.suivant
        if liste_freq.tete:
            liste_freq.tete.precedent = None
        liste_freq.taille -= 1
        # Nettoyer les liens de la liste
        noeud1.suivant = None
        noeud1.precedent = None
        
        # Étape 2 : Retirer le deuxième noeud (deuxième plus petite fréquence)
        noeud2 = liste_freq.tete
        liste_freq.tete = noeud2.suivant
        if liste_freq.tete:
            liste_freq.tete.precedent = None
        liste_freq.taille -= 1
        # Nettoyer les liens de la liste
        noeud2.suivant = None
        noeud2.precedent = None
        
        # Étape 3 : Créer un noeud parent
        # La fréquence du parent = somme des fréquences des enfants
        frequence_parent = noeud1.frequence + noeud2.frequence
        
        # Le parent a une valeur None (c'est un noeud interne, pas une feuille)
        # Les enfants sont noeud1 (gauche) et noeud2 (droite)
        parent = Noeud(None, frequence_parent, gauche=noeud1, droit=noeud2)
        
        # Étape 4 : Réinsérer le parent dans la liste
        liste_freq.append_noeud(parent)
        
        # Étape 5 : Re-trier la liste pour maintenir l'ordre
        liste_freq.trier_par_frequence()
    
    # À la fin, il ne reste qu'un noeud : la racine de l'arbre
    arbre = ArbreHuffman(liste_freq.tete)
    return arbre



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
    
    # Test de construction de l'arbre de Huffman
    print("\n4. Construction de l'arbre de Huffman...")
    arbre = construire_arbre_huffman(liste_freq)
    if arbre.est_vide():
        print("   [ERREUR] L'arbre est vide!")
    else:
        print("   [OK] Arbre de Huffman construit avec succès!")
        print(f"   Racine de l'arbre: fréquence = {arbre.racine.frequence}")
    
    # Visualisation de l'arbre
    print("\n4.5. Visualisation de l'arbre:")
    arbre.afficher()
    
    # Test de génération des codes
    print("\n5. Génération des codes de Huffman...")
    codes = arbre.generer_codes()
    print("   Codes générés:")
    
    actuel_code = codes.tete
    while actuel_code:
        # actuel_code.valeur = le caractère (bytes)
        # actuel_code.frequence = le code binaire (string)
        if actuel_code.valeur and isinstance(actuel_code.valeur, bytes):
            if 32 <= actuel_code.valeur[0] <= 126:
                print(f"   '{actuel_code.valeur.decode()}' → {actuel_code.frequence}")
            else:
                print(f"   Octet {actuel_code.valeur[0]} → {actuel_code.frequence}")
        actuel_code = actuel_code.suivant
    
    print("\n=== Tous les tests terminés ===\n")
    
    # Résultat attendu pour "ABRACADABRA":
    # Fréquences: C(1), D(1), B(2), R(2), A(5)
    # 
    # Codes possibles (selon construction):
    # A: 0 (car la plus fréquente)
    # B: 110
    # R: 111
    # C: 100
    # D: 101