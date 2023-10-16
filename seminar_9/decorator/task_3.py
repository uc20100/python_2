"""
Модуль декоратора с записью в JSON файл
"""
# Задание №3
# 📌 Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# 📌 Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой
# функции.

import random
from functools import wraps
from typing import Callable
import json
from pathlib import Path

__all__ = ['decor_to_json']


def decor(write_fie: str = 'info_decor.json'):
    """
    Функция параметров декоратора.

    :param write_fie: Файл JSON
    :return:
    """
    def info_func(func: Callable):
        """
        Функция декоратор.

        :param func: Декорируемая функция
        :return:
        """

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
            info_dict['name_func'] = func.__name__
            info_dict['args_func'] = args
            info_dict['kwargs_func'] = kwargs
            result_func = func(*args, **kwargs)
            info_dict['return_func'] = result_func
            load_list.append(info_dict)
            with open(p, 'w', encoding='utf-8') as f_write:
                json.dump(load_list, f_write, ensure_ascii=False)
            return result_func

        return write_json

    return info_func


@decor()
def decor_to_json(rand_min: int, rand_max: int, /, *, info_str: str) -> str:
    """
    Функция для декорирования.

    :param rand_min: Минимальный предел рандомного числа,
    :param rand_max: максимальный предел рандомного числа,
    :param info_str: строка информации,
    :return: результирующая строка.
    """
    return info_str + ' ' + str(random.randint(rand_min, rand_max))


if __name__ == '__main__':
    print(decor_to_json(1, 10, info_str='Результат'))
