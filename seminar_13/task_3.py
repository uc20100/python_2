# Задание №3
# 📌 Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class UsException(BaseException):
    pass


class LevelException(UsException):
    """
        Класс ошибки доступа пользователя.

         Атрибуты:
        - self.old_level (int | str): старый уровень доступа пользователя,
        - self.new_level (int | str): новый уровень доступа пользователя.

         Dunder методы:
        - __str__(self): Возвращает строковое представление ошибки.
        """
    def __init__(self, old_level, new_level):
        self.old_level = old_level
        self.new_level = new_level

    def __str__(self):
        return f"Ваш уровень '{self.new_level}' меньше уровня '{self.old_level}', а должен быть больше или равен"


class AccessException(UsException):
    """
    Класс ошибки доступа пользователя.

     Атрибуты:
    - self.name (str): имя пользователя,
    - self.identifier (str): id пользователя.

     Dunder методы:
    - __str__(self): Возвращает строковое представление ошибки.
    """

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def __str__(self):
        return f"Пользователя с именем '{self.name}' и идентификатором '{self.identifier}' нет в множестве"
