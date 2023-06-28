#!/usr/bin/python3
"""import class Rectangle"""
from models.rectangle import Rectangle


"""Create class"""


class Square(Rectangle):
    """Create constructor"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    """Getter"""
    @property
    def size(self):
        return self.width

    """setter value"""
    @size.setter
    def size(self, value):
        self.height = value
        self.width = value
