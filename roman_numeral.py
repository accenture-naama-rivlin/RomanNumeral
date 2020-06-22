class RomanNumeralTranslator:

    def translate(self, number):

        roman_numeral = ""
        arabic_to_roman = {
            5: "V",
            4: "IV",
            1: "I"
        }

        while number > 0:
            for arabic_value, roman_value in arabic_to_roman.items():
                if number >= arabic_value:
                    roman_numeral += roman_value
                    number -= arabic_value


        return roman_numeral
