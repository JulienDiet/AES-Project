from data_structure import word128bits_to_bytes_matrix, column_to_matrix, bytes_matrix_to_word128bits
from substitution import load_substitution_box, inverse_substitution_box
from aes_key_schedule import key_schedule
from roundfunction import aes_round, aes_final_round, aes_inverse_round, aes_inverse_final_round, matrix_xor


def compute_round_count(aes_key_length):
    """
    This function determines the number of AES rounds based on the key length.
    :param aes_key_length: the number of bits as an integer value
    :return: the number of AES rounds which depends on the key length
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
    AES encryption for a single block or a list of blocks.
    :param block: 128-bit block(s) to be encrypted (int or list of ints)
    :param key: 128/192/256 bits to encrypt the block
    :param aes_key_length: the number of bits as an integer value
    :return: the encrypted 128-bit block(s)
    """
    encrypted_blocks = []
    if isinstance(block, int):
        block = [block]

    substitution_box = load_substitution_box()
    round_keys = key_schedule(key, aes_key_length, substitution_box)
    num_rounds = compute_round_count(aes_key_length)

    for single_block in block:
        block_matrix = word128bits_to_bytes_matrix(single_block)
        round_key_matrices = [column_to_matrix(round_keys[i], round_keys[i + 1], round_keys[i + 2], round_keys[i + 3])
                              for i in range(0, len(round_keys), 4)]

        # Initial XOR
        block_matrix = matrix_xor(block_matrix, round_key_matrices[0])

        # Execute rounds
        for i in range(1, num_rounds):
            block_matrix = aes_round(block_matrix, round_key_matrices[i], substitution_box)

        # Final round
        block_matrix = aes_final_round(block_matrix, round_key_matrices[num_rounds], substitution_box)

        # Convert matrix back to 128-bit word
        encrypted_blocks.append(bytes_matrix_to_word128bits(block_matrix))

    return encrypted_blocks


def aes_decrypt_block(block, key, aes_key_length):
    """
    AES decryption for a single block or a list of blocks.
    :param block: the 128-bit cipher block(s) to be decrypted (int or list of ints)
    :param key: 128/192/256 bits to decrypt the cipher block
    :param aes_key_length: the number of bits as an integer value
    :return: decrypted 128-bit block(s)
    """
    decrypted_blocks = []
    if isinstance(block, int):
        block = [block]

    substitution_box = load_substitution_box()
    inverse_sub_box = inverse_substitution_box(substitution_box)
    round_keys = key_schedule(key, aes_key_length, substitution_box)
    num_rounds = compute_round_count(aes_key_length)

    for single_block in block:
        block_matrix = word128bits_to_bytes_matrix(single_block)
        round_key_matrices = [column_to_matrix(round_keys[i], round_keys[i + 1], round_keys[i + 2], round_keys[i + 3])
                              for i in range(0, len(round_keys), 4)]

        # Initial XOR
        block_matrix = matrix_xor(block_matrix, round_key_matrices[num_rounds])

        # Execute rounds
        for i in range(num_rounds - 1, 0, -1):
            block_matrix = aes_inverse_round(block_matrix, round_key_matrices[i], inverse_sub_box)

        # Final round
        block_matrix = aes_inverse_final_round(block_matrix, round_key_matrices[0], inverse_sub_box)

        # Convert matrix back to 128-bit word
        decrypted_blocks.append(bytes_matrix_to_word128bits(block_matrix))

    return decrypted_blocks
