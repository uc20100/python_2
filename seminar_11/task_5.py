# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

from fractions import Fraction


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def perimeter(self):
        if self.width is None:
            return 4 * self.length
        else:
            return 2 * (self.length + self.width)

    def area(self):
        if self.width is None:
            return self.length ** 2
        else:
            return self.length * self.width

    def __add__(self, other):
        len_res = (self.perimeter() + other.perimeter()) / 4
        return Rectangle(len_res)

    def __sub__(self, other):
        len_squ = abs(self.perimeter() - other.perimeter()) / 4
        return Rectangle(len_squ)


if __name__ == '__main__':
    rest = Rectangle(5, 10)
    print(f'{rest.perimeter() = }')
    print(f'{rest.area() = }')

    square = Rectangle(5)
    print(f'{square.perimeter() = }')
    print(f'{square.area() = }')

    sum_rest = rest + square
    print(f'{sum_rest.length = } {sum_rest.width = } {sum_rest.perimeter() = }')

    sum_rest = square - rest
    print(f'{sum_rest.length = } {sum_rest.width = } {sum_rest.perimeter() = }')