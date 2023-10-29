# Задание №6
# 📌 Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Value:
    """
    Дескриптор класса Rectangle.

     Dunder методы:
    - __set_name__(self, owner, name): вызывается при создании атрибута класса,
    - __set__(self, instance, value): выполняет действие при задании значения атрибуту класса,
    - __get__(self, instance, owner): выполняет действие при обращении к атрибуту класса.

     Функции:
    - validate(value): валидация атрибута класса.
    """

    def __set_name__(self, owner, name):
        """
        Функция вызывается при создании атрибута класса.

        :param owner:
        :param name:
        :return:
        """
        self.param_name = '_' + name

    def __set__(self, instance, value):
        """
        Функция выполняет действие при задании значения атрибуту класса.

        :param instance:
        :param value:
        :return:
        """
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        """
        Функция выполняет действие при обращении к атрибуту класса.

        :param instance:
        :param owner:
        :return:
        """
        return getattr(instance, self.param_name)

    @staticmethod
    def validate(value):
        """
        Функция валидирует значения атрибута.

        :param value:
        :return:
        """
        if value is not None and value <= 0:
            raise ValueError('Значение должно быть больше нуля')


class Rectangle:
    """
    Класс, представляющий прямоугольник.

     Атрибуты:
    - width (int): ширина прямоугольника,
    - length (int): длина прямоугольника.

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

    """
    # Экономим память
    # __slots__ = ('_length', '_width')
    length = Value()
    width = Value()

    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        :return: периметр прямоугольника
        """
        if self.width is None:
            return 4 * self.length
        else:
            return 2 * (self.length + self.width)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        :return: площадь прямоугольника
        """
        if self.width is None:
            return self.length ** 2
        else:
            return self.length * self.width

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        :param other: второй прямоугольник (Rectangle)
        :return: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        if self.width is None:
            s_width = self.length
        else:
            s_width = self.width
        if other._width is None:
            o_width = other._length
        else:
            o_width = other._width
        if (self.length + other.length) == (s_width + o_width):
            return Rectangle((self.length + other.length), None)
        else:
            return Rectangle((self.length + other.length), (s_width + o_width))

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        :param other: вычитаемый прямоугольник (Rectangle)
        :return: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.width is None:
            s_width = self.length
        else:
            s_width = self.width
        if other._width is None:
            o_width = other._length
        else:
            o_width = other._width
        if abs(self.length - other.length) == abs(s_width - o_width):
            return Rectangle(abs(self.length - other.length), None)
        else:
            return Rectangle(abs(self.length - other.length), abs(s_width - o_width))

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        :param other: второй прямоугольник (Rectangle)
        :return: True, если равны, иначе False
        """
        return self.length == other.length and self.perimeter() == other.perimeter()

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
        if self.width is None:
            return f'Квадрат со стороной {self.length}'
        else:
            return f'Прямоугольник со сторонами {self.length} и {self.width}'

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        :return: строковое представление прямоугольника
        """
        return f'{Rectangle.__name__}({self.length}, {self.width})'


if __name__ == '__main__':
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3)

    print(rect1)
    print(rect2)

    print(rect1.perimeter())
    print(rect1.area())
    print(rect2.perimeter())
    print(rect2.area())

    print('\nСложение:')
    rect_sum = rect1 + rect2
    print(rect1)
    print(rect2)
    print(rect_sum)

    print('\nВычитание:')
    rect_diff = rect1 - rect2
    print(rect1)
    print(rect2)
    print(rect_diff)
    print()

    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)

    print(repr(rect1))
    print(repr(rect2))

    print(rect1.__dict__)
    print(rect2.__dict__)
    print(rect1)
    print(rect2)
