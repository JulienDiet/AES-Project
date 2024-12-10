from substitution import *


def round_constant():
    """
    This function returns the 10 first round constants.
    :return: an array containing the 10 first round constants
    """
    return [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


def rotword(word32bits):
    """
    This function takes the 8 most significant bits and places them as least significant bits.
    All other bits move of 8 places from least to most significant.
    :param word32bits: a 32-bit word to which the rotword is applied
    :return: the result of the rotword operation as a 32-bit word
    """
    return (word32bits << 8 | (word32bits >> 24)) & 0xFFFFFFFF


def subword(word32bits, substitution_box):
    """
    This function replaces all the bytes that make up the 32-bit word with the corresponding bytes in the substitution
    box receive in the argument.
    :param word32bits: a 32-bit word to which the subword is applied
    :param substitution_box: the substitution box (table) required for the subword operation
    :return: the result of the subword operation as a 32-bit word
    """
    result = 0
    for i in range(4):  # Process each byte
        byte = (word32bits >> (24 - i * 8)) & 0xFF
        substituted_byte = substitution(substitution_box, byte)
        result |= substituted_byte << (24 - i * 8)
    return result


def original_key_to_word32bits(original_key, length):
    """
    This function splits the key into 32-bit words. The words are placed in an array
    starting with the most significant 32-bit word.
    :param original_key: 128/192/256-bit key
    :param length: the number of bits as an integer value
    :return: an array containing the 32-bit words that make up the key
    """
    # Si original_key est un entier, on le convertit en bytes
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
    This function implements the key schedule:
    (i) obtains the round constants
    (ii) converts the original key into a 32-bit word
    (iii) determines the number of 32-bit words from the key and the number of AES rounds
    (iv) executes the key schedule to build all the 32-bit words that make up the AES round keys
    :param original_key: 128/192/256-bit key
    :param length: the number of bits as an integer value
    :param substitution_box: the substitution box (table) required for the key schedule operation
    :return: an array containing the 32-bit words that make up the AES round keys.
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
