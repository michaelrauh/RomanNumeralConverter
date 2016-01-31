import unittest
import number_converter


class NumberConverterTest(unittest.TestCase):

    def setUp(self):
        self.converter = number_converter.NumberConverter()

    def test_that_basic_numeral_definitions_work(self):
        self.assertEqual(self.converter.convert_arabic_to_numeral(1), "I")
        self.assertEqual(self.converter.convert_arabic_to_numeral(5), "V")
        self.assertEqual(self.converter.convert_arabic_to_numeral(10), "X")
        self.assertEqual(self.converter.convert_arabic_to_numeral(50), "L")
        self.assertEqual(self.converter.convert_arabic_to_numeral(100), "C")
        self.assertEqual(self.converter.convert_arabic_to_numeral(500), "D")
        self.assertEqual(self.converter.convert_arabic_to_numeral(1000), "M")

    def test_conversion_using_basic_adding_rule(self):
        self.assertEqual(self.converter.convert_arabic_to_numeral(2), "II")
        self.assertEqual(self.converter.convert_arabic_to_numeral(6), "VI")
        self.assertEqual(self.converter.convert_arabic_to_numeral(20), "XX")
        self.assertEqual(self.converter.convert_arabic_to_numeral(1001), "MI")
        self.assertEqual(self.converter.convert_arabic_to_numeral(61), "LXI")

    def test_conversion_using_basic_subtraction_rule(self):
        self.assertEqual(self.converter.convert_arabic_to_numeral(4), "IV")
        self.assertEqual(self.converter.convert_arabic_to_numeral(9), "IX")
        self.assertEqual(self.converter.convert_arabic_to_numeral(40), "XL")
        self.assertEqual(self.converter.convert_arabic_to_numeral(900), "CM")

    def test_conversion_of_arbitrary_number(self):
        self.assertEqual(self.converter.convert_arabic_to_numeral(1066), "MLXVI")
        self.assertEqual(self.converter.convert_arabic_to_numeral(1989), "MCMLXXXIX")
        self.assertEqual(self.converter.convert_arabic_to_numeral(3), "III")

    def test_forbidden_numbers(self):
        self.assertEqual(self.converter.convert_arabic_to_numeral(-1), "")
        self.assertEqual(self.converter.convert_arabic_to_numeral(0), "")

    def test_overflow_numbers(self):
        self.assertEqual(self.converter.convert_arabic_to_numeral(5000), "")

    def test_basic_conversion_from_numeral_to_arabic(self):
        self.assertEqual(self.converter.convert_numeral_to_arabic("I"), 1)
        self.assertEqual(self.converter.convert_numeral_to_arabic("V"), 5)
        self.assertEqual(self.converter.convert_numeral_to_arabic("X"), 10)
        self.assertEqual(self.converter.convert_numeral_to_arabic("L"), 50)
        self.assertEqual(self.converter.convert_numeral_to_arabic("C"), 100)
        self.assertEqual(self.converter.convert_numeral_to_arabic("D"), 500)
        self.assertEqual(self.converter.convert_numeral_to_arabic("M"), 1000)

    def test_basic_add_case_for_numeral_to_arabic(self):
        self.assertEqual(self.converter.convert_numeral_to_arabic("II"), 2)
        self.assertEqual(self.converter.convert_numeral_to_arabic("VI"), 6)
        self.assertEqual(self.converter.convert_numeral_to_arabic("XX"), 20)
        self.assertEqual(self.converter.convert_numeral_to_arabic("MI"), 1001)
        self.assertEqual(self.converter.convert_numeral_to_arabic("LXI"), 61)

    def test_basic_subtract_case_for_numeral_to_arabic(self):
        self.assertEqual(self.converter.convert_numeral_to_arabic("IV"), 4)
        self.assertEqual(self.converter.convert_numeral_to_arabic("IX"), 9)
        self.assertEqual(self.converter.convert_numeral_to_arabic("XL"), 40)
        self.assertEqual(self.converter.convert_numeral_to_arabic("CM"), 900)

    def test_arbitrary_conversion_for_numeral_to_arabic(self):
        self.assertEqual(self.converter.convert_numeral_to_arabic("MLXVI"), 1066)
        self.assertEqual(self.converter.convert_numeral_to_arabic("MCMLXXXIX"), 1989)
        self.assertEqual(self.converter.convert_numeral_to_arabic("III"), 3)

    def test_that_a_numeral_can_repeat_only_three_times(self):
        self.assertEqual(self.converter.convert_numeral_to_arabic("XXXX"), 0)
        self.assertEqual(self.converter.convert_numeral_to_arabic("IIII"), 0)
        self.assertEqual(self.converter.convert_numeral_to_arabic("CCCC"), 0)
        self.assertEqual(self.converter.convert_numeral_to_arabic("MMMM"), 0)

    def test_that_certain_numerals_may_not_repeat(self):
        self.assertEqual(self.converter.convert_numeral_to_arabic("VV"), 0)
        self.assertEqual(self.converter.convert_numeral_to_arabic("LL"), 0)
        self.assertEqual(self.converter.convert_numeral_to_arabic("DD"), 0)

    def test_that_only_one_subtraction_can_be_made_per_numeral(self):
        self.assertEqual(self.converter.convert_numeral_to_arabic("XXC"), 0)

if __name__ == '__main__':
    unittest.main()