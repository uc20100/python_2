# Задание №2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

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


if __name__ == '__main__':
    rest = Rectangle(5, 10)
    print(f'{rest.perimeter() = }')
    print(f'{rest.area() = }')

    square = Rectangle(5)
    print(f'{square.perimeter() = }')
    print(f'{square.area() = }')

