"""
Модуль декоратора с параметрами.
"""
# Задание №4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable

__all__ = ['print_str']


def count_print(count: int):
    """
    Декоратор с параметрами.

    :param count: Количество выполнений декорируемой функции.
    :return:
    """
    def decor(func: Callable):
        def run_func(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return run_func
    return decor


@count_print(10)
def print_str(in_str: str):
    print(in_str)


if __name__ == '__main__':
    print_str('Hello World!')
