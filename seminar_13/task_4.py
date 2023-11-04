# Задание №4
# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

from pathlib import Path
import json


def create_user_json(file_json: str = 'users.json'):
    """
    Функция создает пользователей и сохраняет их в JSON файл

    :param file_json: JSON файл
    :return:
    """
    while True:
        list_value = list(input('Введите через пробел Имя, идентификатор, уровень доступа (1-7) '
                                'или "q" для выхода из цикла: ').split())
        if len(list_value) == 1 and str(list_value[0]).lower() == 'q':
            print('Выход из цикла')
            break
        if len(list_value) == 3:
            name, identifier, level = list_value
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
                        if f'{level}' in json_dict:
                            json_dict_2 = json_dict[f'{level}']
                        else:
                            json_dict_2 = {}
                        json_dict_2[identifier] = name
                        json_dict[f'{level}'] = json_dict_2
                        with open(file_json, 'w', encoding='utf-8') as f:
                            json.dump(json_dict, f, ensure_ascii=False)
                            print('Запись выполнена')
            else:
                print('Это не натуральное число, повторите ввод')
        else:
            print('Вы ввели не три параметра или "q" для выхода из цикла, повторите ввод')


def create_users(file_json: str = 'users.json'):
    """
    Функция добавляет в множества объекты класса Us, читая инфу из JSON файла.

    :param file_json: JSON файл,
    :return: возвращает множество.
    """
    set_users = set()
    try:
        with open(file_json, 'r', encoding='utf-8') as fj:
            try:
                json_dict = json.load(fj)
            except json.decoder.JSONDecodeError as e:
                raise e
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файла '{file_json}' не найдено. {e}")
    for lev, item_ in json_dict.items():
        for ident, name in item_.items():
            a = Us(name, ident, lev)
            set_users.add(a)
    return set_users


class Us:
    """
    Класс 'Us'

     Атрибуты:
    - self.name (str): имя пользователя,
    - self.identifier (str): id пользователя,
    - self.level (str | int): уровень доступа пользователя.

     Dunder методы:
    - __init__(self, name, identifier, level): конструктор класса,
    - __eq__(self, other): сравнение двух экземпляров класса,
    - __hash__(self): возвращает собственный hash,
    - __str__(self): возвращает строковое представление класса.
    """
    def __init__(self, name, identifier, level):
        self.name = name
        self.identifier = identifier
        self.level = level

    def __eq__(self, other):
        return self.identifier == other.identifier and self.name == other.name

    def __str__(self):
        return f'Идентификатор: {self.identifier}, Имя: {self.name}, Уровень: {self.level}'

    def __hash__(self):
        return hash((self.name, self.identifier, self.level))


if __name__ == '__main__':
    create_user_json('users.json')
    for item in create_users():
        print(item)
