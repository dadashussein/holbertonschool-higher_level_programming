#!/usr/bin/python3
"""Document for module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Document for Square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            Square.__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """doc for getter"""
        return self.width

    @size.setter
    def size(self, value):
        """doc for setter"""
        self.width = value
        self.height = value
