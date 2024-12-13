def multiply_by_2(a):
    """
    Cette fonction effectue une multiplication dans le corps fini GF(2^8) par 2.
    Voir la documentation AES référencée dans les instructions et le site HELMo Learn pour une solution simple
    et rapide.
    :param a: l'octet à multiplier par 2
    :return: le résultat de l'opération sous forme d'octet
    """
    if a & 0x80:
        return ((a << 1) ^ 0x1B) & 0xFF
    else:
        return (a << 1) & 0xFF


def multiply_by_3(a):
    """
    Cette fonction exécute la multiplication dans GF(2^8) par 3.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour une solution
    rapide et facile.
    :param a: l'octet à multiplier par 3
    :return: le résultat de l'opération sous forme d'octet
    """
    return multiply_by_2(a) ^ a


def multiply_by_9(a):
    """
    Cette fonction exécute la multiplication dans GF(2^8) par 9.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour une solution
    rapide et facile.
    :param a: l'octet à multiplier par 9
    :return: le résultat de l'opération sous forme d'octet
    """
    return multiply_by_2(multiply_by_2(multiply_by_2(a))) ^ a


def multiply_by_11(a):
    """
    Cette fonction exécute la multiplication dans GF(2^8) par 11.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour une solution
    rapide et facile.
    :param a: l'octet à multiplier par 11
    :return: le résultat de l'opération sous forme d'octet
    """
    return multiply_by_2(multiply_by_2(multiply_by_2(a)) ^ a) ^ a


def multiply_by_13(a):
    """
    Cette fonction exécute la multiplication dans GF(2^8) par 13.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour une solution
    rapide et facile.
    :param a: l'octet à multiplier par 13
    :return: le résultat de l'opération sous forme d'octet
    """
    return multiply_by_2(multiply_by_2(multiply_by_2(a) ^ a)) ^ a


def multiply_by_14(a):
    """
    Cette fonction exécute la multiplication dans GF(2^8) par 14.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour une solution
    rapide et facile.
    :param a: l'octet à multiplier par 14
    :return: le résultat de l'opération sous forme d'octet
    """
    return multiply_by_2(multiply_by_2(multiply_by_2(a) ^ a) ^ a)
