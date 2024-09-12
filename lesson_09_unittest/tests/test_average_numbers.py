import unittest
from lesson_09_unittest.src.functions import average_numbers


class TestAverageNumbers(unittest.TestCase):
    def test_average_positive1(self):
        result = average_numbers([1, 2, 9])
        self.assertEqual(result, 4)

    def test_average_positive2(self):
        result = average_numbers([0, 0, 0])
        self.assertEqual(result, 0)

    def test_average_positive3(self):
        result = average_numbers([1.5, 2.5, 9.5])
        self.assertEqual(result, 4.5)

    def test_average_negative1(self):
        result = average_numbers([10, 2, 9])
        self.assertEqual(result, 4)

    def test_average_negative2(self):
        result = average_numbers([10, 2, 9, -5])
        self.assertEqual(result, -3)

    def test_average_negative3(self):
        result = ([])
        self.assertEqual(result, "We dont have empty list!", msg="The list witch you check is empty!")

    def test_average_negative4(self):
        with self.assertRaises(TypeError) as cm:
            average_numbers([10, "2", 9, -5, "python"])
        self.assertEqual(str(cm.exception), "The list contains invalid data: all elements must be numbers!")

if __name__ == '__main__':
    unittest.main()
