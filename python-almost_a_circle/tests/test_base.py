#!/usr/bin/python3
"""Document for unit test"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Document for unit test"""
    def test_base(self):
        """test for base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_2(self):
        """test for base class 2"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_3(self):
        """ test for base class 3"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_base_4(self):
        """ test for base class 4"""
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_json_string(self):
        """ test for json string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        """ test for save to file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(type(file.read()), str)

    def test_from_json_string(self):
        """ test for from json string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[{"id": 89, "width": 10}]'),
                         [{'id': 89, 'width': 10}])

    def test_create(self):
        """ test for create method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_load_from_file(self):
        """ test for load from file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(list_input[0]), str(list_output[0]))
        self.assertEqual(str(list_input[1]), str(list_output[1]))
