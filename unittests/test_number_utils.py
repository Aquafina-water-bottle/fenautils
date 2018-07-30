import unittest

from fenautils import is_number, is_signed_int, is_nonneg_int, is_pos_int

class TestNumberUtils(unittest.TestCase):
    def test_numbers(self):
        # valid
        self.assertTrue(is_number("25.6"))
        self.assertTrue(is_number("-25.6"))
        self.assertTrue(is_number("0"))
        self.assertTrue(is_number("1964"))
        self.assertTrue(is_number("-1964"))

        # invalid numbers
        self.assertFalse(is_number("6e5"))
        self.assertFalse(is_number("1_964"))
        self.assertFalse(is_number("NaN"))
        self.assertFalse(is_number("None"))
        self.assertFalse(is_number("27j+5"))
        self.assertFalse(is_number("abcdefg"))
        self.assertFalse(is_number("12345abcdefg"))
        self.assertFalse(is_number("~26.3"))
        self.assertFalse(is_number("^26.3"))

    def test_signed_ints(self):
        # valid numbers, note that decimal places aren't integers
        self.assertFalse(is_signed_int("25.6"))
        self.assertFalse(is_signed_int("-25.6"))
        self.assertTrue(is_signed_int("0"))
        self.assertTrue(is_signed_int("1964"))
        self.assertTrue(is_signed_int("-1964"))

        # invalid numbers
        self.assertFalse(is_signed_int("6e5"))
        self.assertFalse(is_signed_int("1_964"))
        self.assertFalse(is_signed_int("NaN"))
        self.assertFalse(is_signed_int("None"))
        self.assertFalse(is_signed_int("27j+5"))
        self.assertFalse(is_signed_int("abcdefg"))
        self.assertFalse(is_signed_int("12345abcdefg"))
        self.assertFalse(is_signed_int("~26.3"))
        self.assertFalse(is_signed_int("^26.3"))

    def test_nonneg_int(self):
        self.assertFalse(is_nonneg_int("25.6"))
        self.assertFalse(is_nonneg_int("-25.6"))
        self.assertTrue(is_nonneg_int("0"))
        self.assertTrue(is_nonneg_int("1964"))
        self.assertFalse(is_nonneg_int("-1964"))

        self.assertFalse(is_nonneg_int("6e5"))
        self.assertFalse(is_nonneg_int("1_964"))
        self.assertFalse(is_nonneg_int("NaN"))
        self.assertFalse(is_nonneg_int("None"))
        self.assertFalse(is_nonneg_int("27j+5"))
        self.assertFalse(is_nonneg_int("abcdefg"))
        self.assertFalse(is_nonneg_int("12345abcdefg"))
        self.assertFalse(is_nonneg_int("~26.3"))
        self.assertFalse(is_nonneg_int("^26.3"))

    def test_pos_int(self):
        self.assertFalse(is_pos_int("25.6"))
        self.assertFalse(is_pos_int("-25.6"))
        self.assertFalse(is_pos_int("0"))
        self.assertTrue(is_pos_int("1964"))
        self.assertFalse(is_pos_int("-1964"))

        self.assertFalse(is_pos_int("6e5"))
        self.assertFalse(is_pos_int("1_964"))
        self.assertFalse(is_pos_int("NaN"))
        self.assertFalse(is_pos_int("None"))
        self.assertFalse(is_pos_int("27j+5"))
        self.assertFalse(is_pos_int("abcdefg"))
        self.assertFalse(is_pos_int("12345abcdefg"))
        self.assertFalse(is_pos_int("~26.3"))
        self.assertFalse(is_pos_int("^26.3"))



