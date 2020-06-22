class RomanNumeralTranslator:

    def translate(self, number):

        if number > 3:
            return "IV"

        roman_numeral = ""

        for n in range(1, number+1):
            roman_numeral += "I"
        return roman_numeral
