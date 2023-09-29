# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random as rnd


def random_number(name: str, lines: int):
    """
    Функция заполняет файл случайными числами


    :param name: имя файла
    :param lines: количество строк
    :return:
    """
    with open(f'{name}.txt', 'a', encoding='utf-8') as f:
        for _ in range(lines):
            print(f'{rnd.randint(-1_000, 1000)} | {round(rnd.uniform(-1_000, 1_000), 2)}', file=f)


# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

def pseudonyms(name: str, lines):
    """
    Функция генерит псевдоимена.

    :return:
    """
    vowels = ('а', 'е', 'и', 'о', 'э', 'ю', 'я')
    count = 0

    with open(f'{name}.txt', 'w', encoding='utf-8') as f:
        while count < lines:
            result_str = ''
            for _ in range(8):
                result_str += chr(rnd.randint(0x430, 0x44f))
            for item in vowels:
                if item in result_str:
                    result_str = result_str[0].upper() + result_str[1::]
                    print(result_str, file=f)
                    count += 1
                    break


if __name__ == '__main__':
    # random_number('example', 10)
    pseudonyms('example', 10)
