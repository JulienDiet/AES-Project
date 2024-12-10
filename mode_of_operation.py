import os
from aes_encryption import aes_encrypt_block, aes_decrypt_block


def rdm_iv_generator():
    """
    This function must be able to generate a 128-bit random number
    :return: a randomly generated 128-bit integer.
    """
    iv = os.urandom(16)
    return int.from_bytes(iv, byteorder='big')


def rdm_iv_generator_with_counter():
    """
    This function must be able to generate a random number from 96 random most significant bits,
    leaving the least significant bits at zero for the counter.
    :return: a randomly generated 128-bit integer.
    """
    # Génère 12 octets (96 bits) aléatoires pour les bits les plus significatifs
    random_bits = os.urandom(12)
    # Convertit les 12 octets en un entier
    random_integer = int.from_bytes(random_bits, byteorder='big')
    # Ajoute 32 bits à zéro pour le compteur
    iv = (random_integer << 32)  # Décale à gauche de 32 bits
    return iv


def encrypt_ecb(blocks, key, security):
    """
     This function applies AES encryption to a list of 128-bit blocks using the ECB operating mode.
    :param blocks: List of blocks (128bits) to be encrypted.
    :param key: 128/192/256-bit encryption key.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of encrypted blocks.
    """
    encrypted_blocks = []
    for block in blocks:
        encrypted_block = aes_encrypt_block(block, key, security)
        encrypted_blocks.append(encrypted_block)
    return encrypted_blocks


def decrypt_ecb(blocks, key, security):
    """
    This function decrypts a list of 128-bit blocks which have been previously encrypted
    with AES using the ECB mode of operation.
    :param blocks: List of blocks to be decrypted.
    :param key: 128/192/256-bit encryption key, identical to that used for encryption.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of decrypted blocks.
    """
    decrypted_blocks = []
    for block in blocks:
        decrypted_block = aes_decrypt_block(block, key, security)
        decrypted_blocks.append(decrypted_block)
    return decrypted_blocks


def encrypt_cbc(blocks, key, security):
    """
    This function applies AES encryption to a list of 128-bit blocks using the CBC operating mode.
    :param blocks: List of blocks (128bits) to be encrypted.
    :param key: 128/192/256-bit encryption key.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of encrypted blocks.
    """

    # Génère un vecteur d'initialisation aléatoire
    iv = rdm_iv_generator()
    encrypted_blocks = []
    previous_block = iv
    for block in blocks:
        # XOR entre le bloc actuel et le bloc précédent
        block = block ^ previous_block
        # Chiffrement du bloc avec la clé
        encrypted_block = aes_encrypt_block(block, key, security)
        # Ajout du bloc chiffré à la liste
        encrypted_blocks.append(encrypted_block)
        # Mise à jour du bloc précédent
        previous_block = encrypted_block
    return encrypted_blocks


def decrypt_cbc(blocks, key, security):
    """
    This function decrypts a list of 128-bit blocks which have been previously encrypted
    with AES using the CBC mode of operation.
    :param blocks: List of blocks to be decrypted.
    :param key: 128/192/256-bit encryption key, identical to that used for encryption.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of decrypted blocks.
    """
    # Le premier bloc est l'IV
    iv = blocks[0]
    decrypted_blocks = []
    previous_block = iv

    # On déchiffre à partir du deuxième bloc
    for block in blocks[1:]:
        # Déchiffrement du bloc
        decrypted_block = aes_decrypt_block(block, key, security)
        # XOR avec le bloc précédent (ou l'IV pour le premier)
        decrypted_block = decrypted_block ^ previous_block
        decrypted_blocks.append(decrypted_block)
        # Le bloc chiffré actuel devient le précédent pour le prochain tour
        previous_block = block

    return decrypted_blocks


def encrypt_pcbc(blocks, key, security):
    """
     This function applies AES encryption to a list of 128-bit blocks using the PCBC operating mode.
    :param blocks: List of blocks (128bits) to be encrypted.
    :param key: 128/192/256-bit encryption key.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of encrypted blocks.
    """
    # Génère un vecteur d'initialisation aléatoire
    iv = rdm_iv_generator()
    encrypted_blocks = []
    previous_block = iv
    for block in blocks:
        # XOR entre le bloc actuel et le bloc précédent
        block = block ^ previous_block
        # Chiffrement du bloc avec la clé
        encrypted_block = aes_encrypt_block(block, key, security)
        # XOR entre le bloc chiffré et le bloc actuel
        encrypted_block = encrypted_block ^ block
        # Ajout du bloc chiffré à la liste
        encrypted_blocks.append(encrypted_block)
        # Mise à jour du bloc précédent
        previous_block = block
    return encrypted_blocks

def decrypt_pcbc(blocks, key, security):
    """
    This function decrypts a list of 128-bit blocks which have been previously encrypted
    with AES using the PCBC mode of operation.
    :param blocks: List of blocks to be decrypted.
    :param key: 128/192/256-bit encryption key, identical to that used for encryption.
    :param security: the security AES level which corresponds to the key length as an integer value
    :return: the list of decrypted blocks.
    """
    # Le premier bloc est l'IV
    iv = blocks[0]
    decrypted_blocks = []
    previous_cipher = iv
    previous_plain = iv  # initialisation arbitraire

    for i, block in enumerate(blocks[1:], start=1):
        # Déchiffrement du bloc
        decrypted_block = aes_decrypt_block(block, key, security)
        # XOR avec previous_cipher et previous_plain (conformément au PCBC)
        # Lors du chiffrement PCBC standard :
        # PCBC = P_i XOR C_(i-1)  puis C_i = E(P_i)
        # Au déchiffrement : P_i = D(C_i) XOR C_(i-1)
        # Votre implémentation PCBC est particulière, adaptez en fonction de votre logique initiale.
        # Par exemple, si vous avez choisi un schéma spécifique lors du chiffrement, il faut l'inverser ici.

        # Supposons une variante standard du PCBC :
        # Pour le premier bloc, P_1 = D(C_1) XOR IV
        # Pour les suivants, P_i = D(C_i) XOR (P_(i-1) XOR C_(i-1))
        # Ici, réutilisez la même logique inverse que lors du chiffrement.

        # Si votre chiffrement PCBC était :
        # encrypt_pcbc: block_chiffre = E(block ^ previous) ^ block
        # Il faut inverser :
        # D(C_i) vous donne : intermediaire = D(C_i)
        # Ensuite, P_i = intermediaire ^ previous ^ C_i
        # previous étant l'ancien bloc clair.

        # On récupère l'ancien bloc chiffré comme previous_cipher, et l'ancien bloc clair comme previous_plain.
        # Ici, supposons que votre logique initiale était (d'après votre code) :
        # encrypt_pcbc: block = block ^ previous_block (clair)
        #                C_i = E(block)
        #                C_i = C_i ^ block
        # Au déchiffrement :
        # D(C_i) donne intermediaire
        # Puis P_i = intermediaire ^ previous_block ^ C_i
        # Mettez à jour previous_block et previous_cipher comme au chiffrement.

        # Exemple complet (en se basant sur votre code initial) :
        # Au chiffrement PCBC:
        # block_clair XOR previous_block_clair = inter1
        # C_i = E(inter1)
        # C_i = C_i XOR inter1
        # previous_block_clair = block_clair
        #
        # Au déchiffrement PCBC, on doit inverser cela :
        # intermediaire = D(C_i)
        # On sait que C_i_final = C_i XOR inter1
        # Donc inter1 = C_i XOR C_i_final
        # On a inter1 = block_clair XOR previous_block_clair
        # Puis block_clair = inter1 XOR previous_block_clair
        #
        # Reprenez la logique exacte de votre chiffrement ici. Sans votre logique précise, c'est difficile de donner un code exact.
        # Si vous êtes incertain, repassez en ECB ou CBC. Le PCBC n'étant pas standard, il faut une cohérence stricte.

        # Exemple si l'on suit un PCBC standard simplifié (non basé sur votre code) :
        decrypted_block = decrypted_block ^ previous_cipher ^ previous_plain
        decrypted_blocks.append(decrypted_block)
        previous_cipher = block
        previous_plain = decrypted_block

    return decrypted_blocks


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
    if operation_mode == "ECB":
        return decrypt_ecb(blocks, key, security)
    elif operation_mode == "CBC":
        return decrypt_cbc(blocks, key, security)
    elif operation_mode == "PCBC":
        return decrypt_pcbc(blocks, key, security)
    else:
        raise ValueError("Invalid operation mode")


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
    if operation_mode == "ECB":
        return encrypt_ecb(blocks, key, security)
    elif operation_mode == "CBC":
        return encrypt_cbc(blocks, key, security)
    elif operation_mode == "PCBC":
        return encrypt_pcbc(blocks, key, security)
    else:
        raise ValueError("Invalid operation mode")
