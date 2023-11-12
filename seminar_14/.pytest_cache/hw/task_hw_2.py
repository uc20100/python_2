# Возьмите код из прошлой задачи "Класс Rectangle".
#
# Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)
#
# Тесты:
#
# test_width: Тестирование инициализации ширины. Создайте прямоугольник с шириной 5 и убедитесь, что атрибут width
# корректно установлен на 5.
#
# test_height: Тестирование инициализации ширины и высоты. Создайте прямоугольник с шириной 3 и высотой 4 и убедитесь,
# что атрибут height корректно установлен на 4.
#
# test_perimeter: Тестирование вычисления периметра. Создайте прямоугольник с шириной 5 и вычислите его периметр.
# Убедитесь, что результат равен 20.
#
# test_area: Тестирование вычисления площади. Создайте прямоугольник с шириной 3 и высотой 4 и вычислите его площадь.
# Убедитесь, что результат равен 12.
#
# test_addition: Тестирование операции сложения. Создайте два прямоугольника: один с шириной 5, другой с шириной 3 и
# высотой 4. Выполните операцию сложения r1 + r2 и убедитесь, что полученный прямоугольник имеет правильные значения
# ширины и высоты (8 и 6.0 соответственно).
#
# test_subtraction: Тестирование операции вычитания. Создайте два прямоугольника: один с шириной 10, другой с
# шириной 3 и высотой 4. Выполните операцию вычитания r1 - r2 и убедитесь, что полученный прямоугольник имеет
# правильные значения ширины и высоты (7 и 6.0 соответственно).
#
# test_negative_width: Тестирование инициализации отрицательной ширины. Попробуйте создать прямоугольник с
# отрицательной шириной (-5) и убедитесь, что это вызывает исключение NegativeValueError.
#
# test_negative_height: Тестирование инициализации отрицательной высоты. Попробуйте создать прямоугольник с шириной 5
# и отрицательной высотой (-4) и убедитесь, что это вызывает исключение NegativeValueError.
#
# test_set_width: Тестирование изменения ширины. Создайте прямоугольник с шириной 5 и измените его ширину на 10.
# Убедитесь, что атрибут width корректно изменяется на 10.
#
# test_set_negative_width: Тестирование изменения отрицательной ширины. Создайте прямоугольник с шириной 5 и
# попробуйте изменить его ширину на отрицательное значение (-10). Убедитесь, что это вызывает
# исключение NegativeValueError.
#
# test_set_height: Тестирование изменения высоты. Создайте прямоугольник с шириной 3 и высотой 4 и измените его
# высоту на 6. Убедитесь, что атрибут height корректно изменяется на 6.
#
# test_set_negative_height: Тестирование изменения отрицательной высоты. Создайте прямоугольник с шириной 3 и высотой 4
# и попробуйте изменить его высоту на отрицательное значение (-6). Убедитесь, что это вызывает
# исключение NegativeValueError.
#
# test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом. Создайте два
# прямоугольника: один с шириной 3 и высотой 4, другой с шириной 10. Попробуйте выполнить операцию вычитания r1 - r2
# и убедитесь, что это вызывает исключение NegativeValueError.
#
# test_subtraction_same_perimeter: Тестирование операции вычитания с прямоугольниками одинакового периметра.
# Создайте два прямоугольника: один с шириной 5, другой с шириной 4 и высотой 3. Выполните операцию вычитания r1 - r2
# и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты (1 и 1.0 соответственно).
#
# Используйте модуль unittest для запуска тестов. Все тесты должны выполняться успешно и не вызывать ошибок.
#
# Запускать тесты не надо, автотест это сделает сам:

import unittest


class NegativeValueError(ValueError):
    pass


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


# Введите ваше решение ниже
class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        """
        Выполняется перед запуском теста.
        """
        self.r5 = Rectangle(5)
        self.r3_4 = Rectangle(3, 4)

    def test_width(self):
        """"
        Тестирование инициализации ширины.
        """
        self.assertEqual(self.r5.width, 5)

    def test_height(self):
        """
        Тестирование инициализации ширины и высоты.
        """
        self.assertEqual(self.r3_4.height, 4)

    def test_perimeter(self):
        """
        Тестирование вычисления периметра.
        """
        self.assertEqual(self.r5.perimeter(), 20)

    def test_area(self):
        """
        Тестирование вычисления площади.
        """
        self.assertEqual(self.r3_4.area(), 12)

    def test_addition(self):
        """
        Тестирование операции сложения.
        """
        r1 = r2 = Rectangle(4)
        r = r1 + r2
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)

    def test_subtraction(self):
        """
        Тестирование операции вычитания.
        """
        r1 = Rectangle(10)
        r = r1 - self.r3_4
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 6)

    def test_negative_width(self):
        """
        Тестирование инициализации отрицательной ширины.
        """
        self.assertRaisesRegex(NegativeValueError, 'Ширина должна быть положительной, а не -5', Rectangle, -5)

    def test_negative_height(self):
        """
        Тестирование инициализации отрицательной высоты.
        """
        self.assertRaisesRegex(NegativeValueError, 'Высота должна быть положительной, а не -4', Rectangle, 5, -4)

    def test_set_width(self):
        """
        Тестирование изменения ширины.
        """
        self.r5.width = 10
        self.assertEqual(self.r5.width, 10)

    def test_set_negative_width(self):
        """
        Тестирование изменения отрицательной ширины.
        """
        ex = None
        try:
            self.r5.width = -10
        except NegativeValueError as e:
            ex = e
        self.assertEqual('NegativeValueError: Ширина должна быть положительной, а не -10', 'NegativeValueError: '
                         + ex.__str__())

    def test_set_height(self):
        """
        Тестирование изменения высоты.
        """
        self.r3_4.height = 6
        self.assertEqual(self.r3_4.height, 6)

    def test_set_negative_height(self):
        """
        Тестирование изменения отрицательной высоты.
        """
        ex = None
        try:
            self.r3_4.height = -6
        except NegativeValueError as e:
            ex = e
        self.assertEqual('NegativeValueError: Высота должна быть положительной, а не -6', 'NegativeValueError: '
                         + ex.__str__())


if __name__ == '__main__':
    unittest.main()