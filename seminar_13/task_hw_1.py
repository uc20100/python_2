# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, которое выбрасывается при
# некорректных значениях ширины и высоты, как при создании объекта, так и при установке их через сеттеры

class UsException(BaseException):
    pass


class NegativeValueError(UsException):
    """
    Класс ошибки значения переменной.

     Атрибуты:
    - self.value: название переменной в которой произошла ошибка.

     Dunder методы:
    - __init__(self, value): конструктор класса,
    - __str__(self): возвращает строковое представление ошибки.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Параметр '{self.value[1:]}' должен быть больше нуля."


class Value:
    """
        Дескриптор класса Rectangle.

         Методы:
        - validate(self, value): валидация значений атрибутов класса.

         Dunder методы:
        - __init__(self, value=None): конструктор класса,
        - __set_name__(self, owner, name): вызывается при создании атрибута класса,
        - __set__(self, instance, value): выполняет действие при задании значения атрибуту класса,
        - __get__(self, instance, owner): выполняет действие при обращении к атрибуту класса.
        """

    def __init__(self, value=None):
        self.value = value

    def __set_name__(self, owner, name):
        """
        Функция выполняет действие при создании атрибута класса.

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
        Функция выполняет действие при чтении атрибуту класса.

        :param instance:
        :param owner:
        :return:
        """
        return getattr(instance, self.param_name)

    def validate(self, value):
        """
        Функция валидирует значения атрибута.

        :param value:
        :return:
        """
        if value is None or value <= 0:
            raise NegativeValueError(self.param_name)


class Rectangle:
    """
    Класс, представляющий прямоугольник.

     Атрибуты:
    - width (int): ширина прямоугольника,
    - height (int): высота прямоугольника.

     Методы:
    - perimeter(): вычисляет периметр прямоугольника,
    - area(): вычисляет площадь прямоугольника.

     Dunder методы:
    - __init__(self, width, height=None): конструктор класса,
    - __add__(other): определяет операцию сложения двух прямоугольников,
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого,
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников,
    - __eq__(other): определяет операцию "равно" для двух прямоугольников,
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников,
    - __str__(): возвращает строковое представление прямоугольника,
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.
    """

    width = Value()
    height = Value()

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


if __name__ == '__main__':
    r = Rectangle(1, 1)
    r.width = 1
