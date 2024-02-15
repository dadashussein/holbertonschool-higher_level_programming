"""test rectangle class"""
import unittest
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
