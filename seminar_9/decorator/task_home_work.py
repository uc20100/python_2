"""
Модуль домашнего задания.
"""
# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
# 📌 Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса


import random
import csv
import json
from typing import Callable

__all__ = ['save_to_json', 'generate_csv_file', 'find_roots']


def save_to_json(func: Callable):
    def calc(*args, **kwargs):
        with open(args[0], 'r', encoding='utf-8') as f_read, open('results.json', 'w', encoding='utf-8') as f_write:
            csv_read = list(csv.reader(f_read))
            json_list = []
            for item in csv_read:
                a, b, c = item
                a, b, c = int(a), int(b), int(c)
                result_func = func(a, b, c)
                json_list.append({'a': a, 'b': b, 'c': c, 'result': result_func})
            json.dump(json_list, f_write)

    return calc


def generate_csv_file(csv_wr: str, rows: int):
    """
    Функция генерации 3-х рандомных чисел.

    :param csv_wr: Файл данных CSV
    :param rows: Количество строк
    :return:
    """
    with open(csv_wr, 'w', encoding='utf-8', newline='') as f_write:
        csv_write = csv.writer(f_write, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for _ in range(rows):
            date_list = [random.randint(1, 100) for _ in range(3)]
            csv_write.writerow(date_list)


@save_to_json
def find_roots(a: int, b: int, c: int):
    """
    Решение квадратного уравнения ax^2 + bx + c = 0.

    :param a: Коэффициент а,
    :param b: Коэффициент b,
    :param c: Коэффициент c,
    :return: корни квадратного уравнения.
    """
    # дискриминант - D = b^2 − 4ac
    d = b * b - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    else:
        return False


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 1501)
    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 1501)
