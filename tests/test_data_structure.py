import random
import unittest

from data_structure import word128bits_to_bytes_matrix, column_to_matrix, bytes_matrix_to_word128bits


class TestEvaluation(unittest.TestCase):

    def test_word128bits_to_bytes_matrix(self):
        expected_bytes = [0 for _ in range(17)]
        word128bit = 0
        shift = 120
        for i in range(16):
            expected_bytes[i] = random.randint(0, 255)
            word128bit |= expected_bytes[i] << shift
            shift -= 8

        bytes_matrix = word128bits_to_bytes_matrix(word128bit)

        assert bytes_matrix[0][0] == expected_bytes[0]
        assert bytes_matrix[1][0] == expected_bytes[1]
        assert bytes_matrix[2][0] == expected_bytes[2]
        assert bytes_matrix[3][0] == expected_bytes[3]

        assert bytes_matrix[0][1] == expected_bytes[4]
        assert bytes_matrix[1][1] == expected_bytes[5]
        assert bytes_matrix[2][1] == expected_bytes[6]
        assert bytes_matrix[3][1] == expected_bytes[7]

        assert bytes_matrix[0][2] == expected_bytes[8]
        assert bytes_matrix[1][2] == expected_bytes[9]
        assert bytes_matrix[2][2] == expected_bytes[10]
        assert bytes_matrix[3][2] == expected_bytes[11]

        assert bytes_matrix[0][3] == expected_bytes[12]
        assert bytes_matrix[1][3] == expected_bytes[13]
        assert bytes_matrix[2][3] == expected_bytes[14]
        assert bytes_matrix[3][3] == expected_bytes[15]


    def test_column_to_matrix(self):
        expected_bytes = [0 for _ in range(17)]
        shift = 120
        for i in range(16):
            expected_bytes[i] = random.randint(0, 255)
            shift -= 8

        c1 = expected_bytes[0] << 24 | expected_bytes[1] << 16 | expected_bytes[2] << 8 | expected_bytes[3]
        c2 = expected_bytes[4] << 24 | expected_bytes[5] << 16 | expected_bytes[6] << 8 | expected_bytes[7]
        c3 = expected_bytes[8] << 24 | expected_bytes[9] << 16 | expected_bytes[10] << 8 | expected_bytes[11]
        c4 = expected_bytes[12] << 24 | expected_bytes[13] << 16 | expected_bytes[14] << 8 | expected_bytes[15]

        bytes_matrix = column_to_matrix(c1, c2, c3, c4)

        assert bytes_matrix[0][0] == expected_bytes[0]
        assert bytes_matrix[1][0] == expected_bytes[1]
        assert bytes_matrix[2][0] == expected_bytes[2]
        assert bytes_matrix[3][0] == expected_bytes[3]

        assert bytes_matrix[0][1] == expected_bytes[4]
        assert bytes_matrix[1][1] == expected_bytes[5]
        assert bytes_matrix[2][1] == expected_bytes[6]
        assert bytes_matrix[3][1] == expected_bytes[7]

        assert bytes_matrix[0][2] == expected_bytes[8]
        assert bytes_matrix[1][2] == expected_bytes[9]
        assert bytes_matrix[2][2] == expected_bytes[10]
        assert bytes_matrix[3][2] == expected_bytes[11]

        assert bytes_matrix[0][3] == expected_bytes[12]
        assert bytes_matrix[1][3] == expected_bytes[13]
        assert bytes_matrix[2][3] == expected_bytes[14]
        assert bytes_matrix[3][3] == expected_bytes[15]


    def test_bytes_matrix_to_word128bits(self):
        expected_word128bit = 0
        shift = 120
        for i in range(16):
            expected_word128bit |= random.randint(0, 255) << shift
            shift -= 8

        bytes_matrix = word128bits_to_bytes_matrix(expected_word128bit)
        word128bit = bytes_matrix_to_word128bits(bytes_matrix)
        assert expected_word128bit == word128bit
