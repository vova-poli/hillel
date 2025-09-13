from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle
import math

def test_rectangle():
    r = Rectangle(4, 5)
    assert r.area() == 20
    assert r.perimeter() == 18

def test_circle():
    c = Circle(3)
    assert round(c.area(), 2) == round(math.pi * 9, 2)
    assert round(c.perimeter(), 2) == round(2 * math.pi * 3, 2)

def test_triangle():
    t = Triangle(6)
    expected_area = (math.sqrt(3) / 4) * 6**2
    assert round(t.area(), 2) == round(expected_area, 2)
    assert t.perimeter() == 18