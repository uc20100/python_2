"""
Модуль сбора статистики о каталогах
"""
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
#     ○ Для дочерних объектов указывайте родительскую директорию.
#     ○ Для каждого объекта укажите файл это или директория.
#     ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

__all__ = ['info_folder']
if __name__ == '__main__':
    from file_func.task_6 import any_file_generator_to_folder
    from file_func.task_home_work import rename_file
    import shutil
    from pathlib import Path
    from file_func.task_7 import sort_file
import os
import json
import csv
import pickle


def info_folder(folder: str, file_json: str, file_csv: str, file_pickle: str):
    """
    Функция собирает статистику о директории

    :param folder: папка о которой нужен отчет
    :param file_json: файл отчета JSON
    :param file_csv: файл отчета CSV
    :param file_pickle: файл отчета pickle
    :return:
    """

    list_info = []
    for dir_path, dir_name, file_name in os.walk(Path.cwd() / folder):
        for dir_ in dir_name:
            size_dir = os.path.getsize(f'{dir_path}\\{dir_}')
            list_info.append({'parent_folder': dir_path, 'type_obj': 'folder', 'size_obj': size_dir})
        for file_ in file_name:
            size_file = os.path.getsize(f'{dir_path}\\{file_}')
            list_info.append({'parent_folder': dir_path, 'type_obj': 'file', 'size_obj': size_file})
        with (open(file_json, 'w', encoding='utf-8') as f_json,
              open(file_csv, 'w', newline='', encoding='utf-8') as f_csv,
              open(file_pickle, 'wb') as f_pickle):
            json.dump(list_info, f_json, ensure_ascii=False)
            csv_write = csv.writer(f_csv, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_write.writerow(list(list_info[0].keys()))
            for item in list_info:
                csv_write.writerow(list(item.values()))
            pickle.dump(list_info, f_pickle)


if __name__ == '__main__':
    folder_ = 'test_folder\\other\\NoName\\папка'

    # Удаляем папку если она есть
    del_folder, *_ = folder_.split('\\')
    p = Path(Path().cwd())
    for obj in p.iterdir():
        if obj == Path(Path().cwd() / del_folder) and obj.is_dir():
            shutil.rmtree(Path().cwd() / del_folder)
            break
    # Создаем папки
    list_f = folder_.split('\\')
    str_f = ''
    for f in list_f:
        str_f += f'{f}\\'
        Path(Path().cwd() / str_f).mkdir()
    # Генерим рандомные файлы в заданную папку
    file_dict = dict(txt=3, doc=1, pdf=2)
    any_file_generator_to_folder(folder_, **file_dict)
    # Делаем красивые имена файлам
    for key_dict in file_dict:
        rename_file(folder=folder_, type_file_original=key_dict, name='file_', n_digits=5)
    # Раскидываем файлы по разным папкам
    folder_dict = dict(Видео=['avi', 'mp4'], Изображения=['bmp', 'jpg', 'png'], Документы=['doc', 'exl', 'pdf'])
    sort_file(folder_, **folder_dict)

    info_folder('test_folder', 't.json', 't.csv', 't.pickle')
    with (open('t.pickle', 'rb') as f_read):
        print(pickle.load(f_read))