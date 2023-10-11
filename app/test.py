import unittest
from app import is_prime

class AppTestCase(unittest.TestCase):
    def test_true_when_x_is_17(self):
        result = is_prime(17)
        self.assertEqual(eval(result), True)

class AppTestCase(unittest.TestCase):
    def test_true_when_x_is_36(self):
        result = is_prime(36)
        self.assertEqual(eval(result), False)

class AppTestCase(unittest.TestCase):
    def test_true_when_x_is_13219(self):
        result = is_prime(13219)
        self.assertEqual(eval(result), True)

if __name__ == '__main__':
    unittest.main()