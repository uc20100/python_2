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
    """
    Класс 'Пользователь'

     Атрибуты:
    - self.set_user (set): множество с объектами класса Us,

     Методы:
    - load(self, file_json: str = 'users.json'): Загружает в множество объекты класса Us из файла JSON,
    - login_system(self, name, identifier): Проверяет наличие пользователя в множестве и возвращает уровень доступа, либо ошибку AccessException,
    - add_user(self, name, identifier, level): Добавляет пользователя, если такой пользователь есть и новый уровень доступа меньше чем был, то выдает ошибку LevelException,

     Dunder методы:
    - __str__(self): Возвращает строковое представление множества.
    """
    def __init__(self):
        self.set_user = None

    def __str__(self):
        """
        Возвращает строковое представление множества.

        :return:
        """
        ret = ''
        for item in self.set_user:
            ret += f'id: {item.identifier}, name: {item.name}, level: {item.level}\n'
        return ret

    def load(self, file_json: str = 'users.json'):
        """
        Загружает в множество, объекты класса Us из файла JSON.

        :param file_json: файл JSON.
        :return:
        """
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
        """
        Функция проверяет возможность входа в систему.

        :param name: имя пользователя,
        :param identifier: id пользователя,
        :return: уровень доступа или ошибка LevelException
        """
        for item in self.set_user:
            if item.identifier == identifier and item.name == name:
                return item.level
        else:
            raise AccessException(name, identifier)

    def add_user(self, name, identifier, level):
        """
        Функция добавляет пользователя в множество.

        :param name: имя пользователя,
        :param identifier: id пользователя,
        :param level: уровень доступа пользователя,
        :return: если такой пользователь есть и его старый уровень доступа больше нового, то ошибка LevelException, в противном случае добавление.
        """
        if not isinstance(level, int):
            raise ValueError("Параметр 'level' должен быть натуральным числом.")
        if not (1 <= level <= 7):
            raise ValueError("Параметр 'level' должен находиться в пределах от 1 до 7.")
        for item in self.set_user:
            if item.identifier == identifier and item.name == name:
                if int(item.level) > level:
                    raise LevelException(item.level, level)
        u = Us(name, identifier, level)
        set.add(self.set_user, u)


if __name__ == '__main__':
    d = User()
    d.load()
    d.add_user('Evgeny', 'uc', 7)
    print(d.login_system('Evgeny', 'uc'))
    print(d)
