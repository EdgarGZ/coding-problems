#  Python utilities
import unittest

# Coding problem
from time_in_words.time_in_words import main


class TimeInWordsTests(unittest.TestCase):

    def test_case_one(self):
        h = 5
        m = 45
        self.assertEqual(main(h, m), 'quarter to six')

    def test_case_two(self):
        h = 3
        m = 00
        self.assertEqual(main(h, m), 'three o\' clock')

    def test_case_three(self):
        h = 7
        m = 15
        self.assertEqual(main(h, m), 'quarter past seven')


if __name__ == '__main__':
    unittest.main()