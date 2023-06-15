#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    def test_max_integer(self):
        # Test with positive integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        # Test with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

        # Test with mixed positive and negative integers
        self.assertEqual(max_integer([-5, -2, 0, 4, 7]), 7)

        # Test with duplicate values
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing a single element
        self.assertEqual(max_integer([10]), 10)

        # Test with a list containing floats
        self.assertEqual(max_integer([1.5, 2.7, 3.2]), 3.2)

        # Test with a list containing a mix of integers and floats
        self.assertEqual(max_integer([2, 4.5, 1, 3.8]), 4.5)

        # Test with a large list
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)


if __name__ == '__main__':
    unittest.main()
