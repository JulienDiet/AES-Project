import os
from aes_encryption import aes_encrypt_block, aes_decrypt_block


def rdm_iv_generator():
    """
    Cette fonction doit être capable de générer un nombre aléatoire de 128 bits.
    :return: un entier de 128 bits généré aléatoirement.
    """
    iv = os.urandom(16)
    return int.from_bytes(iv, byteorder='big')


def rdm_iv_generator_with_counter():
    """
    Cette fonction doit être capable de générer un nombre aléatoire à partir de 96 bits les plus
    significatifs aléatoires,
    en laissant les bits les moins significatifs à zéro pour le compteur.
    :return: un entier de 128 bits généré aléatoirement.
    """
    random_bits = os.urandom(12)
    random_integer = int.from_bytes(random_bits, byteorder='big')
    iv = (random_integer << 32)
    return iv


def encrypt_ecb(blocks, key, security):
    """
    Cette fonction applique le chiffrement AES à une liste de blocs de 128 bits en utilisant le mode de
    fonctionnement ECB.
    :param blocks: Liste de blocs (128 bits) à chiffrer.
    :param key: Clé de chiffrement de 128/192/256 bits.
    :param security: le niveau de sécurité AES correspondant à la longueur de la clé sous forme d'entier
    :return: la liste des blocs chiffrés.
    """
    encrypted_blocks = []
    for block in blocks:
        encrypted_block = aes_encrypt_block(block, key, security)
        encrypted_blocks.append(encrypted_block)
    return encrypted_blocks


def decrypt_ecb(blocks, key, security):
    """
    Cette fonction déchiffre une liste de blocs de 128 bits qui ont été préalablement chiffrés
    avec AES en utilisant le mode de fonctionnement ECB.
    :param blocks: Liste de blocs à déchiffrer.
    :param key: Clé de chiffrement de 128/192/256 bits, identique à celle utilisée pour le chiffrement.
    :param security: le niveau de sécurité AES correspondant à la longueur de la clé sous forme d'entier
    :return: la liste des blocs déchiffrés.
    """
    decrypted_blocks = []
    for block in blocks:
        decrypted_block = aes_decrypt_block(block, key, security)
        decrypted_blocks.append(decrypted_block)
    return decrypted_blocks


def encrypt_cbc(blocks, key, security):
    """
    Cette fonction applique le chiffrement AES à une liste de blocs de 128 bits en utilisant le mode de
    fonctionnement CBC.
    :param blocks: Liste de blocs (128 bits) à chiffrer.
    :param key: Clé de chiffrement de 128/192/256 bits.
    :param security: le niveau de sécurité AES correspondant à la longueur de la clé sous forme d'entier
    :return: la liste des blocs chiffrés.
    """
    iv = rdm_iv_generator()
    encrypted_blocks = []
    previous_block = iv

    for block in blocks:
        block_to_encrypt = block ^ previous_block
        encrypted_block = aes_encrypt_block(block_to_encrypt, key, security)
        encrypted_blocks.append(encrypted_block)
        previous_block = encrypted_block

    return [iv] + encrypted_blocks


def decrypt_cbc(blocks, key, security):
    """
    Cette fonction déchiffre une liste de blocs de 128 bits qui ont été préalablement chiffrés
    avec AES en utilisant le mode de fonctionnement CBC.
    :param blocks: Liste de blocs à déchiffrer.
    :param key: Clé de chiffrement de 128/192/256 bits, identique à celle utilisée pour le chiffrement.
    :param security: le niveau de sécurité AES correspondant à la longueur de la clé sous forme d'entier
    :return: la liste des blocs déchiffrés.
    """
    iv = blocks[0]
    encrypted_blocks = blocks[1:]
    decrypted_blocks = []
    previous_block = iv

    for block in encrypted_blocks:
        decrypted_block = aes_decrypt_block(block, key, security)
        decrypted_block ^= previous_block
        decrypted_blocks.append(decrypted_block)
        previous_block = block

    return decrypted_blocks


def encrypt_pcbc(blocks, key, security):
    """
    Cette fonction applique le chiffrement AES à une liste de blocs de 128 bits en utilisant le mode de
    fonctionnement PCBC.
    :param blocks: Liste de blocs (128 bits) à chiffrer.
    :param key: Clé de chiffrement de 128/192/256 bits.
    :param security: le niveau de sécurité AES correspondant à la longueur de la clé sous forme d'entier
    :return: la liste des blocs chiffrés.
    """
    iv = rdm_iv_generator()
    encrypted_blocks = []
    previous_block = iv

    for block in blocks:
        block_to_encrypt = block ^ previous_block
        encrypted_block = aes_encrypt_block(block_to_encrypt, key, security)
        encrypted_blocks.append(encrypted_block)
        previous_block = block ^ encrypted_block

    return [iv] + encrypted_blocks


def decrypt_pcbc(blocks, key, security):
    """
    Cette fonction déchiffre une liste de blocs de 128 bits qui ont été préalablement chiffrés
    avec AES en utilisant le mode de fonctionnement PCBC.
    :param blocks: Liste de blocs à déchiffrer.
    :param key: Clé de chiffrement de 128/192/256 bits, identique à celle utilisée pour le chiffrement.
    :param security: le niveau de sécurité AES correspondant à la longueur de la clé sous forme d'entier
    :return: la liste des blocs déchiffrés.
    """

    iv = blocks[0]
    encrypted_blocks = blocks[1:]
    decrypted_blocks = []
    previous_block = iv

    for encrypted_block in encrypted_blocks:
        decrypted_block = aes_decrypt_block(encrypted_block, key, security)
        plaintext_block = decrypted_block ^ previous_block
        decrypted_blocks.append(plaintext_block)
        previous_block = plaintext_block ^ encrypted_block

    return decrypted_blocks


def decrypt(blocks, key, security, operation_mode="ECB"):
    """
    Cette fonction déchiffre une liste de blocs de 128 bits qui ont été préalablement chiffrés
    avec AES selon le mode de fonctionnement donné en argument.
    :param blocks: Liste de blocs à déchiffrer.
    :param key: Clé de chiffrement de 128/192/256 bits, identique à celle utilisée pour le chiffrement.
    :param security: le niveau de sécurité AES correspondant à la longueur de la clé sous forme d'entier
    :param operation_mode: chaîne spécifiant le mode de fonctionnement (‘ECB’ ou ‘CBC’).
    :return: la liste des blocs déchiffrés.
    """
    if operation_mode == "ECB":
        return decrypt_ecb(blocks, key, security)
    elif operation_mode == "CBC":
        return decrypt_cbc(blocks, key, security)
    elif operation_mode == "PCBC":
        return decrypt_pcbc(blocks, key, security)
    else:
        raise ValueError("Invalid operation mode")


def encrypt(blocks, key, security, operation_mode="ECB"):
    """
    Cette fonction chiffre une liste de blocs de 128 bits
    avec AES selon le mode de fonctionnement donné en argument.
    :param blocks: Liste de blocs à chiffrer.
    :param key: la clé de chiffrement de 128/192/256 bits.
    :param security: le niveau de sécurité AES correspondant à la longueur de la clé sous forme d'entier
    :param operation_mode: chaîne spécifiant le mode de fonctionnement ("ECB", "CBC", "PCBC").
    :return: la liste des blocs chiffrés.
    """
    if operation_mode == "ECB":
        return encrypt_ecb(blocks, key, security)
    elif operation_mode == "CBC":
        return encrypt_cbc(blocks, key, security)
    elif operation_mode == "PCBC":
        return encrypt_pcbc(blocks, key, security)
    else:
        raise ValueError("Invalid operation mode")
