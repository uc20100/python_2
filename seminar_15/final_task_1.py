"""
Задача из семинара 6. Расставить 8-ь ферзей, чтобы они не били друг друга.
"""
# Координаты фигур на шахматной доске
#     1  2  3  4  5  6  7  8
# 1|  11 12 13 14 15 16 17 18
# 2|  21 22 23 24 25 26 27 28
# 3|  31 32 33 34 35 36 37 38
# 4|  41 42 43 44 45 46 47 48
# 5|  51 52 53 54 55 56 57 58
# 6|  61 62 63 64 65 66 67 68
# 7|  71 72 73 74 75 76 77 78
# 8|  81 82 83 84 85 86 87 88

__all__ = ['random_queen']

import random as rnd
import logging
import argparse

logging.basicConfig(format='{levelname:<8} - {asctime}. {msg}',
                    style='{',
                    filename='queen_placement.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

logger_val = logging.getLogger(__name__)


def _location_queen(location: int) -> set[int]:
    """
    Функция вычисляет все возможные локации ферзя.

    :param location: текущая локация ферзя
    :return: список возможных локаций
    """
    # Ходы как ладья слева на право
    location_1 = [(location // 10) * 10 + i for i in range(1, 9, 1)]
    # Ходы как ладья сверху вниз
    location_2 = [(location % 10) + i * 10 for i in range(1, 9, 1)]
    # Ходы как у слона, слева на право
    location_3 = []
    next_location = location
    while not (next_location // 10 == 8 or next_location % 10 == 1):
        next_location += 9
    location_3.append(next_location)
    while not (next_location // 10 == 1 or next_location % 10 == 8):
        next_location -= 9
        location_3.append(next_location)
    # Ходы как у слона, справа на лево
    location_4 = []
    next_location = location
    while not (next_location // 10 == 8 or next_location % 10 == 8):
        next_location += 11
    location_4.append(next_location)
    while not (next_location // 10 == 1 or next_location % 10 == 1):
        next_location -= 11
        location_4.append(next_location)

    return set(location_1 + location_2 + location_3 + location_4)


def _beating_queen(queen_1: int, queen_2: int, queen_3: int, queen_4: int,
                   queen_5: int, queen_6: int, queen_7: int, queen_8: int) -> bool:
    """
    Функция определяет есть ли бьющая пара ферзей.

    :param queen_1: локация ферзя 1;
    :param queen_2: локация ферзя 2;
    :param queen_3: локация ферзя 3;
    :param queen_4: локация ферзя 4;
    :param queen_5: локация ферзя 5;
    :param queen_6: локация ферзя 6;
    :param queen_7: локация ферзя 7;
    :param queen_8: локация ферзя 8;
    :return: True если такая пара есть, False если нет.
    """
    queen_placement = {queen_1, queen_2, queen_3, queen_4, queen_5, queen_6, queen_7, queen_8}

    for item_ in queen_placement:
        item_set = {item_}
        if not ((_location_queen(item_) & queen_placement - item_set) == set()):
            return False
    return True


def random_queen(number_options: int):
    """
    Функция случайной расстановки 8 ферзей, чтобы они не били друг друга.

    :param number_options: количество вариантов расстановок.
    """
    units = [0, 9]
    tens = [0, 9]
    list_queen = []
    result_out = []
    count = 0

    if 1 <= number_options <= 92:
        while count < number_options:
            for _ in range(8):
                queen_location = rnd.choice([i for i in range(11, 89, 1) if i % 10 not in units if i // 10 not in tens])
                list_queen.append(queen_location)
                units.append(queen_location % 10)
                tens.append(queen_location // 10)
            if _beating_queen(*list_queen):
                # Проверка, что такой комбинации не было ранее
                for item_result_out in result_out:
                    count_ = 0
                    for i in item_result_out:
                        if i in list_queen:
                            count_ += 1
                    if count_ == 8:
                        break
                else:
                    result_out.append(list_queen.copy())
                    count += 1

            units = [0, 9]
            tens = [0, 9]
            list_queen.clear()
        logger_val.info(_list_to_str(*result_out))
    else:
        logger_val.error(f'Количество возможных вариантов должно лежать в пределах 1-92, а задано {number_options}.')


def _list_to_str(*args):
    """
    Функция преобразования расстановки ферзей из формата list в строковый формат.

    :param args: расстановка ферзей в формате list;
    :return: расстановка ферзей в строковом формате.
    """
    result_str = 'Расстановка 8-и ферзей, чтобы они не били друг друга:\n'

    for num, item_ in enumerate(args, start=1):
        item_str = f'\nРасстановка {num}:\n   1  2  3  4  5  6  7  8\n'
        for i in range(1, 9):
            item_str += f'{i} '
            for j in range(1, 9):
                if i * 10 + j in item_:
                    item_str += 'FF '
                else:
                    item_str += '__ '
            item_str = item_str[:-1] + '\n'
        result_str += item_str
    return result_str


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Функция располагает 8 ферзей на шахматной доске, '
                                                 'которые не бьют друг друга.')
    parser.add_argument('-number_options', metavar='number_options', type=int,
                        help='количество возможных вариантов (1-92)', default=1)
    args = parser.parse_args()

    # Генерим возможные варианты расположения ферзей
    random_queen(args.number_options)

    # Запуск из командной строки
    # python final_task_1.py -number_options 10
    # Описание параметров
    # python final_task_1.py --help
