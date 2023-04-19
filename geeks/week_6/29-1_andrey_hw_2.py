from math import pi


class Figure:
    unit = 'mm'

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return round(pi * self.__radius ** 2, 2)

    def info(self):
        print(
            f'Circle radius: {str(self.__radius) + Circle.unit}, '
            f'area: {str(self.calculate_area()) + Circle.unit}')


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        print(
            f'RightTriangle side a: {str(self.__side_a) + Circle.unit}, '
            f'side b: {str(self.__side_b) + Circle.unit}, '
            f'area: {str(self.calculate_area()) + RightTriangle.unit}')


figures = [Circle(4), Circle(2),
           RightTriangle(1, 5), RightTriangle(5, 8), RightTriangle(10, 4)]

for figure in figures:
    figure.info()