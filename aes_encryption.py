from data_structure import *
from aes_key_schedule import *
from roundfunction import *
from substitution import inverse_substitution_box, load_substitutionBox


def compute_round_count(aes_key_length):
    """
    Cette fonction détermine le nombre de tours AES en fonction de la longueur de la clé.
    :param aes_key_length: le nombre de bits sous forme d'entier
    :return: le nombre de tours AES qui dépend de la longueur de la clé
    """

    if aes_key_length == 128:
        return 10
    elif aes_key_length == 192:
        return 12
    elif aes_key_length == 256:
        return 14
    else:
        raise ValueError("The key length must be 128, 192 or 256 bits.")


def aes_encrypt_block(block, key, aes_key_length):
    """
    Chiffrement AES pour un bloc unique.
    :param block: bloc de 128 bits à chiffrer
    :param key: clé de 128/192/256 bits pour chiffrer le bloc
    :param aes_key_length: le nombre de bits sous forme d'entier
    :return: le bloc chiffré de 128 bits
    """

    substitution_box = load_substitutionBox()
    round_keys = key_schedule(key, aes_key_length, substitution_box)
    num_rounds = compute_round_count(aes_key_length)

    block_matrix = word128bits_to_bytes_matrix(block)

    block_matrix = matrix_xor(block_matrix, column_to_matrix(*round_keys[:4]))

    for round in range(1, num_rounds):
        round_key_matrix = column_to_matrix(*round_keys[round * 4:(round + 1) * 4])
        block_matrix = aes_round(block_matrix, round_key_matrix, substitution_box)

    final_key_matrix = column_to_matrix(*round_keys[num_rounds * 4:(num_rounds + 1) * 4])
    block_matrix = aes_final_round(block_matrix, final_key_matrix, substitution_box)

    encrypted_block = bytes_matrix_to_word128bits(block_matrix)
    return encrypted_block


def aes_decrypt_block(block, key, aes_key_length):
    """
    Déchiffrement AES pour un bloc unique.
    :param block: le bloc chiffré de 128 bits à déchiffrer
    :param key: clé de 128/192/256 bits pour déchiffrer le bloc chiffré
    :param aes_key_length: le nombre de bits sous forme d'entier
    :return: le bloc déchiffré de 128 bits
    """

    substitution_box = load_substitutionBox()
    inverse = inverse_substitution_box(substitution_box)
    round_keys = key_schedule(key, aes_key_length, substitution_box)
    num_rounds = compute_round_count(aes_key_length)

    block_matrix = word128bits_to_bytes_matrix(block)

    final_key_matrix = column_to_matrix(*round_keys[num_rounds * 4:(num_rounds + 1) * 4])
    block_matrix = aes_inverse_final_round(block_matrix, final_key_matrix, inverse)

    for round in range(num_rounds - 1, 0, -1):
        round_key_matrix = column_to_matrix(*round_keys[round * 4:(round + 1) * 4])
        block_matrix = aes_inverse_round(block_matrix, round_key_matrix, inverse)

    initial_key_matrix = column_to_matrix(*round_keys[:4])
    block_matrix = matrix_xor(block_matrix, initial_key_matrix)

    decrypted_block = bytes_matrix_to_word128bits(block_matrix)
    return decrypted_block
