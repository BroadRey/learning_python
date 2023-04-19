# ДЗ**
class Figure:
    unit = 'mm'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length
        self.__perimeter = self.calculate_perimeter()

    def calculate_perimeter(self):
        return self.__side_length * 4

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(
            f'Square side length: {str(self.__side_length) + Square.unit}, '
            f'perimeter: {str(self.__perimeter) + Square.unit}, '
            f'area: {str(self.calculate_area()) + Square.unit}')


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__perimeter = self.calculate_perimeter()

    def calculate_perimeter(self):
        return self.__length * 2 + self.__width * 2

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(
            f'Rectangle length: {str(self.__length) + Square.unit}, '
            f'width: {str(self.__width) + Square.unit}, '
            f'area: {str(self.calculate_area()) + Square.unit}')


figures = [Square(3), Square(5), Rectangle(2, 3),
           Rectangle(7, 2), Rectangle(5, 1)]

for figure in figures:
    figure.info()