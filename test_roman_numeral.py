import unittest
import roman_numeral

class RomanNumeralTranslatorTest(unittest.TestCase):

    def test_one_returns_I(self):
        number = roman_numeral.RomanNumeralTranslator()
        self.assertEqual("I", number.translate(1))


if __name__ == "__main__":
    unittest.main()