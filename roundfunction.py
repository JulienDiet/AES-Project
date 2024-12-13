from gf256_multiplication import *


def matrix_xor(matrix, key):
    """
    Cette fonction effectue une opération XOR sur les octets des matrices données en arguments.
    :param matrix: une matrice de 4x4 octets
    :param key: une matrice de 4x4 octets
    :return: une matrice de 4x4 octets contenant le résultat du XOR entre les octets correspondants
             des matrices reçues en arguments
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
    Cette fonction effectue la substitution des octets de la matrice donnée en argument.
    :param matrix: une matrice de 4x4 octets
    :param substitution_box: la boîte de substitution AES
    :return: une matrice de 4x4 octets contenant les octets substitués de la matrice donnée en argument.
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
    Cette fonction effectue l'opération de décalage des lignes (shift rows) d'AES sur la matrice donnée en argument.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour les détails de
    l'opération.
    :param matrix: une matrice de 4x4 octets
    """
    return [
        matrix[0],
        matrix[1][1:] + matrix[1][:1],
        matrix[2][2:] + matrix[2][:2],
        matrix[3][3:] + matrix[3][:3]
    ]


def inv_shift_rows(matrix):
    """
    Cette fonction effectue l'opération inverse de décalage des lignes (shift rows) d'AES sur la matrice
    donnée en argument.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour les détails
    de l'opération.
    :param matrix: une matrice de 4x4 octets
    """
    return [
        matrix[0],
        matrix[1][-1:] + matrix[1][:-1],
        matrix[2][-2:] + matrix[2][:-2],
        matrix[3][-3:] + matrix[3][:-3]
    ]


def mix_column(r):
    """
    Cette fonction effectue la multiplication polynomiale 3x^3+x^2+x+2 (modulo x^4+1) avec des octets dans
    GF(2^8) comme coefficients.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour les détails
    de l'opération.
    :param r: une colonne composée de 4 octets
    :return: le résultat de l'opération mix column sous forme de colonne composée de 4 octets
    """
    return [
        multiply_by_2(r[0]) ^ multiply_by_3(r[1]) ^ r[2] ^ r[3],
        r[0] ^ multiply_by_2(r[1]) ^ multiply_by_3(r[2]) ^ r[3],
        r[0] ^ r[1] ^ multiply_by_2(r[2]) ^ multiply_by_3(r[3]),
        multiply_by_3(r[0]) ^ r[1] ^ r[2] ^ multiply_by_2(r[3]),
    ]


def inv_mix_column(r):
    """
    Cette fonction effectue la multiplication polynomiale par 11x^3+13x^2+9x+14 (modulo x^4+1) avec des
    octets dans GF(2^8) comme coefficients.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour les détails
     de l'opération.
    :param r: une colonne composée de 4 octets
    :return: le résultat de l'opération mix column sous forme de colonne composée de 4 octets
    """

    return [
        multiply_by_14(r[0]) ^ multiply_by_11(r[1]) ^ multiply_by_13(r[2]) ^ multiply_by_9(r[3]),
        multiply_by_9(r[0]) ^ multiply_by_14(r[1]) ^ multiply_by_11(r[2]) ^ multiply_by_13(r[3]),
        multiply_by_13(r[0]) ^ multiply_by_9(r[1]) ^ multiply_by_14(r[2]) ^ multiply_by_11(r[3]),
        multiply_by_11(r[0]) ^ multiply_by_13(r[1]) ^ multiply_by_9(r[2]) ^ multiply_by_14(r[3]),
    ]


def mix_columns(matrix):
    """
    Cette fonction effectue l'opération mix columns d'AES sur chaque colonne de la matrice donnée en
    argument.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour les détails
    de l'opération.
    :param matrix: une matrice de 4x4 octets
    :return: une matrice de 4x4 octets résultant de l'opération mix columns
    """
    for c in range(4):
        col = [matrix[r][c] for r in range(4)]
        mixed_col = mix_column(col)
        for r in range(4):
            matrix[r][c] = mixed_col[r]
    return matrix


def inv_mix_columns(matrix):
    """
    Cette fonction effectue l'opération inverse de mix columns d'AES sur chaque colonne de la matrice donnée
    en argument.
    Consultez la documentation AES référencée dans les instructions et le site HELMo Learn pour les détails
    de l'opération.
    :param matrix: une matrice de 4x4 octets
    :return: une matrice de 4x4 octets résultant de l'opération inverse de mix columns d'AES
    """
    for c in range(4):
        col = [matrix[r][c] for r in range(4)]
        mixed_col = inv_mix_column(col)
        for r in range(4):
            matrix[r][c] = mixed_col[r]
    return matrix


def aes_round(blockmatrix, key_matrix, substitution_box):
    """
    Cette fonction exécute un tour d'AES en réalisant toutes les étapes dans l'ordre prescrit.
    :param blockmatrix: bloc à chiffrer sous forme de matrice de 4x4 octets
    :param key_matrix: clé AES sous forme de matrice de 4x4 octets
    :param substitution_box: la boîte de substitution AES
    :return: le bloc à chiffrer, après un tour, sous forme de matrice de 4x4 octets
    """

    blockmatrix = sub_bytes(blockmatrix, substitution_box)
    blockmatrix = shift_rows(blockmatrix)
    blockmatrix = mix_columns(blockmatrix)
    blockmatrix = matrix_xor(blockmatrix, key_matrix)

    return blockmatrix


def aes_inverse_round(blockmatrix, key_matrix, inverse_substitution_box):
    """
    Cette fonction exécute un tour inverse d'AES en réalisant toutes les étapes dans l'ordre prescrit.
    :param blockmatrix: bloc à déchiffrer sous forme de matrice de 4x4 octets
    :param key_matrix: clé AES sous forme de matrice de 4x4 octets
    :param inverse_substitution_box: la boîte de substitution inverse d'AES
    :return: le bloc à déchiffrer, après un tour inverse, sous forme de matrice de 4x4 octets
    """

    blockmatrix = matrix_xor(blockmatrix, key_matrix)
    blockmatrix = inv_mix_columns(blockmatrix)
    blockmatrix = inv_shift_rows(blockmatrix)
    blockmatrix = sub_bytes(blockmatrix, inverse_substitution_box)

    return blockmatrix


def aes_final_round(blockmatrix, key_matrix, substitution_box):
    """
    Cette fonction exécute le dernier tour d'AES en réalisant toutes les étapes dans l'ordre prescrit.
    :param blockmatrix: bloc à chiffrer sous forme de matrice de 4x4 octets
    :param key_matrix: clé AES sous forme de matrice de 4x4 octets
    :param substitution_box: la boîte de substitution AES
    :return: le bloc à chiffrer, après le dernier tour, sous forme de matrice de 4x4 octets
    """
    blockmatrix = sub_bytes(blockmatrix, substitution_box)
    blockmatrix = shift_rows(blockmatrix)
    blockmatrix = matrix_xor(blockmatrix, key_matrix)

    return blockmatrix


def aes_inverse_final_round(blockmatrix, key_matrix, inverse_substitution_box):
    """
    Cette fonction exécute le dernier tour inverse d'AES en réalisant toutes les étapes dans l'ordre
    prescrit.
    :param blockmatrix: bloc à déchiffrer sous forme de matrice de 4x4 octets
    :param key_matrix: clé AES sous forme de matrice de 4x4 octets
    :param inverse_substitution_box: la boîte de substitution inverse d'AES
    :return: le bloc à déchiffrer, après le dernier tour inverse, sous forme de matrice de 4x4 octets
    """
    blockmatrix = matrix_xor(blockmatrix, key_matrix)
    blockmatrix = inv_shift_rows(blockmatrix)
    blockmatrix = sub_bytes(blockmatrix, inverse_substitution_box)

    return blockmatrix
