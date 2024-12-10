from data_structure import *
from aes_key_schedule import *
from roundfunction import *
from substitution import inverse_substitution_box, load_substitution_box


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
    AES encryption for a single block.
    :param block: 128-bit block to be encrypted
    :param key: 128/192/256 bits to encrypt the block
    :param aes_key_length: the number of bits as an integer value
    :return: the encrypted 128-bit block
    """
    substitution_box = load_substitution_box()
    round_keys = key_schedule(key, aes_key_length, substitution_box)
    num_rounds = compute_round_count(aes_key_length)

    # Convert block to matrix
    block_matrix = word128bits_to_bytes_matrix(block)

    # Initial XOR
    block_matrix = matrix_xor(block_matrix, column_to_matrix(*round_keys[:4]))

    # Execute rounds
    for round in range(1, num_rounds):
        round_key_matrix = column_to_matrix(*round_keys[round * 4:(round + 1) * 4])
        block_matrix = aes_round(block_matrix, round_key_matrix, substitution_box)

    # Final round
    final_key_matrix = column_to_matrix(*round_keys[num_rounds * 4:(num_rounds + 1) * 4])
    block_matrix = aes_final_round(block_matrix, final_key_matrix, substitution_box)

    # Convert matrix back to 128-bit word
    encrypted_block = bytes_matrix_to_word128bits(block_matrix)
    return encrypted_block


def aes_decrypt_block(block, key, aes_key_length):
    """
    AES decryption for a single block.
    :param block: the 128-bit cipher block to be decrypted
    :param key: 128/192/256 bits to decrypt the cipher block
    :param aes_key_length: the number of bits as an integer value
    :return: decrypted 128-bit block
    """
    substitution_box = load_substitution_box()
    inverse = inverse_substitution_box(substitution_box)
    round_keys = key_schedule(key, aes_key_length, substitution_box)
    num_rounds = compute_round_count(aes_key_length)

    # Convert block to matrix
    block_matrix = word128bits_to_bytes_matrix(block)

    # Final round (inverse final round)
    final_key_matrix = column_to_matrix(*round_keys[num_rounds * 4:(num_rounds + 1) * 4])
    block_matrix = aes_inverse_final_round(block_matrix, final_key_matrix, inverse)

    # Execute rounds in reverse order
    for round in range(num_rounds - 1, 0, -1):
        round_key_matrix = column_to_matrix(*round_keys[round * 4:(round + 1) * 4])
        block_matrix = aes_inverse_round(block_matrix, round_key_matrix, inverse)

    # Initial XOR
    initial_key_matrix = column_to_matrix(*round_keys[:4])
    block_matrix = matrix_xor(block_matrix, initial_key_matrix)

    # Convert matrix back to 128-bit word
    decrypted_block = bytes_matrix_to_word128bits(block_matrix)
    return decrypted_block
