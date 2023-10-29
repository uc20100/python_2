# Задание №3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class Value:
    """
        Дескриптор класса Generator.

         Dunder методы:
         __set_name__(self, owner, name): вызывается при создании атрибута класса.
         __set__(self, instance, value): выполняет действие при задании значения атрибуту класса.
         __get__(self, instance, owner): выполняет действие при обращении к атрибуту класса.

        Функции:
        validate(value): валидация атрибута класса.
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
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if value is not None and value < 1:
            raise ValueError(f'Значение {value} должно быть больше или равно 1')


class Generator:
    """
    Класс для генерации значений факториала.

    Атрибуты:
    stop (int): начальное значение числа
    start (int): конечное значение числа
    step (int): шаг генерации

    Dunder методы:
    __iter__(self): итератор объекта.
    __next__(self): шаг итератора.
    """

    stop = Value()
    start = Value()
    step = Value()

    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.stop = stop
        self.start = start
        self.step = step
        self._count = start

    def __iter__(self):
        """
        Функция итератора объекта.

        :return:
        """
        return self

    def __next__(self):
        """
        Функция шага итератора, возвращает значение факториала.

        :return:
        """
        while self._count <= self.stop:
            factorial = 1
            for _i in range(1, self._count + 1):
                factorial *= _i
            print(f'Факториал числа: {self._count}, равен: {factorial:_}')
            self._count += self.step
            return factorial
        raise StopIteration


if __name__ == '__main__':
    gen = Generator(10, 2, 2)
    for i in gen:
        print(f'Значение итератора: {i:_}')
