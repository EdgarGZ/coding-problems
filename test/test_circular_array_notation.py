#  Python utilities
import unittest

# Coding problem
from circular_array_notation.circular_array_notation import main


class CircularArrayRotationTests(unittest.TestCase):

    def test_case_one(self):
        a = [1, 2, 3]
        k = 2
        queries = [0, 1, 2]
        self.assertEqual(main(a, k, queries), [2, 3, 1])

    def test_case_two(self):
        a = [3, 4, 5]
        k = 2
        queries = [1, 2]
        self.assertEqual(main(a, k, queries), [5, 3])


if __name__ == '__main__':
    unittest.main()