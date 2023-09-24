# ДЗ, задание №2. Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
from typing import Set

__all__ = ['beating_queen']


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
    :param queen_4: локация ферзя 4f'{_location_queen(item) & queen_placement = }'
    :param queen_5: локация ферзя 5
    :param queen_6: локация ферзя 6
    :param queen_7: локация ферзя 7
    :param queen_8: локация ферзя 8
    :return: True если такая пара есть, False если нет
    """
    queen_placement = {queen_1, queen_2, queen_3, queen_4, queen_5, queen_6, queen_7, queen_8}

    for item in queen_placement:
        item_set = {item}
        if not ((_location_queen(item) & queen_placement - item_set) == set()):
            return False
    return True


if __name__ == '__main__':
    # Хорошая расстановка ферзей
    good = (31, 52, 23, 84, 15, 76, 47, 68)
    bad = (31, 52, 23, 84, 15, 76, 47, 67)
    print(f'{beating_queen(*good) = }')
    print(f'{beating_queen(*bad) = }')
