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

from typing import Callable

__all__ = ['go_guess']


def go_guess(number: int, attempts: int) -> Callable[[], str]:
    """
    Функция замыкание, угадывание числа.

    :param number: Загаданное число,
    :param attempts: число попыток,
    :return: возвращает функцию.
    """
    return_str = None
    if not (1 <= number <= 1_000):
        return_str = 'Значение number должно быть в пределах от 1 до 1_000.'
    else:
        if not (1 <= attempts <= 10):
            return_str = 'Значение attempts должно быть в пределах от 1 до 10.'

    def guess() -> str:
        """
        Функция угадывания числа.

        :return: Возвращает строковый результат.
        """
        nonlocal return_str
        if not return_str:
            for i in range(attempts):
                number_ = input(f'Введите число: ')
                if number_.isdigit():
                    if number == int(number_):
                        return_str = 'Ура вы угадали!'
                        break
                    else:
                        if attempts - i - 1:
                            print(f'Не угадали, осталось {attempts - i - 1} попыток.')
                        else:
                            return_str = 'Не угадали, попытки исчерпаны'
                else:
                    if attempts - i - 1:
                        print(f'Введите натуральное число. Осталось {attempts - i - 1} попыток.')
                    else:
                        return_str = 'Не угадали, попытки исчерпаны'
        return return_str

    return guess


if __name__ == '__main__':
    func = go_guess(100, 3)
    print(func())
