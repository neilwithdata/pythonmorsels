import math


class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self._radius * self._radius

    @area.setter
    def area(self, value):
        raise AttributeError("can't set attribute")

    def __repr__(self):
        return f'Circle({self._radius})'
