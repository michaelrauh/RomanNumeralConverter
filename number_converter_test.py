import unittest
import number_converter


class NumberConverterTest(unittest.TestCase):

    def setUp(self):
        self.converter = number_converter.NumberConverter()

    def test_that_one_is_i(self):
        self.assertEqual(self.converter.convert(1), "I")

    def test_that_five_is_V(self):
        self.assertEqual(self.converter.convert(5), "V")

if __name__ == '__main__':
    unittest.main()