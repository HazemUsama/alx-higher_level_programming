#!/usr/bin/python3
"""8-rectangle"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    
    def __init__(self, width, height):
        integer_validator(self, "width", width)
        integer_validator(self, "height", width)
        self.__width = width
        self.__height = height
