# Задание №1
# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


class Factorial:
    """
    Класс для вычисления факториала и хранении истории вычислений.

     Атрибуты:
    - k_value (int): количество последних значений хранящихся в памяти,
    - factorial_dict (dict): история вычислений.

     Dunder методы:
    - __str__(): возвращает строковое представление истории вычислений,
    - __repr__(): возвращает строковое представление объекта класса для отладки,
    - __call__(self, number): вычисление факториала и сохранение истории вычислений.

    """

    def __init__(self, k_value: int):
        self.k_value = k_value
        self.factorial_dict = {}

    def __call__(self, number):
        """
        Функция считает факториал.

        :param number: число от которого нужен факториал
        :return:
        """
        factorial = 1
        if number < 0:
            raise ValueError('Число должно быть > 0')
        if number > 1:
            for i in range(1, number + 1):
                factorial *= i
        self.factorial_dict[number] = factorial
        if len(self.factorial_dict) > self.k_value:
            key_item = iter(self.factorial_dict.keys())
            self.factorial_dict.pop(next(key_item))

    def __str__(self):
        """
        Возвращает строковое представление истории вычислений.

        :return:
        """
        return '\n'.join([f'Число: {item[0]}, Факториал: {item[1]}' for item in self.factorial_dict.items()])


if __name__ == '__main__':
    value_1 = Factorial(5)
    value_1(7)
    value_1(0)
    value_1(1)
    value_1(2)
    value_1(3)
    value_1(4)
    value_1(5)
    value_1(6)
    value_1(10)
    print(value_1)

    print()
    value_2 = Factorial(3)
    value_2(0)
    value_2(1)
    value_2(2)
    value_2(3)
    value_2(4)
    value_2(5)
    print(value_2)
