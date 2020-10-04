#  Python utilities
import unittest

# Coding problem
from lisas_workbook.lisas_workbook import main


class LisasWorkbookTests(unittest.TestCase):

    def test_case_one(self):
        n = 5
        k = 3
        arr = [4, 2, 6, 1, 10]
        self.assertEqual(main(n, k, arr), 4)

    def test_case_two(self):
        n = 10
        k = 5
        arr = [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]
        self.assertEqual(main(n, k, arr), 8)


if __name__ == '__main__':
    unittest.main()
    