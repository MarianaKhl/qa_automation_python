from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length   # private

    def get_area(self):
        return f"Square area = {self.__side_length ** 2}:"

    def get_perimeter(self):
        return f"Square perimeter = {self.__side_length * 4}."


class Rectangle(Shape):
    def __init__(self, wight, height):
        self.__wight = wight
        self.__height = height

    def get_area(self):
        return f"Rectangle area = {self.__wight * self.__height}:"

    def get_perimeter(self):
        return f"Rectangle perimeter = {(self.__wight + self.__height) * 2}."


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return f"Circle area = {3.14159 * self.__radius ** 2}:"

    def get_perimeter(self):
        return f"Circle perimeter = {2 * 3.14159 * self.__radius}."

shapes = [Square(4), Rectangle(6, 12), Circle(3)]

for shape in shapes:
    print(shape.get_area(), shape.get_perimeter())

