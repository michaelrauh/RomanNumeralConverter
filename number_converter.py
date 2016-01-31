class NumberConverter():

    @staticmethod
    def convert(number):
        number_to_numeral = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        final = ""
        while number > 0:
            nearest_key = max([i for i in number_to_numeral.keys() if i <= number])
            final += number_to_numeral[nearest_key]
            number -= nearest_key
        return final