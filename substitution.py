def load_substitution_box():
    """
    This function loads the values from the "data.txt" file and places them in a 16x16 matrix
    :return: a 16x16 matrix corresponding to the AES substitution box
    """
    substitution_box = []

    with open("data.txt", "r") as file:
        for line in file:
            row = [int(value, 16) for value in line.split()]
            substitution_box.append(row)

    return substitution_box


def inverse_substitution_box(substitution_box):
    """
    This function builds the AES inverse substitution box based on the AES substitution box
    :param substitution_box: the AES substitution box as a 16x16 matrix
    :return: the inverse AES substitution box as a 16x16 matrix
    """
    inverse_box = [[0] * 16 for _ in range(16)]

    for row in range(16):
        for col in range(16):
            value = substitution_box[row][col]
            inverse_box[value >> 4][value & 0x0F] = (row << 4) | col
    return inverse_box


def substitution(box, value):
    """
    This function executes the substitution.
    :param box: the substitution box
    :param value: the value to be substituted
    :return: the output value from the substitution box corresponding to the input value
    """
    row = value >> 4
    col = value & 0x0F
    return box[row][col]
