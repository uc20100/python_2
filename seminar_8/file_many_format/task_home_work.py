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

__all__ = ['info_folder', 'generate_folder_and_file']

# Импорт для функции generate_folder_and_file
from file_func.task_6 import any_file_generator_to_folder
from file_func.task_home_work import rename_file
import shutil
from pathlib import Path
from file_func.task_7 import sort_file
# Импорт для функции info_folder
import os
import json
import csv
import pickle


def info_folder(folder: str, file_json: str, file_csv: str, file_pickle: str):
    """
    Функция собирает статистику о директории.

    :param folder: Папка о которой нужен отчет
    :param file_json: Файл отчета JSON
    :param file_csv: Файл отчета CSV
    :param file_pickle: Файл отчета pickle
    :return:
    """
    list_path = []
    list_info = []
    for dir_path, *_ in os.walk(Path.cwd() / folder):
        list_path.append(dir_path)
    for path_ in list_path:
        size_dir = 0
        for path_file, _, file_mame in os.walk(path_):
            for f_name in file_mame:
                size_dir += os.path.getsize(f'{path_file}\\{f_name}')
        *_, dir_name = path_.split('\\')
        len_dir_name = len(dir_name)+1
        p_folder = str(path_)[:-len_dir_name]
        list_info.append({'parent_folder': p_folder, 'name': dir_name, 'type_obj': 'folder', 'size_obj': size_dir})

    for path_, _, fl_name in os.walk(Path.cwd() / folder):
        for fl in fl_name:
            size_fl = os.path.getsize(f'{path_}\\{fl}')
            list_info.append({'parent_folder': path_, 'name': fl, 'type_obj': 'file', 'size_obj': size_fl})

    with (open(file_json, 'w', encoding='utf-8') as f_json,
          open(file_csv, 'w', newline='', encoding='utf-8') as f_csv,
          open(file_pickle, 'wb') as f_pickle):
        json.dump(list_info, f_json, ensure_ascii=False)
        csv_write = csv.writer(f_csv, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(list(list_info[0].keys()))
        for item in list_info:
            csv_write.writerow(list(item.values()))
        pickle.dump(list_info, f_pickle)


def generate_folder_and_file(directory: str, file_dict: dict, sort_dict: dict, file_name: str = None, n_dig: int = 5,
                             range_original: list = None):
    """
    Функция генерит папки и файлы.

    :param directory: Каталог для размещения файлов и директорий
    :param file_dict: Файловый словарь: ключ - тип файла, значение - количество файлов
    :param sort_dict: Словарь сортировки файлов: ключ - каталог, значение - типы файлов для этого каталога
    :param file_name: Желаемое имя файлов
    :param n_dig: Количество цифр в конце файла
    :param range_original: Диапазон оригинального имени, например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла
    :return:
    """
    # Удаляем папку если она есть
    del_folder, *_ = directory.split('\\')
    p = Path(Path().cwd())
    for obj in p.iterdir():
        if obj == Path(Path().cwd() / del_folder) and obj.is_dir():
            shutil.rmtree(Path().cwd() / del_folder)
            break
    # Создаем папки
    list_f = directory.split('\\')
    str_f = ''
    for f in list_f:
        str_f += f'{f}\\'
        Path(Path().cwd() / str_f).mkdir()
    # Генерим рандомные файлы в заданную папку
    any_file_generator_to_folder(directory, **file_dict)
    # Делаем красивые имена файлам
    for key_dict in file_dict:
        rename_file(folder=directory, type_file_original=key_dict, name=file_name, n_digits=n_dig,
                    range_original=range_original)
    # Раскидываем файлы по разным папкам
    sort_file(directory, **sort_dict)


if __name__ == '__main__':
    dir_gen = 'test_folder\\other\\NoName\\просто_папка'
    file_gen = dict(txt=3, doc=1, pdf=2)
    sort_fl = dict(Видео=['avi', 'mp4'], Изображения=['bmp', 'jpg', 'png'], Документы=['doc', 'exl', 'pdf'])
    # Создаем файлы и каталоги
    generate_folder_and_file(directory=dir_gen, file_dict=file_gen, sort_dict=sort_fl, file_name='file_')
    # Создаём отчёты о файлах и каталогах
    info_folder('test_folder', 't.json', 't.csv', 't.pickle')
    # Проверяем на чтение pickle файл
    with (open('t.pickle', 'rb') as f_read):
        print(pickle.load(f_read))
