"""
Модуль добавления пользователей в JSON файл
"""
# Задание №2
# 📌 Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в
# JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные
# должны сохраняться.

__all__ = ['create_user']
from pathlib import Path
import json


def create_user(file_json):
    """
    Функция создает пользователей и сохраняет их в JSON файл

    :param file_json: JSON файл
    :return:
    """
    wr_status = False
    while True:
        name, identifier, level = input('Введите через пробел Имя, идентификатор, уровень доступа (1-7): ').split()

        if level.isdigit():
            if not (1 <= int(level) <= 7):
                print('Уровень доступа должен быть от 1 до 7')
            else:
                json_dict = dict()
                json_dict_2 = dict()
                if Path(Path.cwd() / file_json).is_file():
                    with open(file_json, 'r', encoding='utf-8') as fj:
                        json_dict = json.load(fj)
                if f'level_{level}' in json_dict.keys():
                    if identifier in json_dict[f'level_{level}'].keys():
                        print('Такой идентификатор уже есть (')
                    else:
                        json_dict_2 = json_dict[f'level_{level}']
                        wr_status = True
                else:
                    wr_status = True
                if wr_status:
                    wr_status = False
                    with open(file_json, 'w', encoding='utf-8') as f:
                        json_dict_2[identifier] = name
                        json_dict[f'level_{level}'] = json_dict_2
                        json.dump(json_dict, f)
                        print('Запись выполнена')


if __name__ == '__main__':
    create_user('my_json')
