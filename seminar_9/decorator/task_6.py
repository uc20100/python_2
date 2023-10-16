"""
Модуль множественного декорирования с декоратором wraps.
"""
# Задание №6
# 📌 Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

from typing import Callable
import random
import json
from pathlib import Path
from functools import wraps

__all__ = ['guess']


def check(func: Callable):
    """
    Декоратор, проверки параметров.

    :param func: Функция угадывания числа,
    :return: возвращает функцию.
    """
    @wraps(func)
    def check_setting(*args, **kwargs):
        num, att = args
        if not (1 <= num <= 1_000):
            num = random.randint(1, 1_000)
        if not (1 <= att <= 10):
            att = random.randint(1, 10)
        return func(num, att, **kwargs)

    return check_setting


def save_json(write_fie: str = 'info_decor.json'):
    """
    Декоратор сохранения в файл JSON.

    :param write_fie: Файл JSON
    :return:
    """

    def wrapper_1(func: Callable):

        @wraps(func)
        def write_json(*args, **kwargs):
            """
            Функция записи JSON файла.

            :param args: Позиционные аргументы,
            :param kwargs: ключевые аргументы,
            :return: результат работы функции.
            """
            load_list = []
            info_dict = {}
            p = Path(Path.cwd() / write_fie)
            for item in Path.cwd().iterdir():
                if item == p and item.is_file():
                    with open(p, 'r', encoding='utf-8') as f_read:
                        load_list = json.load(f_read)
            info_dict['args_func'] = args
            info_dict['kwargs_func'] = kwargs
            result_func = func(*args, **kwargs)
            info_dict['return_func'] = result_func
            load_list.append(info_dict)
            with open(p, 'w', encoding='utf-8') as f_write:
                json.dump(load_list, f_write, ensure_ascii=False)
            return result_func

        return write_json

    return wrapper_1


def count_print(count: int = 5):
    """
    Декоратор количества запуска функции.

    :param count: Количество выполнений декорируемой функции.
    :return:
    """

    def wrapper_2(func: Callable):
        @wraps(func)
        def count_func(*args, **kwargs):
            rez_str = None
            for i in range(count):
                print(f'\nЦикл №{i + 1}')
                rez_str = func(*args, **kwargs)
                print(rez_str)
            return rez_str

        return count_func

    return wrapper_2


@count_print(3)
@save_json('guess.json')
@check
def guess(number: int, attempts: int, /, *, inf_str: str):
    """
    Функция угадывания числа.

    :param number: Загаданное число,
    :param attempts: количество попыток,
    :param inf_str: информационная строка.
    """
    for i in range(attempts):
        number_ = input(f'Введите число: ')
        if number_.isdigit():
            if number == int(number_):
                return inf_str + 'Ура вы угадали!'
            else:
                if attempts - i - 1:
                    print(f'Не угадали, осталось {attempts - i - 1} попыток.')
                else:
                    return inf_str + 'Не угадали, попытки исчерпаны'
        else:
            if attempts - i - 1:
                print(f'Введите натуральное число. Осталось {attempts - i - 1} попыток.')
            else:
                return inf_str + 'Не угадали, попытки исчерпаны'


if __name__ == '__main__':
    help(guess)
    guess(100, 3, inf_str='Результат: ')
