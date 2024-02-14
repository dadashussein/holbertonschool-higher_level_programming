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

    def update(self, *args, **kwargs):
        """Document for method"""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
