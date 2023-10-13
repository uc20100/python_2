"""
Модуль угадывания числа.
"""
# Задание №1
# 📌 Создайте функцию-замыкание, которая запрашивает два целых
# числа:
#   ○ от 1 до 100 для загадывания,
#   ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

__all__ = ['start_guess']

from typing import Callable


def start_guess(number: int) -> Callable[[int], str]:
    """
    Функция замыкание, угадывание числа.

    :param number: Загаданное число,
    :return: возвращает функцию
    """
    status = False
    if not (1 <= number <= 1_000):
        print('Число должно быть в пределах от 1 до 1_000.')
    else:
        status = True

    def guess(attempts: int) -> str:
        """
        Функция угадывания числа.

        :param attempts: Число попыток,
        :return: возвращает строковый результат.
        """
        if status:
            if 1 <= attempts <= 10:
                for i in range(attempts):
                    number_ = input(f'Введите число: ')
                    if number_.isdigit():
                        if number == int(number_):
                            return 'Ура вы угадали!'
                        else:
                            print(f'Не угадали, осталось {attempts - i - 1} попыток.')
                    else:
                        print(f'Введите натуральное число. Осталось {attempts - i - 1} попыток.')
                else:
                    return 'Попытки исчерпаны ('
        return 'Параметры функции ошибочны.'

    return guess


func = start_guess(100)
print(func(5))
