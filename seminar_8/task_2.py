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
    while True:
        name, identifier, level = input('Введите через пробел Имя, идентификатор, уровень доступа (1-7): ').split()

        if level.isdigit():
            if not (1 <= int(level) <= 7):
                print('Уровень доступа должен быть от 1 до 7')
            else:
                json_dict = dict()
                if Path(Path.cwd() / file_json).is_file():
                    with open(file_json, 'r', encoding='utf-8') as fj:
                        json_dict = json.load(fj)
                for key_level in json_dict:
                    if identifier in json_dict[key_level].keys():
                        print('Такой идентификатор уже есть (')
                        break
                else:
                    if f'level_{level}' in json_dict:
                        json_dict_2 = json_dict[f'level_{level}']
                    else:
                        json_dict_2 = {}
                    json_dict_2[identifier] = name
                    json_dict[f'level_{level}'] = json_dict_2
                    with open(file_json, 'w', encoding='utf-8') as f:
                        json.dump(json_dict, f)
                        print('Запись выполнена')
        else:
            print('Это не натуральное число, повторите ввод')


if __name__ == '__main__':
    create_user('my_json')
