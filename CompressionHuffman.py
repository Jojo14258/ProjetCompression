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

def bits_vers_octets(texte_binaire):
    """Convertit une chaîne de bits en octets.
    
    Args:
        texte_binaire (str): Chaîne de '0' et '1'
        
    Returns:
        tuple: (liste d'octets, nombre de bits de padding)
    """
    longueur = len(texte_binaire)
    bits_manquants = (8 - (longueur % 8)) % 8
    
    if bits_manquants > 0:
        texte_binaire += '0' * bits_manquants
    
    octets = ListChaineDouble()
    
    for i in range(0, len(texte_binaire), 8):
        groupe = texte_binaire[i:i+8]
        valeur = int(groupe, 2)
        octets.append(valeur)
    
    return octets, bits_manquants

def encoder(codes, contenuFichier, fichier_sortie):
    """Encode le contenu avec les codes de Huffman et écrit le fichier compressé.
    
    Args:
        codes: Table de codes (ListChaineDouble)
        contenuFichier: Contenu à compresser (ListChaineDouble)
        fichier_sortie: Chemin du fichier de sortie
    """
    actuel_contenu = contenuFichier.tete
    texte_binaire = ""
    
    # Construction de la chaîne binaire complète
    while actuel_contenu:
        octet_a_encoder = actuel_contenu.valeur

        # Recherche du code correspondant
        actuel_code = codes.tete
        code_trouve = None
        
        while actuel_code:
            if actuel_code.valeur == octet_a_encoder:  
                code_trouve = actuel_code.frequence
                break
            actuel_code = actuel_code.suivant

        if code_trouve:
            texte_binaire += code_trouve
        
        actuel_contenu = actuel_contenu.suivant
    
   
    
    # Écriture du fichier : [table des codes][padding][données compressées]
    with open(fichier_sortie, 'wb') as fichier:
        # 1. Écrie le nombre de codes dans la table
        fichier.write(bytes([codes.taille]))
        
        # 2. Écrie chaque code : [valeur][longueur][code en bits]
        actuel_code = codes.tete
        while actuel_code:
            valeur = actuel_code.valeur[0]  # Le byte (premier élément du bytes)
            code_bits = actuel_code.frequence  # La chaîne de bits "010110..."
            longueur_code = len(code_bits)
            
            # Écrie la valeur (1 octet)
            fichier.write(bytes([valeur]))
            
            # Écrie la longueur du code (1 octet)
            fichier.write(bytes([longueur_code]))
            
            # Convertie le code en octets et écrire
            code_octets, _ = bits_vers_octets(code_bits)
            actuel_octet_code = code_octets.tete
            while actuel_octet_code:
                fichier.write(bytes([actuel_octet_code.valeur]))
                actuel_octet_code = actuel_octet_code.suivant
            
            actuel_code = actuel_code.suivant

        # Conversion bits -> octets
        octets_compresses, padding = bits_vers_octets(texte_binaire)        
        # 3. Écrire le padding
        fichier.write(bytes([padding]))
        
        # 4. Écrire les données compressées
        actuel_octet = octets_compresses.tete
        while actuel_octet:
            fichier.write(bytes([actuel_octet.valeur]))
            actuel_octet = actuel_octet.suivant
    
    return octets_compresses.taille

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
    
    # Création du fichier test
    contenu_test = "ABRACADABRA"
    with open("test.txt", "w") as f:
        f.write(contenu_test)
    print(f"Fichier créé: 'test.txt' ({len(contenu_test)} caractères)\n")
    
    # Compression
    compresser_fichier("./test.txt", "test.compressed")
    
    # Vérification
    import os
    taille_originale = os.path.getsize("test.txt")
    taille_compressee = os.path.getsize("test.compressed")
    ratio = (1 - taille_compressee / taille_originale) * 100
    
    print(f"\n=== Résultats ===")
    print(f"Taille originale: {taille_originale} octets")
    print(f"Taille compressée: {taille_compressee} octets")
    print(f"Taux de compression: {ratio:.1f}%")
    
    # Lecture du fichier compressé pour vérification
    with open("test.compressed", "rb") as f:
        padding = f.read(1)[0]
        donnees = f.read()
        print(f"\nPadding stocké: {padding} bits")
        print(f"Données compressées: {len(donnees)} octets")
        print(f"Premiers octets: {' '.join(f'{b:02x}' for b in donnees[:5])}...")
