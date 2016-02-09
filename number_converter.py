class NumberConverter():

    def __init__(self):
        self.ARABIC_TO_NUMERAL = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",
                                  400: "CD", 500: "D", 900: "CM", 1000: "M"}
        self.NUMERAL_TO_ARABIC = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        self.NUMERAL_TO_ARABIC_SUBTRACT_PATTERNS = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        self.ILLEGAL_PATTERNS = ["IIII", "XXXX", "CCCC", "MMMM", "VV", "LL", "DD", "IXL", "IXC", "XCD", "XCM", "IIV",
                                 "IIX", "XXL", "XXC", "CCD", "CCM"]

    def convert_arabic_to_numeral(self, arabic):
        numeral = ""
        while 0 < arabic < 5000:
            highest_below_arabic = max([i for i in self.ARABIC_TO_NUMERAL.keys() if i <= arabic])
            numeral += self.ARABIC_TO_NUMERAL[highest_below_arabic]
            arabic -= highest_below_arabic
        return numeral

    def convert_numeral_to_arabic(self, numeral):

        if self.check_for_illegal_pattern(numeral):
            return 0

        arabic = 0
        while numeral != "":
            if numeral[:2] in self.NUMERAL_TO_ARABIC_SUBTRACT_PATTERNS:
                arabic += self.NUMERAL_TO_ARABIC_SUBTRACT_PATTERNS[numeral[:2]]
                numeral = numeral[2:]
            else:
                arabic += self.NUMERAL_TO_ARABIC[numeral[0]]
                numeral = numeral[1:]
        return arabic

    def check_for_illegal_pattern(self, numeral):
        for pattern in self.ILLEGAL_PATTERNS:
            if pattern in numeral:
                return True
        return False