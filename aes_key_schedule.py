from substitution import *


def round_constant():
    """
    Cette fonction renvoie les 10 premières constantes de round.
    :return: un tableau contenant les 10 premières constantes de round
    """

    return [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


def rotword(word32bits):
    """
    Cette fonction prend les 8 bits les plus significatifs et les place comme les bits les moins significatifs.
    Tous les autres bits se déplacent de 8 positions des moins significatifs aux plus significatifs.
    :param word32bits: un mot de 32 bits auquel l'opération rotword est appliquée
    :return: le résultat de l'opération rotword sous forme de mot de 32 bits
    """

    return (word32bits << 8 | (word32bits >> 24)) & 0xFFFFFFFF


def subword(word32bits, substitution_box):
    """
    Cette fonction remplace tous les octets qui composent le mot de 32 bits par les octets correspondants dans la boîte
    de substitution reçue en argument.
    :param word32bits: un mot de 32 bits auquel l'opération subword est appliquée
    :param substitution_box: la boîte de substitution (table) nécessaire pour l'opération subword
    :return: le résultat de l'opération subword sous forme de mot de 32 bits
    """

    result = 0
    for i in range(4):
        byte = (word32bits >> (24 - i * 8)) & 0xFF
        substituted_byte = substitution(substitution_box, byte)
        result |= substituted_byte << (24 - i * 8)
    return result


def original_key_to_word32bits(original_key, length):
    """
    Cette fonction divise la clé en mots de 32 bits. Les mots sont placés dans un tableau
    en commençant par le mot de 32 bits le plus significatif.
    :param original_key: clé de 128/192/256 bits
    :param length: le nombre de bits sous forme d'entier
    :return: un tableau contenant les mots de 32 bits qui composent la clé
    """

    if isinstance(original_key, int):
        original_key = original_key.to_bytes(length // 8, 'big')

    if length == 128:
        nb_words = 4
    elif length == 192:
        nb_words = 6
    elif length == 256:
        nb_words = 8
    else:
        raise ValueError("The key length must be 128, 192 or 256 bits.")

    if len(original_key) != length // 8:
        raise ValueError(f"The original key must be {length // 8} bytes long.")

    words = [int.from_bytes(original_key[i * 4:(i + 1) * 4], "big") for i in range(nb_words)]
    return words


def key_schedule(original_key, length, substitution_box):
    """
    Cette fonction implémente le programme de génération de clés :
    (i) obtient les constantes de round
    (ii) convertit la clé originale en mots de 32 bits
    (iii) détermine le nombre de mots de 32 bits à partir de la clé et le nombre de tours AES
    (iv) exécute le programme de génération de clés pour construire tous les mots de 32 bits qui composent
    les clés des tours AES
    :param original_key: clé de 128/192/256 bits
    :param length: le nombre de bits sous forme d'entier
    :param substitution_box: la boîte de substitution (table) nécessaire pour l'opération de génération de clés
    :return: un tableau contenant les mots de 32 bits qui composent les clés des tours AES.
    """

    round_constants = round_constant()
    words = original_key_to_word32bits(original_key, length)

    if length == 128:
        nb_rounds = 10
        nb_words = 4
    elif length == 192:
        nb_rounds = 12
        nb_words = 6
    elif length == 256:
        nb_rounds = 14
        nb_words = 8
    else:
        raise ValueError("The key length must be 128, 192, or 256 bits.")

    for i in range(nb_words, 4 * (nb_rounds + 1)):
        temp = words[i - 1]

        if i % nb_words == 0:
            temp = rotword(temp)
            temp = subword(temp, substitution_box)
            temp = temp ^ (round_constants[i // nb_words - 1] << 24)
        elif nb_words > 6 and i % nb_words == 4:
            temp = subword(temp, substitution_box)

        words.append(words[i - nb_words] ^ temp)

    return words
