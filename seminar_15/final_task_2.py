"""
Задача из семинара 8.

Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода:
    Для дочерних объектов указывайте родительскую директорию.
    Для каждого объекта укажите файл это или директория.
    Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с
    учётом всех вложенных файлов и директорий.
"""

__all__ = ['info_folder']

import os
from collections import namedtuple
import logging
import argparse

logging.basicConfig(format='{levelname:<8} - {asctime}. {msg}',
                    style='{',
                    filename='info_folder.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

logger_val = logging.getLogger(__name__)


def info_folder(folder: str):
    """
    Функция собирает статистику о директории.

    :param folder: Папка о которой нужен отчет
    :return:
    """

    FolderInfo = namedtuple('FolderInfo', ['name_file_or_folder', 'parent_folder',
                                           'size', 'type_file', 'flag_folder'], defaults=['', '', 0, 'no_type', True])
    list_namedtuple = []
    list_path = []
    dir_path = None
    for dir_path, *_ in os.walk(folder):
        list_path.append(dir_path)
    if dir_path is not None:
        for path_ in list_path:
            size_dir = 0
            for path_file, _, file_mame in os.walk(path_):
                for f_name in file_mame:
                    size_dir += os.path.getsize(f'{path_file}\\{f_name}')
            *_, dir_name = path_.split('\\')
            len_dir_name = len(dir_name) + 1
            p_folder = str(path_)[:-len_dir_name]
            list_namedtuple.append(FolderInfo(dir_name, p_folder, size_dir))

        for path_, _, fl_name in os.walk(folder):
            for fl in fl_name:
                size_fl = os.path.getsize(f'{path_}\\{fl}')
                try:
                    file_mame_, file_type = fl.split('.')
                except ValueError:
                    file_mame_ = fl
                    file_type = 'no_type'
                list_namedtuple.append(FolderInfo(file_mame_, path_, size_fl, file_type, False))

        max_len_name_file_or_folder = 0
        max_len_parent_folder = 0
        max_len_type_file = 0
        max_len_flag_folder = 0
        max_len_size = 0
        for item in list_namedtuple:
            if max_len_name_file_or_folder < len(item.name_file_or_folder):
                max_len_name_file_or_folder = len(item.name_file_or_folder)
            if max_len_parent_folder < len(item.parent_folder):
                max_len_parent_folder = len(item.parent_folder)
            if max_len_type_file < len(item.type_file):
                max_len_type_file = len(item.type_file)
            if max_len_flag_folder < len(str(item.flag_folder)):
                max_len_flag_folder = len(str(item.flag_folder))
            if max_len_size < len(str(item.size)):
                max_len_size = len(str(item.size))
        mes_str = f"Результаты обхода директории '{folder}':\n"
        for item in list_namedtuple:
            mes_str += (f'parent_folder: {item.parent_folder:<{max_len_parent_folder + 1}}, '
                        f'name: {item.name_file_or_folder:<{max_len_name_file_or_folder + 1}}, '
                        f'folder_flag: {str(item.flag_folder):<{max_len_flag_folder + 1}}, '
                        f'type_file: {item.type_file:<{max_len_type_file + 1}}, '
                        f'size: {item.size:<{max_len_size + max_len_size // 3 + 1}_} байт\n')
        logger_val.info(mes_str)
    else:
        logger_val.error(f"Не верно задан путь к директории - '{folder}'")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Функция сохраняет информацию о директории')
    parser.add_argument('-scan_folder', metavar='scan_folder', type=str,
                        help='путь к папке о которой нужен отчет', default='')
    args = parser.parse_args()

    # Создаём отчёты о файлах и каталогах
    info_folder(args.scan_folder)

    # Запуск из командной строки
    # python final_task_2.py -scan_folder C:\Users\uc201\Desktop\GlonassGpsService
    # Описание параметров
    # python final_task_2.py --help
