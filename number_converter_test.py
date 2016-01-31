import unittest
import number_converter


class NumberConverterTest(unittest.TestCase):

    def setUp(self):
        self.converter = number_converter.NumberConverter()

    def test_that_basic_numeral_definitions_work(self):
        self.assertEqual(self.converter.convert(1), "I")
        self.assertEqual(self.converter.convert(5), "V")
        self.assertEqual(self.converter.convert(10), "X")
        self.assertEqual(self.converter.convert(50), "L")
        self.assertEqual(self.converter.convert(100), "C")
        self.assertEqual(self.converter.convert(500), "D")
        self.assertEqual(self.converter.convert(1000), "M")

    def test_conversion_using_basic_adding_rule(self):
        self.assertEqual(self.converter.convert(2), "II")


if __name__ == '__main__':
    unittest.main()