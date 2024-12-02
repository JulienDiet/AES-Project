def matrix_xor(matrix, key):
    """
    This function performs XOR operation on bytes from the matrix given as arguments.
    :param matrix: a 4x4 bytes matrix
    :param key: a 4x4 bytes matrix
    :return: a 4x4 bytes matrix containing the XOR result between the corresponding bytes of
             the matrix received as arguments
    """


def sub_bytes(matrix, substitution_box):
    """
    This function performs the substitution on byte from the matrix given as argument.
    :param matrix: a 4x4 bytes matrix
    :param substitution_box: the AES substitution box
    :return: a 4x4 bytes matrix consisting of the substituted bytes of the matrix given as argument.
    """


def shift_rows(matrix):
    """
    This function performs the AES shift rows operation on the matrix given as argument.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param matrix: a 4x4 bytes matrix
    """

def inv_shift_rows(matrix):
    """
    This function performs the inverted AES shift rows operation on the matrix given as argument.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param matrix: a 4x4 bytes matrix
    """

def mix_column(r):
    """
    This function performs polynomial multiplication 3x^3+x^2+x+2 (modulo x^4+1) with bytes in GF(2^8) as coefficient.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param r: a column composed of 4 bytes
    :return: the result of mix column as a column composed of 4 bytes
    """


def inv_mix_column(r):
    """
    This function performs polynomial multiplication by 11x^3+13x^2+9x+14 (modulo x^4+1) with bytes in GF(2^8) as coefficient.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param r: a column composed of 4 bytes
    :return: the result of mix column as a column composed of 4 bytes
    """

def mix_columns(matrix):
    """
    This function performs the AES mix columns operation on each column of the matrix given as argument.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param matrix: a 4x4 bytes matrix
    :return: a 4x4 bytes matrix as the result of the mix columns operation
    """

def inv_mix_columns(matrix):
    """
    This function performs the inverted AES mix columns operation on each column of the matrix given as argument.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param matrix: a 4x4 bytes matrix
    :return: a 4x4 bytes matrix as the result of the inverted AES mix columns operation
    """

def aes_round(blockmatrix, key_matrix, substitution_box):
    """
    This function performs a round of the AES by executing all the steps in the prescribed order
    :param blockmatrix: block to encrypt as 4x4 bytes matrix
    :param key_matrix: AES key as a 4x4 bytes matrix
    :param substitution_box: the AES substitution box
    :return: the block to encrypt, after one round, as 4x4 bytes matrix
    """

def aes_inverse_round(blockmatrix, key_matrix, inverse_substitution_box):
    """
    This function performs an inverse round of the AES by executing all the steps in the prescribed order
    :param blockmatrix: block to decrypt as 4x4 bytes matrix
    :param key_matrix: AES key as a 4x4 bytes matrix
    :param inverse_substitution_box: the inverted AES substitution box
    :return: the block to decrypt, after one unversed round, as 4x4 bytes matrix
    """


def aes_final_round(blockmatrix, key_matrix, substitution_box):
    """
    This function performs the final round of the AES by executing all the steps in the prescribed order
    :param blockmatrix: block to encrypt as 4x4 bytes matrix
    :param key_matrix: AES key as a 4x4 bytes matrix
    :param substitution_box: the AES substitution box
    :return: the block to encrypt, after the final round, as 4x4 bytes matrix
    """

def aes_inverse_final_round(blockmatrix, key_matrix, inverse_substitution_box):
    """
    This function performs the inverse final round of the AES by executing all the steps in the prescribed order
    :param blockmatrix: block to decrypt as 4x4 bytes matrix
    :param key_matrix: AES key as a 4x4 bytes matrix
    :param inverse_substitution_box: the inverted AES substitution box
    :return: the block to decrypt, after the inverse final round, as 4x4 bytes matrix
    """
