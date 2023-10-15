"""
Модуль угадывания числа 2.
"""
# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from typing import Callable
import random

__all__ = ['guess']


def check(func: Callable):
    """
    Декоратор, угадывание числа.

    :param func: Функция угадывания числа,
    :return: возвращает функцию.
    """

    def check_setting(*args):
        nonlocal func
        num, att = args
        if not (1 <= num <= 1_000):
            num = random.randint(1, 1_000)
        if not (1 <= att <= 10):
            att = random.randint(1, 10)
        return func(num, att)

    return check_setting


@check
def guess(number: int, attempts: int) -> str:
    """
    Функция угадывания числа.

    :return: Возвращает строковый результат.
    """
    for i in range(attempts):
        number_ = input(f'Введите число: ')
        if number_.isdigit():
            if number == int(number_):
                return 'Ура вы угадали!'
            else:
                if attempts - i - 1:
                    print(f'Не угадали, осталось {attempts - i - 1} попыток.')
                else:
                    return 'Не угадали, попытки исчерпаны'
        else:
            if attempts - i - 1:
                print(f'Введите натуральное число. Осталось {attempts - i - 1} попыток.')
            else:
                return 'Не угадали, попытки исчерпаны'


if __name__ == '__main__':
    print(guess(100, 3))
