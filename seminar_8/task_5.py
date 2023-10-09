"""
Модуль конвертации JSON файлов в pickle файлы
"""
# Задание №5
# 📌 Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

__all__ = ['json_to_pickle']

import json
from pathlib import Path
if __name__ == '__main__':
    import shutil
import pickle


def json_to_pickle(folder: str):
    """
    Функция сохраняет JSON файлы в одноименные pickle файлы

    :param folder: папка в которой будем делать преобразование
    :return:
    """
    p = Path(Path.cwd() / folder)
    for obj in p.iterdir():
        if obj.is_file():
            *_, name_file_all = str(obj).split('\\')
            name_file, type_file = name_file_all.split('.')
            if type_file == 'json':
                with (open(p / name_file_all, 'r', encoding='utf-8') as f_read,
                      open(p / f'{name_file}.pickle', 'wb') as f_write):
                    read_json = json.load(f_read)
                    pickle.dump(read_json, f_write)


if __name__ == '__main__':
    # Удаляем папку если она есть и снова её создаём
    folder_ = 'test_folder'
    p = Path(Path().cwd())
    for obj in p.iterdir():
        if obj == Path().cwd() / folder_ and obj.is_dir():
            shutil.rmtree(folder_)
            break
    Path(folder_).mkdir()
    # Копируем файлы JSON из текущей директории в новую
    for obj in p.iterdir():
        if obj.is_file():
            *_, name_file_all = str(obj).split('\\')
            *_, type_file = name_file_all.split('.')
            if type_file == 'json':
                shutil.copy(name_file_all, folder_)
    # преобразовываем json в pickle
    json_to_pickle(folder_)
