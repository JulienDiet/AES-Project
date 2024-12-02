def multiply_by_2(a):
    """
    Cette fonction effectue une multiplication dans le corps fini GF(2^8) par 2.
    Voir la documentation AES référencée dans les instructions et le site HELMo Learn pour une solution simple et rapide.
    :param a: l'octet à multiplier par 2
    :return: le résultat de l'opération sous forme d'octet
    """
    if a & 0x80:
        return ((a << 1) ^ 0x1B) & 0xFF
    else:
        return (a << 1) & 0xFF


def multiply_by_3(a):
    """
    This function executes GF(2^8) multiplication by 3.
    See the AES documentation referenced in the instructions and the HELMo Learn website for a quick and easy solution.
    :param a: the byte to multiply by 3
    :return: the result of the operation as a byte
    """
    return multiply_by_2(a) ^ a


def multiply_by_9(a):
    """
    This function executes GF(2^8) multiplication by 9.
    See the AES documentation referenced in the instructions and the HELMo Learn website for a quick and easy solution.
    :param a: the byte to multiply by 9
    :return: the result of the operation as a byte
    """
    return multiply_by_2(multiply_by_2(multiply_by_2(a))) ^ a


def multiply_by_11(a):
    """
    This function executes GF(2^8) multiplication by 11.
    See the AES documentation referenced in the instructions and the HELMo Learn website for a quick and easy solution.
    :param a: the byte to multiply by 11
    :return: the result of the operation as a byte
    """
    return multiply_by_2(multiply_by_2(multiply_by_2(a)) ^ a) ^ a


def multiply_by_13(a):
    """
    This function executes GF(2^8) multiplication by 13.
    See the AES documentation referenced in the instructions and the HELMo Learn website for a quick and easy solution.
    :param a: the byte to multiply by 13
    :return: the result of the operation as a byte
    """
    return multiply_by_2(multiply_by_2(multiply_by_2(a) ^ a)) ^ a


def multiply_by_14(a):
    """
    This function executes GF(2^8) multiplication by 14.
    See the AES documentation referenced in the instructions and the HELMo Learn website for a quick and easy solution.
    :param a: the byte to multiply by 14
    :return: the result of the operation as a byte
    """
    return multiply_by_2(multiply_by_2(multiply_by_2(a) ^ a) ^ a)