# Задание №5
# 📌 На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

import unittest
from task_hw_1_seminar_13 import Rectangle, NegativeValueError


class TestRectangle(unittest.TestCase):
    """
    Тестирование класса Rectangle.

     Методы:
    - setUp(self) -> None: выполняется перед запуском тестов;
    - test_create_square(self): тестирование создания квадрата;
    - test_create_rectangle(self): тестирование создания прямоугольника;
    - test_edit_width(self): тестирование изменения ширины прямоугольника;
    - test_edit_height(self): тестирование изменение высоты прямоугольника;
    - test_sum(self): тестирование сложения прямоугольников;
    - test_sub(self): тестирование вычитания прямоугольников;
    - test_eq(self): тестирование сравнения прямоугольников;
    - test_area(self): тестирование вычисления площади прямоугольника.
    """

    def setUp(self) -> None:
        """
        Выполняется перед запуском теста.
        """
        self.r = Rectangle(4)
        self.rect1 = Rectangle(4, 5)
        self.rect2 = Rectangle(3, 3)

    def test_create_square(self):
        """
        Тестирование создания квадрата.
        """
        self.assertRaisesRegex(NegativeValueError, 'Ширина должна быть положительной, а не -2', Rectangle, -2)

    def test_create_rectangle(self):
        """
        Тестирование создания прямоугольника.
        """
        self.assertRaisesRegex(NegativeValueError, 'Высота должна быть положительной, а не -3', Rectangle, 5, -3)

    def test_edit_width(self):
        """
        Тестирование изменения ширины прямоугольника.
        """
        ex = None
        try:
            self.r.width = -3
        except NegativeValueError as e:
            ex = e
        self.assertEqual('NegativeValueError: Ширина должна быть положительной, а не -3', 'NegativeValueError: '
                         + ex.__str__())

    def test_edit_height(self):
        """
        Тестирование изменение высоты прямоугольника.
        """
        ex = None
        try:
            self.r.height = -3
        except NegativeValueError as e:
            ex = e
        self.assertEqual('NegativeValueError: Высота должна быть положительной, а не -3', 'NegativeValueError: '
                         + ex.__str__())

    def test_sum(self):
        """
        Тестирование сложения прямоугольников
        """
        rect_sum = self.rect1 + self.rect2
        if rect_sum.width == rect_sum.height:
            self.assertEqual(f"Квадрат со стороной 7", f"Квадрат со стороной {rect_sum.width}")
        else:
            self.assertEqual(f"Прямоугольник со сторонами 7 и 8",
                             f"Прямоугольник со сторонами {rect_sum.width} и {rect_sum.height}")

    def test_sub(self):
        """
        Тестирование вычитания прямоугольников.
        """
        rect_sum = self.rect1 - self.rect2
        if rect_sum.width == rect_sum.height:
            self.assertEqual(f"Квадрат со стороной 7", f"Квадрат со стороной {rect_sum.width}")
        else:
            self.assertEqual(f"Прямоугольник со сторонами 1 и 2",
                             f"Прямоугольник со сторонами {rect_sum.width} и {rect_sum.height}")

    def test_eq(self):
        """
        Тестирование сравнения прямоугольников.
        """
        self.assertFalse(self.rect1 == self.rect2)

    def test_area(self):
        """
        Тестирование вычисления площади прямоугольника.
        """
        area = self.rect1.area()
        self.assertEqual(20, area)


if __name__ == '__main__':
    unittest.main()
