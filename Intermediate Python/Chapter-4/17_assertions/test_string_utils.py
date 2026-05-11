import unittest
import string_utils

# Define Test Class

class TestStringUtils(unittest.TestCase):

    # define test methods

    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string("hello"), "olleh")

    def test_capitalize_string(self):
        self.assertEqual(string_utils.capitalize_string("hello"), "Hello")

    def test_is_capitalized(self):
        self.assertTrue(string_utils.is_capitalized("Hello"))
        self.assertFalse(string_utils.is_capitalized("hello"))


if __name__ == '__main__':
    unittest.main()