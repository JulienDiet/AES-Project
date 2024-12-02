from unittest import TestCase

from substitution import load_substitution_box, inverse_substitution_box, substitution


class Test(TestCase):
    def test_load_substitution_box(self):
        substitution_box = load_substitution_box()

        assert substitution_box[0][0] == 0x63
        assert substitution_box[15][15] == 0x16

    def test_inverse_substitution_box(self):
        inverse_box = inverse_substitution_box(load_substitution_box())

        assert inverse_box[6][3] == 0x00
        assert inverse_box[1][6] == 0xff

    def test_substitution(self):
        substitution_box = load_substitution_box()
        assert substitution(substitution_box, 0xae) == 0xe4

    def test_substitution_inverse(self):
        inverse_box = inverse_substitution_box(load_substitution_box())
        assert substitution(inverse_box, 0xe4) == 0xae
