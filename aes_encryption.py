
def compute_round_count(aes_key_length):
    """
    This function makes the connection between the length of AES key and the number of AES rounds.
    :param aes_key_length: the number of bits as an integer value
    :return: the number of AES rounds which depends on the key length
    """


def aes_encrypt_block(block, key, aes_key_length):
    """
    This function
    (i) load the substitution box, build the round keys and get the number of rounds.
    (ii) format the block and round key data as a matrix
    (iii) perform the initial XOR
    (iv) execute the rounds
    (v) execute the final round
    :param block: 128-bit block to be encrypted
    :param key: 128/192/256 bits to encrypt the block
    :param aes_key_length: the number of bits as an integer value
    :return: the encrypted 128-bit block
    """


def aes_decrypt_block(block, key, aes_key_length):
    """
    This function
    (i) load the substitution box and invert it, build round keys and get the number of rounds.
    (ii) format the block and round key data as a matrix
    (iii) perform the initial XOR
    (iv) execute the rounds
    (v) execute the final round
    :param block: the 128-bit cipher block to be decrypted
    :param key: 128/192/256 bits to decrypt the cipher block
    :param aes_key_length: the number of bits as an integer value
    :return: decrypted 128 bit block
    """
