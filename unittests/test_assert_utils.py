import unittest

from fenautils import assert_type, assert_iterable_types

class TestAssertUtils(unittest.TestCase):
    def test_assert_type(self):
        self.assertIsNone(assert_type([], list, int))
        self.assertIsNone(assert_type(46, list, int))

        with self.assertRaises(AssertionError) as cm:
            assert_type("yep", list, int)
        self.assertEqual(str(cm.exception), "Expected type of 'yep' to be one of (<class 'list'>, <class 'int'>) but got <class 'str'>")

        with self.assertRaises(AssertionError) as cm:
            assert_type((25,), list)
        self.assertEqual(str(cm.exception), "Expected type of (25,) to be <class 'list'> but got <class 'tuple'>")

    def test_assert_iterable_types(self):
        self.assertIsNone(assert_iterable_types([1, 3, 2], int))
        self.assertIsNone(assert_iterable_types(["a", "b", "c"], str))
        self.assertIsNone(assert_iterable_types(("a", "b", "c"), int, str))

        with self.assertRaises(AssertionError) as cm:
            assert_iterable_types(["a", "b", "c"], int)
        self.assertEqual(str(cm.exception), "Expected type of 'a' to be <class 'int'> but got <class 'str'> in index 0 of iterable ['a', 'b', 'c']")

        with self.assertRaises(AssertionError) as cm:
            assert_iterable_types([23, "b", 327.4], int, str)
        self.assertEqual(str(cm.exception), "Expected type of 327.4 to be one of (<class 'int'>, <class 'str'>) but got <class 'float'> in index 2 of iterable [23, 'b', 327.4]")

        with self.assertRaises(AssertionError) as cm:
            assert_iterable_types([23, "b", 327.4], int, str, duplicate_key=lambda x: x)
        self.assertEqual(str(cm.exception), "Expected type of 327.4 to be one of (<class 'int'>, <class 'str'>) but got <class 'float'> in index 2 of iterable [23, 'b', 327.4]")

        # Duplicates
        self.assertIsNone(assert_iterable_types(("a", "b", "c"), str, duplicate_key=lambda x: x))

        with self.assertRaises(AssertionError) as cm:
            assert_iterable_types(("a", "b", "a"), str, duplicate_key=lambda x: x)
        self.assertEqual(str(cm.exception), "Found a duplicate of 'a' in 'a'")

        with self.assertRaises(AssertionError) as cm:
            assert_iterable_types(["123", "142", "225"], str, duplicate_key=lambda x: x[0])
        self.assertEqual(str(cm.exception), "Found a duplicate of '1' in '142'")

