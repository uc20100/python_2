"""
Модуль сортировки файлов
"""
# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

__all__ = ['sort_file']

from pathlib import Path
import shutil


def sort_file(sort_folder: str, **kwargs):
    """
    Функция сортирует файлы в зависимости от типа.

    :param sort_folder: сортируемая папка
    :param kwargs: именованные аргументы (ключ - папка, значение - типы файлов)
    :return:
    """

    p = Path(Path.cwd() / sort_folder)
    for folder in kwargs.keys():
        for obj in p.iterdir():
            if obj == p / folder and obj.is_dir():
                break
        else:
            Path(p / folder).mkdir()

    for obj in p.iterdir():
        if obj.is_file():
            for type_folder, list_type_file in kwargs.items():
                *_, file_name_all = str(obj).split('\\')
                name_file, type_ = str(file_name_all).split('.')
                if type_ in list_type_file:
                    obj.replace(p / f'{type_folder}' / f'{name_file}.{type_}')


if __name__ == '__main__':
    folder_dict = dict(Видео=['avi', 'mp4'], Изображения=['bmp', 'jpg', 'png'], Документы=['doc', 'exl', 'pdf'])
    sort_file('new_folder', **folder_dict)
