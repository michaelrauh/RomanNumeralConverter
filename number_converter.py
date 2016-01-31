class NumberConverter():

    @staticmethod
    def convert(arabic):
        arabic_to_numeral = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",
                             400: "CD", 500: "D", 900: "CM", 1000: "M"}
        numeral = ""
        while 0 < arabic < 5000:
            highest_below_arabic = max([i for i in arabic_to_numeral.keys() if i <= arabic])
            numeral += arabic_to_numeral[highest_below_arabic]
            arabic -= highest_below_arabic
        return numeral