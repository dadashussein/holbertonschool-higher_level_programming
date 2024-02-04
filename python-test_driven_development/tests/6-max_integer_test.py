#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Document for unit test"""
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -3, -6, -1, -10]), -1)
