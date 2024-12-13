def word128bits_to_bytes_matrix(word128bit):
    """
    Cette fonction divise un mot de 128 bits en octets et les place dans une matrice 4x4.
    Voir la documentation AES référencée dans les instructions et le site HELMo Learn pour le mapping.
    :param word128bit: le mot de 128 bits à convertir en matrice d'octets
    :return: une matrice contenant les octets du mot de 128 bits reçu en argument
    """
    matrix = [[0] * 4 for _ in range(4)]

    for i in range(16):
        byte = (word128bit >> (120 - i * 8)) & 0xFF
        row = i % 4
        col = i // 4
        matrix[row][col] = byte
    return matrix


def column_to_matrix(c0, c1, c2, c3):
    """
    Cette fonction divise les mots de 32 bits en octets et les place dans la colonne correspondante d'une
    matrice 4x4.
    Voir la documentation AES référencée dans les instructions et le site HELMo Learn pour le mapping.
    :param c0: un mot de 32 bits représentant la première colonne de la matrice de sortie
    :param c1: un mot de 32 bits représentant la deuxième colonne de la matrice de sortie
    :param c2: un mot de 32 bits représentant la troisième colonne de la matrice de sortie
    :param c3: un mot de 32 bits représentant la quatrième colonne de la matrice de sortie
    :return: une matrice constituée des mots de 32 bits disposés en colonnes
    """
    matrix = [[0] * 4 for _ in range(4)]

    for i, col in enumerate([c0, c1, c2, c3]):
        for j in range(4):
            byte = (col >> (24 - j * 8)) & 0xFF
            matrix[j][i] = byte
    return matrix


def bytes_matrix_to_word128bits(matrix):
    """
    Cette fonction construit un mot de 128 bits à partir des octets contenus dans une matrice.
    Voir la documentation AES référencée dans les instructions et le site HELMo Learn pour le mapping.
    :param matrix: la matrice d'octets à convertir en un mot de 128 bits
    :return: un mot de 128 bits constitué des octets de la matrice reçue en argument
    """
    word128bit = 0

    for i in range(16):
        byte = matrix[i % 4][i // 4]
        word128bit |= byte << (120 - i * 8)
    return word128bit
