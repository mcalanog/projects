# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_00(self):
        self.assertEqual(postfix_eval(""), '')

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        with self.assertRaises(ValueError):
            postfix_eval('5 0 /')

    def test_postfix_eval_06(self):
        try:
            postfix_eval("1.0 4 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)

    def test_postfix_eval_08(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4.0 ** + 3 -"), 83)

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(postfix_eval("4 6 <<"), 256)

    def test_postfix_eval_10(self):
        self.assertAlmostEqual(postfix_eval("4 6 >>"), 0)

    def test_postfix_eval_11(self):
        self.assertAlmostEqual(postfix_eval("3 3 /"), 1)

    def test_postfix_eval_12(self):
        self.assertAlmostEqual(postfix_eval("4 6 7 * *"), 168)

    def test_postfix_eval_13(self):
        try:
            postfix_eval("1.0 4 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_14(self):
        self.assertAlmostEqual(postfix_eval("4 6 -7 * *"), -168)

    def test_postfix_eval_15(self):
        try:
            postfix_eval("6 4 + -2 <<")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "cannot shift with negative number")


    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("6.0"), "6.0")
        self.assertEqual(infix_to_postfix("6.0 + 5 * 4"), "6.0 5 4 * +")
        self.assertEqual(infix_to_postfix("5 >> 3"), "5 3 >>")
        self.assertEqual(infix_to_postfix("5 << 3"), "5 3 <<")
        self.assertEqual(infix_to_postfix("5 << 3 + 6"), "5 3 << 6 +")
        self.assertEqual(infix_to_postfix("5 << 3 ** 6"), "5 3 << 6 **")
        self.assertEqual(infix_to_postfix("5 + 3 / ( 6 - 5 )"), "5 3 6 5 - / +")
        self.assertEqual(infix_to_postfix('( 4 - 5 ) *  1 >> 4 ** ( 5 - 6 )'), "4 5 - 1 4 >> 5 6 - ** *")
        self.assertEqual(infix_to_postfix("2 / ( 3 / ( 4 / 5 ) )"),"2 3 4 5 / / /")
        self.assertEqual(infix_to_postfix("4 ** 3 * 5 ** 2 - 7 ** 2"), "4 3 ** 5 2 ** * 7 2 ** -")
        self.assertEqual(infix_to_postfix("4 ** 3 * 5 ** 2 - 7 ** 2"), "4 3 ** 5 2 ** * 7 2 ** -")
        self.assertEqual(infix_to_postfix(""), "")
        self.assertEqual(infix_to_postfix("( 5 * ( 4 + 3 - 7 ) / 6 )"), "5 4 3 + 7 - * 6 /")
        self.assertEqual(infix_to_postfix("( 5 ** ( 6 - 3 + 2 ) ** 6 )"), "5 6 3 - 2 + 6 ** **")
        self.assertEqual(infix_to_postfix("4 + 5 + 7 - 6"), "4 5 + 7 + 6 -")
        self.assertEqual(infix_to_postfix("4 + ( 5 + 7 ) - 6"), "4 5 7 + + 6 -")
        self.assertEqual(infix_to_postfix("8 << 2 >> 3 ** 4 ** 5"), "8 2 << 3 >> 4 5 ** **")
        self.assertEqual(infix_to_postfix("3 + 6 * 5"), "3 6 5 * +")
        self.assertEqual(infix_to_postfix("3 * 6 + 5"), "3 6 * 5 +")

        
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4.0 5 6"), "3 2 1 / - 4.0 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* + 3 6 - 4 7"), "3 6 + 4 7 - *")
        self.assertEqual(prefix_to_postfix(""), "")

if __name__ == "__main__":
    unittest.main()
