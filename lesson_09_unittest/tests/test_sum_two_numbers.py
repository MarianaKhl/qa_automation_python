import unittest
from lesson_09_unittest.src.functions import sum_two_numbers


class TestSumTwoNumbers(unittest.TestCase):
    def test_sum_positive(self):
        result = sum_two_numbers(1, 2)
        self.assertEqual(result, 3)

    def test_sum_negative1(self):
        result = sum_two_numbers(-5, 10)
        self.assertEqual(result, -100)

    def test_sum_negative2(self):
        with self.assertRaises(ValueError, msg="Absent one of two numbers"):
            try:
                sum_two_numbers(1, None)
            except ValueError as cm:
                print(f"Error occurred: {cm}")


if __name__ == '__main__':
    unittest.main()
