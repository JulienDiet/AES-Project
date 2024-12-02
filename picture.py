import os

import numpy as np
from PIL import Image
from numpy import asarray

from mode_of_operation import encrypt, decrypt

iv_dict = dict()


def image_from_file_to_bytes(path):
    image = Image.open(path)
    # summarize some details about the image
    # print(image.format)
    # print(image.size)
    # print(image.mode)
    # asarray() class is used to convert
    # PIL images into NumPy arrays
    numpy_data = asarray(image)
    # <class 'numpy.ndarray'>
    # print(type(numpydata))
    #  shape
    buffer = numpy_data.data
    # (x, y, z) = buffer.shape
    # if (x * y * z * 8) % 128 != 0:
    #    print("Your picture must have size as multiple of 128")
    #    exit(-1)
    # print(buffer.tobytes())
    return buffer.tobytes(), buffer.shape


def image_from_bytes_to_file(img_bytes, img_shape, path):
    numpy_cipher_data = np.reshape(np.frombuffer(img_bytes, dtype=np.uint8), newshape=img_shape)
    Image.fromarray(numpy_cipher_data).save(path)


def bytes_to_block128(data_bytes):
    blocks = []
    i = 15
    block = 0
    for pixel in data_bytes:
        # print(i, "{:08b}".format(pixel))
        block |= pixel << 8 * i
        i -= 1
        if i < 0:
            blocks.append(block)
            i = 15
            block = 0
    return blocks


def block128_to_bytes(blocks):
    data_bytes = bytes()
    for block in blocks:
        data_bytes += block.to_bytes(16, 'big')
    return data_bytes


def encrypt_bytes(data_bytes, k, security, operation_mode="ECB"):
    data_blocks = bytes_to_block128(data_bytes)
    cipher_blocks = encrypt(data_blocks, k, security, operation_mode)
    return block128_to_bytes(cipher_blocks)


def decrypt_bytes(cipher_bytes, k, security, operation_mode="ECB"):
    cipher_blocks = bytes_to_block128(cipher_bytes)
    data_blocks = decrypt(cipher_blocks, k, security, operation_mode)
    return block128_to_bytes(data_blocks)


def encrypt_image(path, key, security, operation_mode="ECB"):
    image_bytes, img_shape = image_from_file_to_bytes(path)
    #print(img_shape)
    cipher_bytes = encrypt_bytes(image_bytes, key, security, operation_mode)

    filename = os.path.basename(path)
    directory = os.path.dirname(path) + '\\..\\Encrypted'

    if not operation_mode == "ECB":
        iv_dict[filename] = cipher_bytes[:16]
        cipher_bytes = cipher_bytes[16:]

    image_from_bytes_to_file(cipher_bytes, img_shape, os.path.join(directory, filename))


def decrypt_image(path, key, security, operation_mode="ECB"):
    filename = os.path.basename(path)
    directory = os.path.dirname(path) + '\\..\\Decrypted'

    cipher_bytes, img_shape = image_from_file_to_bytes(path)
    if not operation_mode == "ECB":
        cipher_bytes = iv_dict[filename] + cipher_bytes

    image_bytes = decrypt_bytes(cipher_bytes, key, security, operation_mode)

    image_from_bytes_to_file(image_bytes, img_shape, os.path.join(directory, filename))
