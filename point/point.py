class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and \
                   self.y == other.y and \
                   self.z == other.z
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other, self.z * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'
