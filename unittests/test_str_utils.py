import unittest

from fenautils import decode_str, encode_str

class TestNumberUtils(unittest.TestCase):
    def test_decode_str(self):
        self.assertEqual(decode_str(r'"hello"'), "hello")
        self.assertEqual(decode_str(r'""'), "")
        self.assertEqual(decode_str(r'"\\x89\\t"'), r'\x89\t')

        with self.assertRaises(SyntaxError) as cm:
            decode_str(r'')
        self.assertEqual(str(cm.exception), "Expected the string '' to be longer than two characters so it can begin and end with a quotation")

        with self.assertRaises(SyntaxError) as cm:
            decode_str(r'hello')
        self.assertEqual(str(cm.exception), "Expected the string 'hello' to begin with a quotation")

        with self.assertRaises(SyntaxError) as cm:
            decode_str(r'"hello')
        self.assertEqual(str(cm.exception), "Expected the string '\"hello' to end with a quotation")

    def test_encode_str(self):
        self.assertEqual(encode_str('hello'), '"hello"')
        self.assertEqual(encode_str(r'\x89\t'), r'"\\x89\\t"')





