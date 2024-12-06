import unittest
from lesson_09_unittest.src.functions import sum_even_numbers


class TestSumEvenNumbers(unittest.TestCase):
    def test_sum_even_numbers_positive1(self):
        result = sum_even_numbers([1, 2, 9, 8, 4])
        self.assertEqual(result, 14)

    def test_sum_even_numbers_positive2(self):
        result = sum_even_numbers([1, -2, 9, 8, 4, 0])
        self.assertEqual(result, 10)

    def test_sum_even_numbers_positive3(self):
        result = sum_even_numbers([0])
        self.assertEqual(result, 0)

    def test_sum_even_numbers_negative1(self):
        result = sum_even_numbers([1, -2, 9, -8, 4, 0])
        self.assertEqual(result, 10)

    def test_sum_even_numbers_negative2(self):
        result = sum_even_numbers([1, 9, 7])
        self.assertEqual(result, 10)

    def test_sum_even_numbers_negative3(self):
        result = sum_even_numbers([])
        self.assertEqual(result, "We dont have empty list!", msg="The list witch you check is empty!")

if __name__ == '__main__':
    unittest.main()
