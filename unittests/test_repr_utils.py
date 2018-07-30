import unittest
from typing import NamedTuple

from fenautils import addrepr

@addrepr
class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

@addrepr
class B(NamedTuple):
    a: str
    b: int
    c: float


class TestReprUtils(unittest.TestCase):
    def test_addrepr(self):
        a = A("1", 2, (3, "4"))
        self.assertEqual(repr(a), "A[a='1', b=2, c=(3, '4')]")

        b = B("1", 2, 3.4)
        with self.assertRaises(TypeError) as cm:
            repr(b)
        self.assertEqual(str(cm.exception), "vars() argument must have __dict__ attribute")

