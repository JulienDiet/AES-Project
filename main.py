import os
from random import randint
from picture import encrypt_image, decrypt_image

def clean_old_files():
    for dirname, _, filenames in os.walk('resources\\Encrypted'):
        for filename in filenames:
            os.remove(os.path.join(dirname, filename))
    for dirname, _, filenames in os.walk('resources\\Decrypted'):
        for filename in filenames:
            os.remove(os.path.join(dirname, filename))

def choisir_mode_operatoire():
    modes = ["ECB", "CBC", "PCBC"]
    print("Veuillez choisir un mode opératoire parmi les suivants :")
    for i, mode in enumerate(modes, 1):
        print(f"{i}. {mode}")
    while True:
        choix = input("Entrez le numéro correspondant à votre choix (1-3) : ")
        if choix.isdigit() and 1 <= int(choix) <= 3:
            return modes[int(choix) - 1]
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 3.")

def choisir_longueur_cle():
    longueurs = [128, 192, 256]
    print("Veuillez choisir la longueur de la clé AES parmi les suivantes :")
    for i, longueur in enumerate(longueurs, 1):
        print(f"{i}. {longueur} bits")
    while True:
        choix = input("Entrez le numéro correspondant à votre choix (1-3) : ")
        if choix.isdigit() and 1 <= int(choix) <= 3:
            return longueurs[int(choix) - 1]
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 3.")

def choisir_fichier_dans_dossier(dossier):
    if not os.path.exists(dossier):
        print(f"Le dossier '{dossier}' n'existe pas.")
        return None

    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
    if not fichiers:
        print(f"Aucun fichier trouvé dans le dossier '{dossier}'.")
        return None

    print("Veuillez choisir un fichier parmi les suivants :")
    for i, fichier in enumerate(fichiers, 1):
        print(f"{i}. {fichier}")
    while True:
        choix = input(f"Entrez le numéro correspondant à votre choix (1-{len(fichiers)}) : ")
        if choix.isdigit() and 1 <= int(choix) <= len(fichiers):
            return fichiers[int(choix) - 1]
        else:
            print(f"Choix invalide. Veuillez entrer un numéro entre 1 et {len(fichiers)}.")

def demander_cle_aes():
    while True:
        cle_hex = input("Veuillez entrer la clé AES en hexadécimal : ").strip()
        try:
            if len(cle_hex) not in [32, 48, 64]:
                raise ValueError("La clé doit être de 128, 192 ou 256 bits (32, 48 ou 64 caractères hexadécimaux).")
            return bytes.fromhex(cle_hex), len(cle_hex) * 4
        except ValueError as e:
            print(f"Erreur : {e}")

def nettoyer_fichiers():
    print("Nettoyage des fichiers en cours...")
    clean_old_files()
    print("Les fichiers ont été nettoyés.")

def chiffrer_image():
    dossier = "resources\\Images"
    mode_selectionne = choisir_mode_operatoire()
    fichier_selectionne = choisir_fichier_dans_dossier(dossier)
    if fichier_selectionne is None:
        return
    longueur_cle = choisir_longueur_cle()
    print("Chiffrement de l'image...")
    key = randint(0, 2 ** longueur_cle - 1)
    key_bytes = key.to_bytes(longueur_cle // 8, 'big')
    print('Generated key : ' + hex(key))
    encrypt_image(os.path.join(dossier, fichier_selectionne), key_bytes, longueur_cle, mode_selectionne)
    print(f"L'image {fichier_selectionne} a été chiffrée avec le mode {mode_selectionne}.")

def dechiffrer_image():
    dossier = "resources\\Encrypted"
    mode_selectionne = choisir_mode_operatoire()
    fichier_selectionne = choisir_fichier_dans_dossier(dossier)
    if fichier_selectionne is None:
        return
    key_bytes, longueur_cle = demander_cle_aes()
    decrypt_image(os.path.join(dossier, fichier_selectionne), key_bytes, longueur_cle, mode_selectionne)
    print(f"L'image {fichier_selectionne} a été déchiffrée avec le mode {mode_selectionne}.")

def afficher_menu():
    while True:
        print("\nMenu :")
        print("1. Nettoyer les fichiers")
        print("2. Chiffrer une image")
        print("3. Déchiffrer une image")
        print("4. Quitter")

        choix = input("Veuillez entrer le numéro correspondant à votre choix (1-4) : ").strip()
        if choix == "1":
            nettoyer_fichiers()
        elif choix == "2":
            chiffrer_image()
        elif choix == "3":
            dechiffrer_image()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 4.")

if __name__ == '__main__':
    afficher_menu()
