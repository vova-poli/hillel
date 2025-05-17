import math
from src.figure import Figure

class Triangle(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.__side ** 2

    def perimeter(self):
        return 3 * self.__side