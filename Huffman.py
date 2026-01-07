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


def encoder(codes, contenuFichier, fichier_sortie):
    """Encode le contenu du fichier avec les codes de Huffman.
    
    Args:
        codes: Liste chaînée des codes de Huffman
        contenuFichier: Liste chaînée du contenu à encoder
        fichier_sortie: Nom du fichier de sortie
    """
    # TODO: À implémenter
    liste = ListChaineDouble()
    actuel_contenu = contenuFichier.tete
    texte_binaire = ""
    while actuel_contenu:
        octet_a_encoder = actuel_contenu.valeur  # Le byte à encoder

        # On cherche le code de cet octet dans la liste des codes
        actuel_code = codes.tete
        code_trouve = None
        
        while actuel_code:
          
            if actuel_code.valeur == octet_a_encoder:  
                code_trouve = actuel_code.frequence  # Le code binaire (string "0101...")
                print("code: ", code_trouve)
                break
            actuel_code = actuel_code.suivant

         # Ajouter le code trouvé
        if code_trouve:
            texte_binaire += code_trouve
        
        actuel_contenu = actuel_contenu.suivant
    
    # Afficher pour debug
    print(f"Texte encodé: {texte_binaire}")
    print(f"Longueur: {len(texte_binaire)} bits")
       
    return

def compresser_fichier(fichier_entree, fichier_sortie):
    # Analyser les fréquences du fichier
    listeFreq = Analyser_frequence_texte(fichier_entree)
    
    # Construire l'arbre de Huffman
    arbre = construire_arbre_huffman(listeFreq)
    
    # Génére les codes
    codes = arbre.generer_codes()
    
    # Lire le contenu du fichier à encoder
    contenuFichier = ListChaineDouble()
    with open(fichier_entree, 'rb') as fichier:
        octet = fichier.read(1)
        while octet:
            contenuFichier.append(octet)
            octet = fichier.read(1)
    
    # Encoder le fichier
    encoder(codes, contenuFichier, fichier_sortie)



if __name__ == "__main__":
    print("=== Test de compression Huffman ===\n")
    
    # Créer un fichier de test
    with open("test.txt", "w") as f:
        f.write("ABRACADABRA")
    print("[OK] Fichier de test créé: 'test.txt'\n")
    
    # Test de la fonction compresser_fichier
    compresser_fichier("./test.txt", "test.compressed")
    
    print("\n=== Fin du test ===")
