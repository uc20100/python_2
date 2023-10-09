"""
Модуль переименования файлов
"""
# Задание
# ✔ Решить задачи, которые не успели решить на семинаре.
# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

__all__ = ['rename_file']
from pathlib import Path


def rename_file(folder: str, type_file_original: str, name: str = None, n_digits: int = 3,
                type_file_new: str = None, range_original: list = None):
    """
    Функция группового переименования файлов.

    :param folder: папка где нужно переименовать файлы
    :param name: желаемое конечное имя файлов
    :param n_digits: количество цифр в порядковом номере
    :param type_file_original: расширение исходного файла
    :param type_file_new: расширение конечного файла
    :param range_original: диапазон оригинального имени, например для диапазона [3, 6] берутся буквы с 3 по 6 из
    исходного имени файла
    :return:
    """

    p = Path(Path.cwd() / folder)
    count = 1
    for obj in p.iterdir():
        if obj.is_file():
            *_, name_file_all = str(obj).split('\\')
            name_file, type_file = name_file_all.split('.')
            new_name_file, new_type_file = name_file, type_file
            if type_file == type_file_original:
                if range_original:
                    new_name_file = name_file[(range_original[0]-1): range_original[1]]
                if name:
                    if range_original:
                        new_name_file += name
                    else:
                        new_name_file = name
                new_name_file += f'{str(count)}'.rjust(n_digits, '0')
                if type_file_new:
                    new_type_file = type_file_new
                obj.rename(p / f'{new_name_file}.{new_type_file}')
                count += 1


if __name__ == '__main__':
    rename_file(folder='new_folder', type_file_original='txt', name='12345678_', n_digits=5, type_file_new='css')

    rename_file(folder='new_folder', type_file_original='css', name='_test_', n_digits=5, range_original=[3, 6])

    rename_file(folder='new_folder', type_file_original='css', range_original=[1, 10], type_file_new='txt')


