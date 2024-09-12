import unittest
from lesson_09_unittest.src.functions import find_unique_value


class TestFindUniqueValue(unittest.TestCase):
    def test_unique_value_positive1(self):
        result = find_unique_value("uyfc3r4#!#2o%i&ujd0909873")
        self.assertTrue(result, msg="Entered unique value more than 10")

    def test_unique_value_positive2(self):
        result = find_unique_value("$5hK(c$)p!")
        self.assertFalse(result, msg="Entered unique value equals 10")

    def test_unique_value_negative1(self):
        result = find_unique_value("u6+#64oi")
        self.assertFalse(result, msg="Entered unique value less than 10")

    def test_unique_value_empty(self):
        result = find_unique_value("")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
