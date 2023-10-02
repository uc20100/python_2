"""
Модуль генерации случайных чисел
"""
# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

__all__ = ['random_number']
import random as rnd


def random_number(name: str, lines: int):
    """
    Функция заполняет файл случайными числами.

    :param name: имя файла
    :param lines: количество строк
    :return:
    """
    with open(f'{name}', 'a', encoding='utf-8') as f:
        for _ in range(lines):
            print(f'{rnd.randint(-1_000, 1000)} | {rnd.uniform(-1_000, 1_000)}', file=f)


if __name__ == '__main__':
    random_number('numbers.txt', 8)
