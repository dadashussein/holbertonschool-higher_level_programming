#!/usr/bin/python3
"""test rectangle class"""
import unittest
import os
import sys
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test cases for rectangle class"""

    def test_rectangle(self):
        """Tests the rectangle class"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 5)

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
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n##\n")

    def test_update(self):
        """Tests the update method"""
        r4 = Rectangle(10, 10, 10, 10)
        r4.update(89)
        self.assertEqual(r4.id, 89)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_save_to_file(self):
        try:
            os.remove("Rectangle.json")
        except Exception as e:
            pass

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except Exception as e:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except Exception as e:
            pass

        Rectangle.save_to_file([Rectangle(1, 2, id=13)])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                file.read(),
                '[{"id": 13, "width": 1, "height": 2, "x": 0, "y": 0}]'
            )

    def test_to_dictionary(self):
        """Tests the to_dictionary method"""
        r5 = Rectangle(10, 2, 1, 9, 89)
        self.assertEqual(r5.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 89, 'height': 2, 'width': 10})
