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
from us_exception import AccessException, LevelException
from us import Us


class User:
    """
    Класс 'Пользователь'

     Атрибуты:
    - self.set_user (set): множество с объектами класса Us;
    - self.your_level: ваш уровень доступа.

     Методы:
    - load(self, file_json: str = 'users.json'): загружает в множество объекты класса Us из файла JSON;
    - login_system(self, name, identifier): проверяет наличие пользователя в множестве и возвращает уровень доступа, либо ошибку AccessException;
    - add_user(self, name, identifier, level): добавляет пользователя, если его уровень больше или равен вашему, в противном случае, выдает ошибку LevelException.

     Dunder методы:
    - __init__(self): конструктор класса;
    - __str__(self): возвращает строковое представление множества.
    """

    def __init__(self):
        self.set_user = set()
        self.your_level = None

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
                self.set_user.add(a)

    def login_system(self, name, identifier):
        """
        Функция проверяет возможность входа в систему.

        :param name: имя пользователя;
        :param identifier: id пользователя;
        :return: уровень доступа или ошибка LevelException.
        """
        variant_a = Us(name, identifier, None)
        for item in self.set_user:
            if item == variant_a:
                self.your_level = int(item.level)
                return self.your_level
        else:
            raise AccessException(name, identifier)

    def add_user(self, name, identifier, level):
        """
        Функция добавляет пользователя в множество, если его уровень не меньше чем ваш.

        :param name: имя пользователя;
        :param identifier: id пользователя;
        :param level: уровень доступа пользователя.
        """
        if not isinstance(level, int):
            raise ValueError("Параметр 'level' должен быть натуральным числом.")
        if not (1 <= level <= 7):
            raise ValueError("Параметр 'level' должен находиться в пределах от 1 до 7.")

        if self.your_level is None or level < self.your_level:
            raise LevelException(self.your_level, level)
        else:
            variant_b = Us(name, identifier, level)
            set.add(self.set_user, variant_b)


if __name__ == '__main__':
    d = User()
    d.load()
    print(d.login_system('Evgeny', 'uc'))
    d.add_user('Evgeny', 'ucr', 7)
    print(d)
