# Задание №5
# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

import json
from task_4 import Us
from task_3 import AccessException
from task_3 import LevelException


class User:
    def __init__(self, my_level):
        self.set_user = None
        self.my_level = my_level

    def load(self, file_json: str = 'users.json'):
        list_users = []
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
                list_users.append(a)
        self.set_user = set(list_users)

    def login_system(self, name, identifier):
        for item in self.set_user:
            if item.identifier == identifier and item.name == name:
                return item.level
        else:
            raise AccessException(name, identifier)

    def add_user(self, name, identifier, level):
        for item in self.set_user:
            if item.identifier == identifier and item.name == name:
                if int(item.level) > level:
                    raise LevelException(item.level, level)
        u = Us(name, identifier, level)
        set.add(self.set_user, u)


if __name__ == '__main__':
    d = User(1)
    d.load()
    d.add_user('Evgeny', 'uc', 7)
    print(d.login_system('Evgeny', 'ucc'))
