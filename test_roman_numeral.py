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


if __name__ == "__main__":
    unittest.main()