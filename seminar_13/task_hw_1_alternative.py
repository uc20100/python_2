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

if __name__ == '__main__':
    r1 = Rectangle(5)
    r2 = Rectangle(3,4)
    r3 = r1 - r2
    print(r3.width, r3.height)
    # Ожидаемый ответ:
    # __main__.NegativeValueError: Ширина должна быть положительной, а не -2

    # r = Rectangle(5, -3)
    # Ожидаемый ответ:
    # __main__.NegativeValueError: Высота должна быть положительной, а не -3

    # r = Rectangle(4, 4)
    # r.width = -3
    # Ожидаемый ответ:
    # __main__.NegativeValueError: Ширина должна быть положительной, а не -3

    # r = Rectangle(4, 4)
    # r.height = -3
    # Ожидаемый ответ:
    # __main__.NegativeValueError: Высота должна быть положительной, а не -3