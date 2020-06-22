import unittest
import roman_numeral


class RomanNumeralTranslatorTest(unittest.TestCase):

    def test_one_returns_I(self):
        translator = roman_numeral.RomanNumeralTranslator()
        self.assertEqual("I", translator.translate(1))

    def test_two_returns_II(self):
        translator = roman_numeral.RomanNumeralTranslator()
        self.assertEqual("II", translator.translate(2))


if __name__ == "__main__":
    unittest.main()