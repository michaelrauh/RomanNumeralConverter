class NumberConverter():

    @staticmethod
    def convert_arabic_to_numeral(arabic):
        arabic_to_numeral = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",
                             400: "CD", 500: "D", 900: "CM", 1000: "M"}
        numeral = ""
        while 0 < arabic < 5000:
            highest_below_arabic = max([i for i in arabic_to_numeral.keys() if i <= arabic])
            numeral += arabic_to_numeral[highest_below_arabic]
            arabic -= highest_below_arabic
        return numeral

    @staticmethod
    def convert_numeral_to_arabic(numeral):
        numeral_to_arabic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        numeral_to_arabic_subtract_patterns = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        illegal_patterns = ["IIII", "XXXX", "CCCC", "MMMM", "VV", "LL", "DD", "IXL", "IXC", "XCD", "XCM"]
        for pattern in illegal_patterns:
            if pattern in numeral:
                return 0

        arabic = 0
        previous = float("inf")
        while numeral != "":
            if numeral[:2] in numeral_to_arabic_subtract_patterns:
                arabic += numeral_to_arabic_subtract_patterns[numeral[:2]]
                if previous < numeral_to_arabic_subtract_patterns[numeral[:2]]:
                    return 0
                numeral = numeral[2:]
            else:
                arabic += numeral_to_arabic[numeral[0]]
                numeral = numeral[1:]
            previous = arabic
        return arabic