"""
Модуль генерации псевдоимен
"""
# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

__all__ = ['pseudonyms']
import random as rnd


def pseudonyms(name: str, lines):
    """
    Функция генерит псевдоимена.

    :param name: имя файла
    :param lines: количество строк
    :return:
    """
    vowels = ('а', 'е', 'и', 'о', 'э', 'ю', 'я')
    count = 0

    with open(f'{name}', 'w', encoding='utf-8') as f:
        while count < lines:
            result_str = ''
            for _ in range(rnd.randint(5, 8)):
                result_str += chr(rnd.randint(0x430, 0x44f))
            for item in vowels:
                if item in result_str:
                    result_str = result_str[0].upper() + result_str[1::]
                    print(result_str, file=f)
                    count += 1
                    break


if __name__ == '__main__':
    pseudonyms('pseudonyms.txt', 5)
