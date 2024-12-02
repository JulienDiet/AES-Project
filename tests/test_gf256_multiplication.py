from unittest import TestCase

from gf256_multiplication import multiply_by_2, multiply_by_3, multiply_by_9, multiply_by_11, multiply_by_13, \
    multiply_by_14


class Test(TestCase):
    def test_multiply_by_2_with_overflow(self):
        # (130 << 2) ^ 0x11b
        assert multiply_by_2(130) == 31

    def test_multiply_by_2_without_overflow(self):
        # (75 << 2)
        assert multiply_by_2(75) == 150

    def test_multiply_by_3(self):
        # ((130 << 2) ^ 0x11b) ^ 130
        assert multiply_by_3(130) == 157

    def test_multiply_by_9(self):
        # 0xfe
        assert multiply_by_9(130) == 254

    def test_multiply_by_11(self):
        # 0xe1
        assert multiply_by_11(130) == 225

    def test_multiply_by_13(self):
        # 0xc0
        assert multiply_by_13(130) == 192

    def test_multiply_by_14(self):
        # 0x5d
        assert multiply_by_14(130) == 93
