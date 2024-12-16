def load_substitutionBox():
    """
    Cette fonction charge les valeurs du fichier "data.txt" et les place dans une matrice 16x16.
    :return: une matrice 16x16 correspondant à la boîte de substitution AES
    """
    substitution_box = []

    with open("data.txt", "r") as file:
        for line in file:
            row = [int(value, 16) for value in line.split()]
            substitution_box.append(row)

    return substitution_box


def inverse_substitution_box(substitution_box):
    """
    Cette fonction construit la boîte de substitution inverse d'AES à partir de la boîte de substitution AES.
    :param substitution_box: la boîte de substitution AES sous forme de matrice 16x16
    :return: la boîte de substitution inverse d'AES sous forme de matrice 16x16
    """
    inverse_box = [[0] * 16 for _ in range(16)]

    for row in range(16):
        for col in range(16):
            value = substitution_box[row][col]
            inverse_box[value >> 4][value & 0x0F] = (row << 4) | col
    return inverse_box


def substitution(box, value):
    """
    Cette fonction exécute la substitution.
    :param box: la boîte de substitution
    :param value: la valeur à substituer
    :return: la valeur de sortie provenant de la boîte de substitution correspondant à la valeur d'entrée
    """
    row = value >> 4
    col = value & 0x0F
    return box[row][col]
