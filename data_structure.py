def word128bits_to_bytes_matrix(word128bit):
    """
    This function splits the 128-bit word into bytes and places them in a 4x4 matrix.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the mapping.
    :param word128bit: the 128-bit word to convert into a byte matrix
    :return: a matrix consisting of the bytes of the 128-bit word received as argument
    """
    # Initialisation d'une matrice vide 4x4
    matrix = [[0] * 4 for _ in range(4)]

    for i in range(16):
        # Extraire chaque octet du mot 128 bits
        byte = (word128bit >> (120 - i * 8)) & 0xFF

        # Déterminer la position dans la matrice (colonne, ligne)
        row = i % 4
        col = i // 4

        # Placer l'octet dans la matrice
        matrix[row][col] = byte

    return matrix


def column_to_matrix(c0, c1, c2, c3):
    """
    This function splits the 32-bit words into bytes and places them in the corresponding column of a 4x4 matrix.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the mapping.
    :param c0: a 32-bit word as the first column of the output matrix
    :param c1: a 32-bit word as the second column of the output matrix
    :param c2: a 32-bit word as the third column of the output matrix
    :param c3: a 32-bit word as the fourth column of the output matrix
    :return: a matrix consisting of the 32-bit words as column
    """
    # Initialisation d'une matrice vide 4x4
    matrix = [[0] * 4 for _ in range(4)]

    for i, col in enumerate([c0, c1, c2, c3]):
        for j in range(4):
            # Extraire chaque octet de la colonne
            byte = (col >> (24 - j * 8)) & 0xFF

            # Placer l'octet dans la matrice
            matrix[j][i] = byte

    return matrix


def bytes_matrix_to_word128bits(matrix):
    """
    This function builds a 128-bit word that made up with of the bytes from the matrix.
    See the AES documentation referenced in the instructions and the HELMo Learn website for the mapping.
    :param matrix: the byte matrix to convert into a 128-bit word
    :return: a 128-bit word consisting of the bytes of the matrix received as argument
    """
    # Initialisation d'un mot 128 bits
    word128bit = 0

    for i in range(16):
        # Extraire chaque octet de la matrice
        byte = matrix[i % 4][i // 4]

        # Placer l'octet dans le mot 128 bits
        word128bit |= byte << (120 - i * 8)

    return word128bit


matrice = word128bits_to_bytes_matrix(int("00112233445566778899aabbccddeeff", 16))
for i in matrice:
    print(i)
