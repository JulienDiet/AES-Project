# This is a sample Python script.
import os
from random import random, randint

from picture import encrypt_image, decrypt_image


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def clean_old_files():
    global dirname, directory_names, filenames, filename
    for dirname, directory_names, filenames in os.walk('resources\\Encrypted'):
        for filename in filenames:
            os.remove(os.path.join(dirname, filename))
    for dirname, directory_names, filenames in os.walk('resources\\Decrypted'):
        for filename in filenames:
            os.remove(os.path.join(dirname, filename))


def choisir_mode_operatoire():
    """
    Demande à l'utilisateur de choisir un mode opératoire parmi ECB, CBC et PCBC.
    Capture la réponse et la renvoie sous forme de chaîne de caractères.
    """
    modes = ["ECB", "CBC", "PCBC"]
    print("Veuillez choisir un mode opératoire parmi les suivants :")
    for i, mode in enumerate(modes, 1):
        print(f"{i}. {mode}")

    # Capturer la réponse de l'utilisateur
    choix = input("Entrez le numéro correspondant à votre choix (1-3) : ")

    # Vérifier si l'entrée est valide
    try:
        choix = int(choix)
        if 1 <= choix <= 3:
            return modes[choix - 1]
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 3.")
            return choisir_mode_operatoire()  # Relancer si le choix est invalide
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entier.")
        return choisir_mode_operatoire()  # Relancer si l'entrée est invalide


def choisir_longueur_cle():
    """
    Demande à l'utilisateur de choisir la longueur de la clé AES parmi 128, 192, ou 256 bits.
    Capture la réponse et la renvoie sous forme de nombre entier.
    """
    longueurs = [128, 192, 256]
    print("Veuillez choisir la longueur de la clé AES parmi les suivantes :")
    for i, longueur in enumerate(longueurs, 1):
        print(f"{i}. {longueur} bits")

    # Capturer la réponse de l'utilisateur
    choix = input("Entrez le numéro correspondant à votre choix (1-3) : ")

    # Vérifier si l'entrée est valide
    try:
        choix = int(choix)
        if 1 <= choix <= 3:
            return longueurs[choix - 1]
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 3.")
            return choisir_longueur_cle()  # Relancer si le choix est invalide
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entier.")
        return choisir_longueur_cle()  # Relancer si l'entrée est invalide


import os


def choisir_fichier_dans_dossier(dossier):
    """
    Demande à l'utilisateur de choisir un fichier parmi ceux disponibles dans le dossier 'Images'.
    Capture la réponse et renvoie le nom du fichier sélectionné.
    """

    # Vérifier si le dossier existe
    if not os.path.exists(dossier):
        print(f"Le dossier '{dossier}' n'existe pas.")
        return None

    # Lister les fichiers dans le dossier
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]

    # Vérifier s'il y a des fichiers dans le dossier
    if not fichiers:
        print(f"Aucun fichier trouvé dans le dossier '{dossier}'.")
        return None

    # Afficher la liste des fichiers
    print("Veuillez choisir un fichier parmi les suivants :")
    for i, fichier in enumerate(fichiers, 1):
        print(f"{i}. {fichier}")

    # Capturer la réponse de l'utilisateur
    choix = input(f"Entrez le numéro correspondant à votre choix (1-{len(fichiers)}) : ")

    # Vérifier si l'entrée est valide
    try:
        choix = int(choix)
        if 1 <= choix <= len(fichiers):
            return fichiers[choix - 1]
        else:
            print(f"Choix invalide. Veuillez entrer un numéro entre 1 et {len(fichiers)}.")
            return choisir_fichier_dans_dossier()  # Relancer si le choix est invalide
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entier.")
        return choisir_fichier_dans_dossier()  # Relancer si l'entrée est invalide


def demander_effacement():
    """
    Demande à l'utilisateur s'il souhaite effacer les anciens fichiers.
    Capture la réponse et renvoie True si l'utilisateur a répondu 'oui', sinon False.
    """
    reponse = input(
        "Souhaitez-vous effacer les anciens fichiers des dossiers 'Decrypted' et 'Encrypted' ? (oui/non) : ").strip().lower()

    if reponse == "oui":
        return True
    elif reponse == "non":
        return False
    else:
        print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
        return demander_effacement()  # Redemander si la réponse est invalide


def demander_action():
    """
    Demande à l'utilisateur s'il souhaite chiffrer ou déchiffrer une image.
    Capture la réponse et renvoie 'chiffrer' ou 'déchiffrer'.
    """
    action = input("Souhaitez-vous chiffrer ou déchiffrer une image ? (chiffrer/déchiffrer) : ").strip().lower()

    if action in ["chiffrer", "déchiffrer"]:
        return action
    else:
        print("Réponse invalide. Veuillez répondre par 'chiffrer' ou 'déchiffrer'.")
        return demander_action()  # Redemander si la réponse est invalide


def demander_cle_aes():
    """
    Demande à l'utilisateur d'encoder la clé AES de chiffrement en hexadécimal.
    Capture et renvoie la clé sous forme d'octets (bytes).
    """
    cle_hex = input("Veuillez entrer la clé AES en hexadécimal : ").strip()

    # Vérification que la clé est valide (longueur 128, 192 ou 256 bits en hexadécimal)
    try:
        # Vérifier si la longueur correspond à 128, 192 ou 256 bits (32, 48 ou 64 caractères hexadécimaux)
        if len(cle_hex) not in [32, 48, 64]:
            raise ValueError("La clé doit être de 128, 192 ou 256 bits (32, 48 ou 64 caractères hexadécimaux).")

        # Convertir la clé hexadécimale en bytes
        cle_bytes = bytes.fromhex(cle_hex)
        return cle_bytes, len(cle_hex)*4

    except ValueError as e:
        print(f"Erreur : {e}")
        return demander_cle_aes()  # Redemander la clé si elle est invalide

def afficher_menu():
    """
    Affiche un menu proposant trois choix : nettoyer les fichiers, chiffrer et déchiffrer.
    Capture le choix de l'utilisateur et exécute l'action correspondante.
    """
    print("Menu :")
    print("1. Nettoyer les fichiers")
    print("2. Chiffrer une image")
    print("3. Déchiffrer une image")

    choix = input("Veuillez entrer le numéro correspondant à votre choix (1-3) : ").strip()

    # Vérification que le choix est valide
    if choix == "1":
        nettoyer_fichiers()
    elif choix == "2":
        chiffrer_image()
    elif choix == "3":
        dechiffrer_image()
    else:
        print("Choix invalide. Veuillez entrer un numéro entre 1 et 3.")
        afficher_menu()  # Relancer le menu si l'entrée est invalide


def nettoyer_fichiers():
    """
    Fonction pour nettoyer les fichiers. (Simulée ici, à personnaliser selon vos besoins)
    """
    print("Nettoyage des fichiers en cours...")
    clean_old_files()
    print("Les fichiers ont été nettoyés.")


def chiffrer_image():
    """
    Fonction pour chiffrer une image. (Simulée ici, à personnaliser selon vos besoins)
    """
    dossier = "resources\\Images"
    mode_selectionne = choisir_mode_operatoire()
    fichier_selectionne = choisir_fichier_dans_dossier(dossier)
    longueur_cle = choisir_longueur_cle()
    print("Chiffrement de l'image...")
    key = randint(0, 2 ** longueur_cle - 1)
    print('Generated key : ' + hex(key))
    encrypt_image(os.path.join(dossier, fichier_selectionne), key, longueur_cle, mode_selectionne)
    print(f"L'image {fichier_selectionne} a été chiffrée :")
    print(f"Mode opératoire sélectionné : {mode_selectionne}")
    print('Generated key : ' + hex(key))


def dechiffrer_image():
    """
    Fonction pour déchiffrer une image. (Simulée ici, à personnaliser selon vos besoins)
    """
    dossier = "resources\\Encrypted"
    mode_selectionne = choisir_mode_operatoire()
    fichier_selectionne = choisir_fichier_dans_dossier(dossier)
    key_bytes, longueur_cle = demander_cle_aes()
    print("Déchiffrement de l'image...")
    key = int.from_bytes(key_bytes, "big")
    decrypt_image(os.path.join('resources\\Encrypted', fichier_selectionne), key, longueur_cle, mode_selectionne)
    print(f"L'image {fichier_selectionne} a été déchiffrée.")
    print(f"Mode opératoire sélectionné : {mode_selectionne}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    afficher_menu()