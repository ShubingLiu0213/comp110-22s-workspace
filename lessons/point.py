from __future__ import annotations


class Point:
    """Model a 2D Point."""

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Intialize a Point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factors."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point."""
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled

    def __str__(self) -> str:
        """Produce a str represntion of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str represntion of a Point for python!."""
        return f"Point({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Overload the mu;tiplication operator for Point * float."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")

p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)
p1: Point = p0.scale(2.0)
print(p0)
print(p1)
p1_as_a_str: str = str(p1)
print(p1_as_a_str)
print(f"({p0.x}, {p0.y})")
print(f"({p1.x}, {p1.y})") 
p1_repr: str = repr(p1)
print(p1_repr)
