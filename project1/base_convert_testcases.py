import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

    def test_0(self):
        self.assertEqual(convert(0,0), '0')

    def test_124(self):
        self.assertEqual(convert(124, 12), "A4")

    def test_large(self):
        self.assertEqual(convert(7341213456, 13), '8CCC039B5')

    def test_509(self):
        self.assertEqual(convert(509, 7), "1325")

if __name__ == "__main__":
        unittest.main()