def rdm_iv_generator():
    """
    This function must be able to generate a 128-bit random number
    :return: a randomly generated 128-bit integer.
    """


def rdm_iv_generator_with_counter():
    """
    This function must be able to generate a random number from 96 random most significant bits,
    leaving the least significant bits at zero for the counter.
    :return: a randomly generated 128-bit integer.
    """


def encrypt_ecb(blocks, key, security):
    """
     This function applies AES encryption to a list of 128-bit blocks using the ECB operating mode.
    :param blocks: List of blocks (128bits) to be encrypted.
    :param key: 128/192/256-bit encryption key.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of encrypted blocks.
    """


def decrypt_ecb(blocks, key, security):
    """
    This function decrypts a list of 128-bit blocks which have been previously encrypted
    with AES using the ECB mode of operation.
    :param blocks: List of blocks to be decrypted.
    :param key: 128/192/256-bit encryption key, identical to that used for encryption.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of decrypted blocks.
    """

def encrypt_cbc(blocks, key, security):
    """
    This function applies AES encryption to a list of 128-bit blocks using the CBC operating mode.
    :param blocks: List of blocks (128bits) to be encrypted.
    :param key: 128/192/256-bit encryption key.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of encrypted blocks.
    """

def decrypt_cbc(blocks, key, security):
    """
    This function decrypts a list of 128-bit blocks which have been previously encrypted
    with AES using the CBC mode of operation.
    :param blocks: List of blocks to be decrypted.
    :param key: 128/192/256-bit encryption key, identical to that used for encryption.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of decrypted blocks.
    """

def encrypt_pcbc(blocks, key, security):
    """
     This function applies AES encryption to a list of 128-bit blocks using the PCBC operating mode.
    :param blocks: List of blocks (128bits) to be encrypted.
    :param key: 128/192/256-bit encryption key.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of encrypted blocks.
    """

def decrypt_pcbc(blocks, key, security):
    """
    This function decrypts a list of 128-bit blocks which have been previously encrypted
    with AES using the PCBC mode of operation.
    :param blocks: List of blocks to be decrypted.
    :param key: 128/192/256-bit encryption key, identical to that used for encryption.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of decrypted blocks.
    """
def decrypt(blocks, key, security, operation_mode="ECB"):
    """
    This function decrypts a list of 128-bit blocks which have been previously encrypted
    with AES according to the mode of operation given as an argument.
    :param blocks: List of blocks to be decrypted.
    :param key: 128/192/256-bit encryption key, identical to that used for encryption.
    :param security: the security AES level which corresponds to the key length as an integer value
    :param operation_mode: string specifying the operation mode (‘ECB’ or ‘CBC’).
    :return: the list of decrypted blocks.
    """

def encrypt(blocks, key, security, operation_mode="ECB"):
    """
    This function encrypts a list of 128-bit blocks
    with AES according to the mode of operation given as an argument.
    :param blocks: List of blocks to be decrypted.
    :param key: the 128/192/256-bit encryption key.
    :param security: the security AES level which corresponds to the key length as an integer value
    :param operation_mode: string specifying the operation mode ("ECB", "CBC", "PCBC").
    :return: the list of encrypted blocks.
    """
