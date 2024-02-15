"""test rectangle class"""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Doc for test class"""
    def test_init(self):
        """Tests init of Square"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        s2 = Square(2, 3, 1, 99)
        self.assertEqual(s2.id, 99)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 1)

    def test_square(self):
        s1 = Square(1, 2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        s2 = Square(1, 2, 3)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_square1(self):
        s0 = Square(1, 2, 3, 4)
        self.assertEqual(s0.size, 1)
        self.assertEqual(s0.x, 2)
        self.assertEqual(s0.y, 3)
        self.assertEqual(s0.id, 4)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s0 = Square(1, id=66)
        self.assertEqual(str(s0), "[Square] (66) 0/0 - 1")

    def test_area(self):
        """Tests area of Square"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 3, 1, 99)
        self.assertEqual(s2.area(), 4)

    def test_display(self):
        """Tests display of Square"""
        s1 = Square(2, 3, 1, 99)
        self.assertEqual(s1.display(), None)

    def test_update_kwargs(self):
        """Tests update of Square"""
        s1 = Square(4)
        s1.update(size=9, x=4)
        self.assertEqual(s1.size, 9)
        self.assertEqual(s1.x, 4)

    def test_update_args(self):
        """Tests update of Square"""
        s1 = Square(2)
        s1.update(5, 10, 1, 8)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 8)

    def test_to_dictionary(self):
        """Tests the to_dictionary() method"""
        s1 = Square(8, 1, 4, 42)
        expected_dict = {'id': 42, 'x': 1, 'size': 8, 'y': 4}
        self.assertEqual(s1.to_dictionary(), expected_dict)

    def test_create(self):
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)

        s2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s2.id, 89)
        self.assertEqual(s2.size, 1)

    def test_load_from_file(self):
        s1 = Square(2, 1, 2)
        Square.save_to_file([s1])
        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), 1)

    def test_save_to_file(self):
        try:
            os.remove("Square.json")
        except Exception as e:
            pass

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except Exception as e:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except Exception as e:
            pass

        Square.save_to_file([Square(1, 2, id=13)])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"id": 13, "size": 1, "x": 2, "y": 0}]')
