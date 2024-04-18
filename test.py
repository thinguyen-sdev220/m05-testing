# Author: Thi Nguyen
# File name: test.py
# Description:  Testing program to check if the sum function in the my_sum.py module behaves as expected under different scenarios

import unittest

from my_sum import sum
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()


# After running the test, you’ll see the following information:
# Results of all the tests, one failed (F) and one passed (.)
# Details of failed test (test_list_fraction)