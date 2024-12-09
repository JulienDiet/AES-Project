from gf256_multiplication import *
from substitution import *


def matrix_xor(matrix, key):
    """
    This function performs XOR operation on bytes from the matrix given as arguments.
    :param matrix: a 4x4 bytes matrix
    :param key: a 4x4 bytes matrix
    :return: a 4x4 bytes matrix containing the XOR result between the corresponding bytes of
             the matrix received as arguments
    """
    if len(matrix) != 4 or len(key) != 4:
        raise ValueError("Both matrices must be 4x4.")
    if any(len(row) != 4 for row in matrix) or any(len(row) != 4 for row in key):
        raise ValueError("Both matrices must be 4x4.")

    result = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            result[i][j] = matrix[i][j] ^ key[i][j]

    return result


def sub_bytes(matrix, substitution_box):
    """
    This function performs the substitution on byte from the matrix given as argument.
    :param matrix: a 4x4 bytes matrix
    :param substitution_box: the AES substitution box
    :return: a 4x4 bytes matrix consisting of the substituted bytes of the matrix given as argument.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            byte = matrix[i][j]
            row = byte >> 4
            col = byte & 0x0F
            matrix[i][j] = substitution_box[row][col]
    return matrix


def shift_rows(matrix):
    """
    This function performs the AES shift rows operation on the matrix given as argument.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param matrix: a 4x4 bytes matrix
    """
    return [
        matrix[0],
        matrix[1][1:] + matrix[1][:1],
        matrix[2][2:] + matrix[2][:2],
        matrix[3][3:] + matrix[3][:3]
    ]


def inv_shift_rows(matrix):
    """
    This function performs the inverted AES shift rows operation on the matrix given as argument.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param matrix: a 4x4 bytes matrix
    """
    return [
        matrix[0],
        matrix[1][-1:] + matrix[1][:-1],
        matrix[2][-2:] + matrix[2][:-2],
        matrix[3][-3:] + matrix[3][:-3]
    ]


def mix_column(r):
    """
    This function performs polynomial multiplication 3x^3+x^2+x+2 (modulo x^4+1) with bytes in GF(2^8) as coefficient.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param r: a column composed of 4 bytes
    :return: the result of mix column as a column composed of 4 bytes
    """
    return [
        multiply_by_2(r[0]) ^ multiply_by_3(r[1]) ^ r[2] ^ r[3],
        r[0] ^ multiply_by_2(r[1]) ^ multiply_by_3(r[2]) ^ r[3],
        r[0] ^ r[1] ^ multiply_by_2(r[2]) ^ multiply_by_3(r[3]),
        multiply_by_3(r[0]) ^ r[1] ^ r[2] ^ multiply_by_2(r[3]),
    ]


def inv_mix_column(r):
    """
    This function performs polynomial multiplication by 11x^3+13x^2+9x+14 (modulo x^4+1) with bytes in GF(2^8) as coefficient.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param r: a column composed of 4 bytes
    :return: the result of mix column as a column composed of 4 bytes
    """
    return [
        multiply_by_14(r[0]) ^ multiply_by_11(r[1]) ^ multiply_by_13(r[2]) ^ multiply_by_9(r[3]),
        multiply_by_9(r[0]) ^ multiply_by_14(r[1]) ^ multiply_by_11(r[2]) ^ multiply_by_13(r[3]),
        multiply_by_13(r[0]) ^ multiply_by_9(r[1]) ^ multiply_by_14(r[2]) ^ multiply_by_11(r[3]),
        multiply_by_11(r[0]) ^ multiply_by_13(r[1]) ^ multiply_by_9(r[2]) ^ multiply_by_14(r[3]),
    ]


def mix_columns(matrix):
    """
    This function performs the AES mix columns operation on each column of the matrix given as argument.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param matrix: a 4x4 bytes matrix
    :return: a 4x4 bytes matrix as the result of the mix columns operation
    """
    result = []
    for col in range(4):
        mixed = []
        for row in range(4):
            mixed.append(matrix[row][col])
        result.append(mixed)
    return result


def inv_mix_columns(matrix):
    """
    This function performs the inverted AES mix columns operation on each column of the matrix given as argument.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the operation details.
    :param matrix: a 4x4 bytes matrix
    :return: a 4x4 bytes matrix as the result of the inverted AES mix columns operation
    """
    result = []
    for col in range(4):
        mixed = []
        for row in range(4):
            mixed.append(matrix[row][col])
        result.append(mixed)
    return result


def aes_round(blockmatrix, key_matrix, substitution_box):
    """
    This function performs a round of the AES by executing all the steps in the prescribed order
    :param blockmatrix: block to encrypt as 4x4 bytes matrix
    :param key_matrix: AES key as a 4x4 bytes matrix
    :param substitution_box: the AES substitution box
    :return: the block to encrypt, after one round, as 4x4 bytes matrix
    """

    blockmatrix = sub_bytes(blockmatrix, substitution_box)
    blockmatrix = shift_rows(blockmatrix)
    blockmatrix = mix_columns(blockmatrix)
    blockmatrix = matrix_xor(blockmatrix, key_matrix)

    return blockmatrix


def aes_inverse_round(blockmatrix, key_matrix, inverse_substitution_box):
    """
    This function performs an inverse round of the AES by executing all the steps in the prescribed order
    :param blockmatrix: block to decrypt as 4x4 bytes matrix
    :param key_matrix: AES key as a 4x4 bytes matrix
    :param inverse_substitution_box: the inverted AES substitution box
    :return: the block to decrypt, after one unversed round, as 4x4 bytes matrix
    """

    blockmatrix = matrix_xor(blockmatrix, key_matrix)
    blockmatrix = inv_mix_columns(blockmatrix)
    blockmatrix = inv_shift_rows(blockmatrix)
    blockmatrix = sub_bytes(blockmatrix, inverse_substitution_box)

    return blockmatrix


def aes_final_round(blockmatrix, key_matrix, substitution_box):
    """
    This function performs the final round of the AES by executing all the steps in the prescribed order
    :param blockmatrix: block to encrypt as 4x4 bytes matrix
    :param key_matrix: AES key as a 4x4 bytes matrix
    :param substitution_box: the AES substitution box
    :return: the block to encrypt, after the final round, as 4x4 bytes matrix
    """

    blockmatrix = sub_bytes(blockmatrix, substitution_box)
    blockmatrix = shift_rows(blockmatrix)
    blockmatrix = matrix_xor(blockmatrix, key_matrix)

    return blockmatrix


def aes_inverse_final_round(blockmatrix, key_matrix, inverse_substitution_box):
    """
    This function performs the inverse final round of the AES by executing all the steps in the prescribed order
    :param blockmatrix: block to decrypt as 4x4 bytes matrix
    :param key_matrix: AES key as a 4x4 bytes matrix
    :param inverse_substitution_box: the inverted AES substitution box
    :return: the block to decrypt, after the inverse final round, as 4x4 bytes matrix
    """

    blockmatrix = matrix_xor(blockmatrix, key_matrix)
    blockmatrix = inv_shift_rows(blockmatrix)
    blockmatrix = sub_bytes(blockmatrix, inverse_substitution_box)

    return blockmatrix


def main():
    # Exemples de matrices 4x4
    blockmatrix = [
        [0x32, 0x88, 0x31, 0xe0],
        [0x43, 0x5a, 0x31, 0x37],
        [0xf6, 0x30, 0x98, 0x07],
        [0xa8, 0x8d, 0xa2, 0x34]
    ]

    key_matrix = [
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ]

    substitution_box = load_substitution_box()
    inverse_substitution_box_data = inverse_substitution_box(substitution_box)
    print()
    print("Original block matrix:")
    print(blockmatrix)

    # AES Round
    round_output = aes_round(blockmatrix, key_matrix, substitution_box)
    print()
    print("After AES round:")
    print(round_output)

    # AES Inverse Round
    inverse_round_output = aes_inverse_round(round_output, key_matrix, inverse_substitution_box_data)
    print()
    print("After AES inverse round:")
    print(inverse_round_output)

    # AES Final Round
    final_round_output = aes_final_round(blockmatrix, key_matrix, substitution_box)
    print()
    print("After AES final round:")
    print(final_round_output)

    # AES Inverse Final Round
    inverse_final_round_output = aes_inverse_final_round(final_round_output, key_matrix, inverse_substitution_box_data)
    print()
    print("After AES inverse final round:")
    print(inverse_final_round_output)


if __name__ == "__main__":
    main()
