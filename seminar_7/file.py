# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random as rnd


def write_random_number(name: str, lines: int):
    """
    Функция заполняет файл случайными числами

    :param name: имя файла
    :param lines: количество строк
    :return:
    """
    with open(f'{name}.txt', 'a', encoding='utf-8') as f:
        for _ in range(lines):
            print(f'{rnd.randint(-1_000, 1000)} | {round(rnd.uniform(-1_000, 1_000), 2)}', file=f)


if __name__ == '__main__':
    write_random_number('example', 10)
