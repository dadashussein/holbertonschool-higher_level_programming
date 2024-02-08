#!/usr/bin/python3
"""Document for module"""


class BaseGeometry:
    """Document for class"""
    def area(self):
        """Calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
