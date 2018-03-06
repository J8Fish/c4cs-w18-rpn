import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exp(self):
        result = rpn.calculate("2 2 ^")
        self.assertEqual(4, result)

'''if __name__ == "__main__":
    a = TestBasics()
    a.test_add()
    a.test_subtract()
    a.test_multiply()
    a.test_divide()
    a.test_exp()'''
