"""
Модуль домашнего задания.
"""
# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой
# строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
#
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
#
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:
#
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
#
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
#
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет
# следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c
# и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена
# нформация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.


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
