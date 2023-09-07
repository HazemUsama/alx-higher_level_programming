#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class to test max_integer
    """

    def test_positive(self):
        """
        Test positive integer
        """
        lis = [1, 2, 3, 4]
        self.assertEqual(max_integer(lis), 4)

    def test_negative(self):
        """
        Test negative integer
        """
        lis = [-1, -2, -3, -4]
        self.assertEqual(max_integer(lis), -1)

        # with zero
        lis += [0]
        self.assertEqual(max_integer(lis), 0)

    def test_empty(self):
        """
        Test empty list
        """
        lis = []
        self.assertIsNone(max_integer(lis))

    def test_none(self):
        """
        Test None
        """
        lis = None
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_wrongType(self):
        """
        Test Wrong Type
        """
        lis1 = ["hazem", "osama"]
        lis2 = 123

        self.assertEqual(max_integer(lis1), "osama")
        with self.assertRaises(TypeError):
            max_integer(lis2)

    def test_list_but_not_integer(self):
        """
        Test when not all elemets are integers
        """
        lis1 = [1, 2, 'hello']
        with self.assertRaises(TypeError):
            max_integer(lis1)

    def test_one_elm(self):
        """
        Test when one element only exist
        """
        lis = [1]
        self.assertEqual(max_integer(lis), 1)

    def test_middle(self):
        """
        Test if the max element is in the middle
        """
        lis = [1, 3, 2]
        self.assertEqual(max_integer(lis), 3)
