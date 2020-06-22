class RomanNumeralTranslator:

    def translate(self, number):

        roman_numeral = ""

        for n in range(1, number+1):
            roman_numeral += "I"
        return roman_numeral
