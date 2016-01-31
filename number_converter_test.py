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


if __name__ == '__main__':
    unittest.main()