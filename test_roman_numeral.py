import unittest
import roman_numeral


class RomanNumeralTranslatorTest(unittest.TestCase):

    translator = roman_numeral.RomanNumeralTranslator()

    def test_one_returns_I(self):
        self.assertEqual("I", self.translator.translate(1))

    def test_two_returns_II(self):
        self.assertEqual("II", self.translator.translate(2))

    def test_three_returns_III(self):
        self.assertEqual("III", self.translator.translate(3))

    def test_four_returnsIV(self):
        self.assertEqual("IV", self.translator.translate(4))

    def test_five_returns_V(self):
        self.assertEqual("V", self.translator.translate(5))

    def test_nine_returns_IX(self):
        self.assertEqual("IX", self.translator.translate(9))


if __name__ == "__main__":
    unittest.main()