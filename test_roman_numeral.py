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

    def test_four_returns_IV(self):
        self.assertEqual("IV", self.translator.translate(4))

    def test_five_returns_V(self):
        self.assertEqual("V", self.translator.translate(5))

    def test_nine_returns_IX(self):
        self.assertEqual("IX", self.translator.translate(9))

    def test_ten_returns_X(self):
        self.assertEqual("X", self.translator.translate(10))

    def test_twenty_returns_XX(self):
        self.assertEqual("XX", self.translator.translate(20))

    def test_forty_returns_XL(self):
        self.assertEqual("XL", self.translator.translate(40))

    def test_fifty_returns_L(self):
        self.assertEqual("L", self.translator.translate(50))

    def test_nintey_returns_XC(self):
        self.assertEqual("XC", self.translator.translate(90))

    def test_hundred_returns_C(self):
        self.assertEqual("C", self.translator.translate(100))

    def test_four_hundred_returns_CD(self):
        self.assertEqual("CD", self.translator.translate(400))

    def test_five_hundred_returns_D(self):
        self.assertEqual("D", self.translator.translate(500))

    def test_nine_hundred_returns_CM(self):
        self.assertEqual("CM", self.translator.translate(900))

    def test_one_thousand_returns_M(self):
        self.assertEqual("M", self.translator.translate(1000))


if __name__ == "__main__":
    unittest.main()