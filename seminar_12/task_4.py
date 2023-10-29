# Задание №4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.

class Rectangle:
    """
    Класс, представляющий прямоугольник.

     Атрибуты:
    - _width (int): ширина прямоугольника,
    - _length (int): длина прямоугольника.

     Методы:
    - perimeter(): вычисляет периметр прямоугольника,
    - area(): вычисляет площадь прямоугольника.

     Dunder методы:
    - __add__(other): определяет операцию сложения двух прямоугольников,
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого,
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников,
    - __eq__(other): определяет операцию "равно" для двух прямоугольников,
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников,
    - __str__(): возвращает строковое представление прямоугольника,
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

     Декораторы свойств:
    - @property length(self): возвращает длину прямоугольника,
    - @property width(self): возвращает ширину прямоугольника,
    - @length.setter length(self, value): задает длину прямоугольника,
    - @width.setter width(self, value): задает ширину прямоугольника.
    """

    def __init__(self, length, width=None):
        self._length = length
        self._width = width

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        :return: периметр прямоугольника
        """
        if self._width is None:
            return 4 * self._length
        else:
            return 2 * (self._length + self._width)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        :return: площадь прямоугольника
        """
        if self._width is None:
            return self._length ** 2
        else:
            return self._length * self._width

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        :param other: второй прямоугольник (Rectangle)
        :return: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        if self._width is None:
            s_width = self._length
        else:
            s_width = self._width
        if other._width is None:
            o_width = other._lenght
        else:
            o_width = other._width
        if (self._length + other._length) == (s_width + o_width):
            return Rectangle((self._length + other._length), None)
        else:
            return Rectangle((self._length + other._length), (s_width + o_width))

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        :param other: вычитаемый прямоугольник (Rectangle)
        :return: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self._width is None:
            s_width = self._length
        else:
            s_width = self._width
        if other._width is None:
            o_width = other._lenght
        else:
            o_width = other._width
        if abs(self._length - other._length) == abs(s_width - o_width):
            return Rectangle(abs(self._length - other._length), None)
        else:
            return Rectangle(abs(self._length - other._length), abs(s_width - o_width))

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        :param other: второй прямоугольник (Rectangle)
        :return: True, если равны, иначе False
        """
        return self._length == other._length and self.perimeter() == other.perimeter()

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        :param other: второй прямоугольник (Rectangle)
        :return: True, если периметр первого прямоугольника меньше периметра второго, иначе False
        """
        return self.perimeter() < other.perimeter()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        :param other: второй прямоугольник (Rectangle)
        :return: True, если периметр первого прямоугольника меньше или равно периметру второго, иначе False
        """
        return self.perimeter() <= other.perimeter()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        :return: строковое представление прямоугольника
        """
        if self._width is None:
            return f'Квадрат со стороной {self._length}'
        else:
            return f'Прямоугольник со сторонами {self._length} и {self._width}'

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        :return: строковое представление прямоугольника
        """
        return f'{Rectangle.__name__}({self._length}, {self._width})'

    @property
    def length(self):
        """
        Возвращает длину прямоугольника.

        :return: длина прямоугольника
        """
        return self._length

    @property
    def width(self):
        """
        Возвращает ширину прямоугольника.

        :return: ширина прямоугольника
        """
        return self._width

    @length.setter
    def length(self, value):
        """
        Устанавливает длину прямоугольника.

        :param value: длина прямоугольника
        :return:
        """
        if value > 0:
            self.length = value
        else:
            raise ValueError('Значение должно быть больше нуля')

    @width.setter
    def width(self, value):
        """
        Устанавливает ширину прямоугольника.

        :param value: ширина прямоугольника
        :return:
        """
        if value > 0:
            self._length = value
        else:
            raise ValueError('Значение должно быть больше нуля')


if __name__ == '__main__':
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 3)

    print(rect1)
    print(rect2)

    print(rect1.perimeter())
    print(rect1.area())
    print(rect2.perimeter())
    print(rect2.area())

    rect_sum = rect1 + rect2
    rect_diff = rect1 - rect2

    print(rect_sum)
    print(rect_diff)

    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)

    print(repr(rect1))
    print(repr(rect2))

    print(rect1.width)
    rect1.length = 0

