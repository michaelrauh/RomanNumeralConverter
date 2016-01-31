class NumberConverter():

    @staticmethod
    def convert(number):
        number_to_numeral = {1: "I", 5: "V"}
        return number_to_numeral[number]