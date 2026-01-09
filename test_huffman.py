"""
Test de compression/decompression Huffman avec assertions
"""

from CompressionHuffman import compresser_fichier
from DecompressionHuffman import decompresser_fichier
import os


def test_compression_decompression():
    """Test complet avec un fichier long"""
    
    print("=== Test Huffman ===\n")
    
    # Fichiers
    fichier_original = "fichier_test.txt"
    fichier_compresse = "fichier_test.compressed"
    fichier_decompresse = "fichier_test_decompresse.txt"
    
    # Contenu long pour tester
    contenu = """Le codage de Huffman est un algorithme de compression de donnees sans perte.
Il a ete developpe par David Huffman en 1952. Cette methode utilise un arbre binaire 
pour representer les caracteres les plus frequents avec moins de bits. Les caracteres 
rares utilisent plus de bits. C'est un codage a longueur variable optimal.
L'algorithme construit un arbre en fusionnant les deux noeuds de plus faible frequence.
Il remonte ensuite l'arbre pour generer les codes binaires de chaque caractere.
La compression est efficace sur les textes avec des caracteres repetitifs.
""" * 20  # Repete 20 fois pour avoir un fichier consequent
    
    print(f"Texte de test: {len(contenu)} caracteres\n")
    
    # Creation du fichier
    with open(fichier_original, "w", encoding="utf-8") as f:
        f.write(contenu)
    
    taille_originale = os.path.getsize(fichier_original)
    print(f"[1/4] Fichier original cree: {taille_originale} octets")
    
    # Compression
    compresser_fichier(fichier_original, fichier_compresse)
    taille_compressee = os.path.getsize(fichier_compresse)
    ratio = (1 - taille_compressee / taille_originale) * 100
    
    print(f"[2/4] Fichier compresse: {taille_compressee} octets (gain: {ratio:.1f}%)")
    
    # Assertions sur la compression
    assert os.path.exists(fichier_compresse), "Le fichier compresse n'existe pas"
    assert taille_compressee > 0, "Le fichier compresse est vide"
    assert taille_compressee < taille_originale, "Pas de compression effective"
    
    # Decompression
    decompresser_fichier(fichier_compresse, fichier_decompresse)
    taille_decompresse = os.path.getsize(fichier_decompresse)
    
    print(f"[3/4] Fichier decompresse: {taille_decompresse} octets")
    
    # Verification
    with open(fichier_original, "r", encoding="utf-8") as f:
        contenu_original = f.read()
    
    with open(fichier_decompresse, "r", encoding="utf-8") as f:
        contenu_decompresse = f.read()
    
    print(f"[4/4] Verification de l'integrite...")
    
    # Assertions critiques
    assert os.path.exists(fichier_decompresse), "Le fichier decompresse n'existe pas"
    assert taille_decompresse == taille_originale, f"Tailles differentes: {taille_decompresse} != {taille_originale}"
    assert contenu_decompresse == contenu_original, "Contenu different apres decompression"
    assert len(contenu_decompresse) == len(contenu_original), "Longueurs differentes"
    
    print("\n>>> SUCCES ! Toutes les assertions passent <<<")
    print(f">>> Taux de compression: {ratio:.1f}% <<<\n")
    
    return True


if __name__ == "__main__":
    try:
        test_compression_decompression()
        print("[OK] Test termine avec succes")
    except AssertionError as e:
        print(f"\n[ERREUR] Assertion echouee: {e}")
        exit(1)
    except Exception as e:
        print(f"\n[ERREUR] Exception: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
