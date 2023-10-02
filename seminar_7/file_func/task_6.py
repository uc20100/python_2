"""
Модуль генерации файлов (в директорию)
"""
# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

__all__ = ['any_file_generator_to_folder']
from pathlib import Path
import random as rnd


def _file_generator_to_folder(us_folder: str, type_file: str, min_name: int = 6, max_name: int = 30,
                              min_size: int = 256, max_size: int = 4096, n_file: int = 42):
    """
    Функция создает рандомные файлы с рандомными именами и размером в заданной директории.

    :param us_folder: директория для файлов
    :param type_file: расширение файла
    :param min_name: минимальная длина имени файла
    :param max_name: максимальная длина имени файла
    :param min_size: минимальный размер файла
    :param max_size: максимальный размер файла
    :param n_file: количество сгенерированных файлов`
    :return:
    """
    count = 0
    p = Path(Path().cwd())

    for obj in p.iterdir():
        if obj == Path().cwd() / us_folder and obj.is_dir():
            break
    else:
        Path(us_folder).mkdir()
    p = Path(Path().cwd() / us_folder)

    while count < n_file:
        file_name = ''
        for _ in range(rnd.randint(min_name, max_name)):
            file_name += chr(rnd.randint(0x61, 0x7A))

        for obj_ in p.iterdir():
            if obj_ == Path().cwd() / us_folder / f'{file_name}.{type_file}' and obj_.is_file():
                break
        else:
            with open(f'{p}' + f'\\{file_name}.{type_file}', 'w', encoding='utf-8') as f:
                file_size = rnd.randint(min_size, max_size)
                for _ in range(file_size):
                    f.write(chr(rnd.randint(0, 0xFF)))
                f.truncate(file_size)
            count += 1


def any_file_generator_to_folder(folder: str, **kwargs):
    """
    Функция генерит файлы с заданным расширением и количеством в заданную папку.

    :param folder: папка для файлов
    :param kwargs: именованные аргументы (ключ - тип файла, значение - количество файлов)
    :return:
    """
    for type_f, n_f in kwargs.items():
        _file_generator_to_folder(us_folder=folder, type_file=type_f, n_file=n_f)


if __name__ == '__main__':
    file_dict = dict(txt=3, doc=1, pdf=2)
    any_file_generator_to_folder('new_folder', **file_dict)
