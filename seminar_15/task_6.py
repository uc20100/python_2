# Задание №6
# 📌 Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя
# логирование.


from pathlib import Path
import os


from collections import namedtuple
import logging
import argparse

FolderInfo = namedtuple('FolderInfo', ['name_file_or_folder', 'type_file',
                                       'flag_folder', 'parent_folder'])

logging.basicConfig(format='{levelname:<8} {msg}',
                    style='{',
                    filename='info_folder.log',
                    filemode='w',
                    encoding='utf-8',
                    level=logging.INFO)

logger_val = logging.getLogger(__name__)


def info_folder(folder: str):
    """
    Функция собирает статистику о директории.

    :param folder: Папка о которой нужен отчет
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
        len_dir_name = len(dir_name) + 1
        p_folder = str(path_)[:-len_dir_name]
        logger_val.info(f'parent_folder: {p_folder}, name: {dir_name}, folder_flag: {True}')

    for path_, _, fl_name in os.walk(Path.cwd() / folder):
        for fl in fl_name:
            file_mame_, file_type = fl.split('.')
            logger_val.info(f'parent_folder: {path_}, name: {file_mame_}, file_type: {file_type}')


if __name__ == '__main__':
    # Создаём отчёты о файлах и каталогах
    info_folder('C:\\Users\\uc201\\Desktop\\GlonassGpsService')
