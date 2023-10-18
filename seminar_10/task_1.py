# Задание №1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    my_circle = Circle(5)
    print(f'{my_circle.length() = }')
    print(f'{my_circle.area() = }')
