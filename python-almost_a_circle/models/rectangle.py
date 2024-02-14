#!/usr/bin/python3
"""Document for module"""
from models.base import Base


class Rectangle(Base):
    """Document for class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, input):
        """set value"""
        if type(input) is not int:
            raise TypeError("width must be an integer")
        if input <= 0:
            raise ValueError("width must be > 0")
        self.__width = input

    @property
    def height(self):
        """doc property"""
        return self.__height

    @height.setter
    def height(self, input):
        """doc for setter"""
        if type(input) is not int:
            raise TypeError("height must be an integer")
        if input <= 0:
            raise ValueError("height must be > 0")
        self.__height = input

    @property
    def x(self):
        """doc property"""
        return self.__x

    @x.setter
    def x(self, input):
        """doc for setter"""
        if type(input) is not int:
            raise TypeError("x must be an integer")
        if input < 0:
            raise ValueError("x must be >= 0")
        self.__x = input

    @property
    def y(self):
        """doc property"""
        return self.__y

    @y.setter
    def y(self, input):
        """doc for setter"""
        if type(input) is not int:
            raise TypeError("y must be an integer")
        if input < 0:
            raise ValueError("y must be >= 0")
        self.__y = input

    def area(self):
        """Document for method"""
        return self.__height * self.__width

    def display(self):
        """Doc for method"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        return "[{}] ({}) {}/{} - {}/{}".format(Rectangle.__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update attribut Rectangle"""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Dictionary"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
