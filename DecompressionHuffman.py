from listDoublementChaine import ListChaineDouble
from Noeud import Noeud


def lire_fichier_compresse(fichier_compresse):
    """Lit et parse un fichier compressé avec Huffman.
    
    Structure du fichier :
    - Nombre de codes (1 octet)
    - Pour chaque code : [valeur][longueur][octets du code]
    - Padding (1 octet)
    - Données compressées (reste du fichier)
    
    Args:
        fichier_compresse: Chemin du fichier compressé
        
    Returns:
        tuple: (table_codes, padding, donnees_compressees)
            - table_codes: ListChaineDouble de Noeud(valeur_byte, code_bits)
            - padding: int (nombre de bits de padding)
            - donnees_compressees: ListChaineDouble d'octets
    """
    with open(fichier_compresse, 'rb') as fichier:
        # 1. Lecture le nombre de codes
        nb_codes = fichier.read(1)[0]
        
        # 2. Lecture chaque code et construire la table
        table_codes = ListChaineDouble()
        
        for _ in range(nb_codes):
            # Lecture la valeur du caractère
            valeur = fichier.read(1)[0]
            
            #lecture la longueur du code en bits
            longueur_bits = fichier.read(1)[0]
            
            # Calcul combien d'octets occupent ce code
            nb_octets = (longueur_bits + 7) // 8
            
            # Lecture les octets du code
            octets_code = fichier.read(nb_octets)
            
            # Conversion les octets en chaîne de bits
            code_bits = ""
            for octet in octets_code:
                code_bits += bin(octet)[2:].zfill(8)
            
            # on garde que les bits utiles (selon longueur_bits)
            code_bits = code_bits[:longueur_bits]
            
            # Stocker dans la table (Noeud avec valeur=byte, frequence=code)
            noeud_code = Noeud(bytes([valeur]), code_bits)
            table_codes.append_noeud(noeud_code)
        
        # 3. Lecture le padding (le nombre de zéros qu'on a ajouté à la fin)
        padding = fichier.read(1)[0]
        
        # 4. Lecture de toutes les données compressées dans une ListChaineDouble
        donnees_compressees = ListChaineDouble()
        octet = fichier.read(1)
        while octet:
            donnees_compressees.append(octet[0])
            octet = fichier.read(1)
    
    return table_codes, padding, donnees_compressees


def octets_vers_bits(donnees_compressees, padding):
    """Convertit une liste d'octets en chaîne de bits sans le padding.
    
    Args:
        donnees_compressees: ListChaineDouble d'octets
        padding: int (nombre de bits de padding à retirer)
        
    Returns:
        str: Chaîne de bits sans le padding
    """
    texte_binaire = ""
    
    # Conversion de chaque octet en 8 bits
    actuel = donnees_compressees.tete
    while actuel:
        bits = bin(actuel.valeur)[2:].zfill(8)
        texte_binaire += bits
        actuel = actuel.suivant
    
    # Nous retirons le padding à la fin
    if padding > 0:
        texte_binaire = texte_binaire[:-padding]
    
    return texte_binaire


def decoder(table_codes, bits):
    """Décode une chaîne de bits en utilisant la table des codes de Huffman.
    
    Args:
        table_codes: ListChaineDouble de Noeud(valeur_byte, code_bits)
        bits: str (chaîne de bits à décoder)
        
    Returns:
        ListChaineDouble: Liste d'octets décodés
    """
    resultat = ListChaineDouble()
    code_actuel = ""
    
    # Parcours de chaque bit
    for bit in bits:
        code_actuel += bit
        
        # Recherche si code_actuel correspond à un code dans la table
        actuel = table_codes.tete
        trouve = False
        
        while actuel:
            if actuel.frequence == code_actuel:
                # Code trouvé ! Ajouter le caractère au résultat
                resultat.append(actuel.valeur[0])
                code_actuel = ""
                trouve = True
                break
            actuel = actuel.suivant
    
    return resultat


def decompresser_fichier(fichier_compresse, fichier_sortie):
    """Décompresse un fichier compressé avec Huffman.
    
    Args:
        fichier_compresse: Chemin du fichier compressé
        fichier_sortie: Chemin du fichier de sortie décompressé
    """
    # 1. Lecture le fichier compressé
    table_codes, padding, donnees_compressees = lire_fichier_compresse(fichier_compresse)
    
    # 2. Conversion les octets en bits (sans le padding)
    bits = octets_vers_bits(donnees_compressees, padding)
    
    # 3. Décodage des bits pour obtenir les octets originaux
    octets_originaux = decoder(table_codes, bits)
    
    # 4. Ecriture dans le fichier de sortie
    with open(fichier_sortie, 'wb') as fichier:
        actuel = octets_originaux.tete
        while actuel:
            fichier.write(bytes([actuel.valeur]))
            actuel = actuel.suivant


if __name__ == "__main__":
    print("=== Test de décompression Huffman ===\n")
    
    # Test complet : décompression
    fichier_compresse = "test.compressed"
    fichier_decompresse = "test_decompresse.txt"
    
    print("Décompression en cours...")
    decompresser_fichier(fichier_compresse, fichier_decompresse)
    print(f"Fichier décompressé: {fichier_decompresse}\n")
    
    # Vérification du contenu
    with open(fichier_decompresse, 'r') as f:
        contenu = f.read()
        print(f"Contenu décompressé: {contenu}")
    
    # Comparaison avec l'original
    try:
        with open("test.txt", 'r') as f:
            original = f.read()
        
        if contenu == original:
            print("\n✓ SUCCÈS ! Le fichier décompressé est identique à l'original")
        else:
            print("\n✗ ERREUR : Le fichier décompressé diffère de l'original")
            print(f"Original: {original}")
            print(f"Décompressé: {contenu}")
    except FileNotFoundError:
        print("\nFichier original non trouvé pour comparaison")
