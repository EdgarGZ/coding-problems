#  Python utilities
import unittest

# Coding problem
from super_reduced_string.super_reduced_string import main


class DesignerPDFViewerTests(unittest.TestCase):

    def test_case_one(self):
        string = 'aaabccddd'
        self.assertEqual(main(string), 'abd')

    def test_case_two(self):
        string = 'aa'
        self.assertEqual(main(string), 'Empty String')

    def test_case_three(self):
        string = 'baab'
        self.assertEqual(main(string), 'Empty String')

    def test_case_four(self):
        string = 'acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj'
        self.assertEqual(main(string), 'acdqgacdqj')


if __name__ == '__main__':
    unittest.main()