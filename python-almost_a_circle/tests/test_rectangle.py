#!/usr/bin/python3
"""test rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test cases for rectangle class"""
    def test_str(self):
        """Tests the __str__()"""
        r1 = Rectangle(4, 2, 1, 5, 89)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/5 - 4/2")

    def test_area(self):
        """Tests the area method"""
        r2 = Rectangle(3, 2)
        self.assertEqual(r2.area(), 6)

    def test_display(self):
        """Tests the display method"""
        r3 = Rectangle(2, 3)
        self.assertEqual(r3.display(), None)

    def test_update(self):
        """Tests the update method"""
        r4 = Rectangle(10, 10, 10, 10)
        r4.update(89)
        self.assertEqual(r4.id, 89)

    def test_to_dictionary(self):
        """Tests the to_dictionary method"""
        r5 = Rectangle(10, 2, 1, 9, 89)
        self.assertEqual(r5.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 89, 'height': 2, 'width': 10})
