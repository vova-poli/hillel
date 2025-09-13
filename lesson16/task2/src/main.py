from rectangle import Rectangle
from circle import Circle
from triangle import Triangle

figures = [
    Rectangle(4, 5),
    Circle(3),
    Triangle(6)
]

for figure in figures:
    print(f"{figure.__class__.__name__}:")
    print(f"  Площа: {figure.area():.2f}")
    print(f"  Периметр: {figure.perimeter():.2f}")
