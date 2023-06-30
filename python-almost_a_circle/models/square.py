#!/usr/bin/python3
"""import class Rectangle"""
from models.rectangle import Rectangle


"""Create class"""


class Square(Rectangle):
    """Create constructor"""

    def __init__(self, size, x=0, y=0, id=1):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    '''Method get for size'''
    @property
    def size(self):
        '''return the width'''
        return self.width
    '''Method set for size'''
    @size.setter
    def size(self, value):
        '''Enter the attributes'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """number of arguments"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    """funtion dictionary"""

    def to_dictionary(self):
        """return a dictionary"""

        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
