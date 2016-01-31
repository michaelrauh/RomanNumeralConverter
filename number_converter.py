class NumberConverter():

    @staticmethod
    def convert(arabic):
        arabic_to_numeral = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        numeral = ""
        while arabic > 0:
            highest_below_arabic = max([i for i in arabic_to_numeral.keys() if i <= arabic])
            numeral += arabic_to_numeral[highest_below_arabic]
            arabic -= highest_below_arabic
        return numeral