import unittest
import number_converter


class NumberConverterTest(unittest.TestCase):

    def test_that_one_is_i(self):
        converter = number_converter.NumberConverter()
        self.assertEqual(converter.convert(1), "I")

if __name__ == '__main__':
    unittest.main()