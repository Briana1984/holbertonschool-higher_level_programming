#!/usr/bin/python3
""" model with class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle inherits Base"""

    def __init__(self, width, height, x=0, y=0, id=1):
        """ Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attributes("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attributes("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_attributes("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_attributes("y", value)
        self.__y = value

    def validate_attributes(self, name, value, eq=True):
        """ validate the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def display(self):
        """Display the area"""
        print(self.__y * '\n', end='')
        for j in range(self.__height):
            print(str(self.__x * ' ') + str(self.__width * '#'))

    def __str__(self):
        """return info about rectangle"""
        id_st = self.id
        x_st = self.__x
        y_st = self.__y
        width_st = self.__width
        height_st = self.__height
        return f"[Rectangle] ({id_st}) {x_st}/{y_st} - {width_st}/{height_st}"

    def update(self, *args, **kwargs):
        """number of arguments"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):

        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
