"""
Шахматный модуль
"""

__all__ = ['beating_queen', 'random_queen']

import random as rnd


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


def beating_queen(queen_1: int, queen_2: int, queen_3: int, queen_4: int,
                  queen_5: int, queen_6: int, queen_7: int, queen_8: int) -> bool:
    """
    Функция определяет есть ли бьющая пара ферзей.

    :param queen_1: локация ферзя 1
    :param queen_2: локация ферзя 2
    :param queen_3: локация ферзя 3
    :param queen_4: локация ферзя 4
    :param queen_5: локация ферзя 5
    :param queen_6: локация ферзя 6
    :param queen_7: локация ферзя 7
    :param queen_8: локация ферзя 8
    :return: True если такая пара есть, False если нет
    """
    queen_placement = {queen_1, queen_2, queen_3, queen_4, queen_5, queen_6, queen_7, queen_8}

    for item_ in queen_placement:
        item_set = {item_}
        if not ((_location_queen(item_) & queen_placement - item_set) == set()):
            return False
    return True


# ДЗ, задание №3. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различный случайные  варианты и выведите 4 успешных расстановки
def random_queen() -> list:
    """
    Функция случайной расстановки 8 ферзей, чтобы они не били друг друга.

    :return: 4 варианта расстановки
    """
    units = [0, 9]
    tens = [0, 9]
    list_queen = []
    result_out = []
    count = 0

    while True:
        for _ in range(8):
            queen_location = rnd.choice([i for i in range(11, 89, 1) if i % 10 not in units if i // 10 not in tens])
            list_queen.append(queen_location)
            units.append(queen_location % 10)
            tens.append(queen_location // 10)
        if beating_queen(*list_queen):
            if count < 4:
                result_out.append(list_queen.copy())
                count += 1
            else:
                break
        units = [0, 9]
        tens = [0, 9]
        list_queen.clear()
    return result_out


if __name__ == '__main__':
    # Хорошая и плохая расстановка ферзей
    good = (31, 52, 23, 84, 15, 76, 47, 68)
    bad = (31, 52, 23, 84, 15, 76, 47, 67)
    print(f'{beating_queen(*good) = }')
    print(f'{beating_queen(*bad) = }')
    print()

    # Генерация хороших расстановок ферзей
    print('Хорошие расстановки ферзей:')
    good_queen = random_queen()
    for n, item in enumerate(good_queen, 1):
        print(f'{n} - {item}')
