# Задание №2
# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json


class Factorial:
    """
    Класс для вычисления факториала и хранении истории вычислений.

    Атрибуты:
    k_value (int): количество последних значений хранящихся в памяти
    factorial_dict (dict): история вычислений

     Dunder методы:
     __init__(self, k_value): инициализация объекта.
     __str__(): возвращает строковое представление истории вычислений.
     __repr__(): возвращает строковое представление объекта класса для отладки.
     __call__(self, number): вычисление факториала и сохранение истории вычислений.
     __enter__(): выполняет действия при входе в менеджер контекста.
     __exit__(self, exc_type, exc_val, exc_tb): выполняет действия при выходе из менеджера контекста.
    """

    def __init__(self, k_value, name_json: str = None):
        """
        Инициализация класса.

        :param k_value: количество последних значений хранящихся в памяти
        :param name_json: имя файла JSON для хранения истории вычислений
        """
        self.k_value = k_value
        self.factorial_dict = {}
        self.name_json = name_json

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

    def __enter__(self):
        """
        Функция выполняет действия при входе в менеджер контекста.

        :return:
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Функция выполняет действия при выходе из менеджера контекста.

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        if not self.name_json:
            f = open('noname.json', 'w', encoding='utf-8')
        else:
            f = open(self.name_json, 'w', encoding='utf-8')
        json.dump(self.factorial_dict, f)
        # f.close()


if __name__ == '__main__':
    value_1 = Factorial(5, 'value_1.json')

    with value_1:
        value_1(8)
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
    value_2 = Factorial(4)
    value_2(0)
    value_2(1)
    value_2(2)
    value_2(3)
    value_2(4)
    value_2(5)
    with value_2:
        value_2(0)
    print(value_2)
