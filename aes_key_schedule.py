def round_constant():
    """
    This function returns the 10 first round constants.
    :return: an array containing the 10 first round constants
    """


def rotword(word32bits):
    """
    This function takes the 8 most significant bits and places them as least significant bits.
    All other bits move of 8 places from least to most significant.
    :param word32bits: a 32-bit word to which the rotword is applied
    :return: the result of the rotword operation as a 32-bit word
    """


def subword(word32bits, substitution_box):
    """
    This function replaces all the bytes that make up the 32-bit word with the corresponding bytes in the substitution
    box receive in the argument.
    :param word32bits: a 32-bit word to which the subword is applied
    :param substitution_box: the substitution box (table) required for the subword operation
    :return: the result of the subword operation as a 32-bit word
    """


def inv_subword(word32bits, inverse_substitution_box):
    """
    This function replaces all the bytes that make up the 32-bit word with the corresponding bytes in the substitution
    box receive in the argument. This function could be implemented using the subword function.
    :param word32bits: a 32-bit word to which the inv_subword is applied
    :param inverse_substitution_box: the substitution box (table) required for the inv_subword operation
    :return: the result of the inv_subword operation as a 32-bit word
    """


def original_key_to_word32bits(original_key, length):
    """
    This function splits the key into 32-bit words. The words are placed in an array
    starting with the most significant 32-bit word
    :param original_key: 128/192/256-bit key
    :param length: the number of bits as an integer value
    :return: an array containing the 32-bit words that make up the key
    """


def key_schedule(original_key, length, substitution_box):
    """
    This function implements the key schedule :
    (i) obtains the round constants
    (ii) converts the original key into a 32-bit word
    (iii) determines the number of 32-bit words from the key and the number of AES rounds
    (iv) executes the key schedule to build all the 32-bit words that make up the AES round keys
    :param original_key: 128/192/256-bit key
    :param length: the number of bits as an integer value
    :param substitution_box: the substitution box (table) required for the key schedule operation
    :return: an array containing the 32-bit words that make up the AES round keys.
    """
