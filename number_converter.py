class NumberConverter():

    @staticmethod
    def convert(number):
        number_to_numeral = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        return number_to_numeral[number]