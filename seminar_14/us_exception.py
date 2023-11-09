class UsException(BaseException):
    pass


class LevelException(UsException):
    """
        Класс ошибки уровня пользователя.

         Атрибуты:
        - self.your_level (int | str): ваш уровень доступа;
        - self.user_level (int | str): уровень доступа пользователя.

         Dunder методы:
        - __str__(self): Возвращает строковое представление ошибки.
        """

    def __init__(self, your_level, user_level):
        self.your_level = your_level
        self.user_level = user_level

    def __str__(self):
        if self.your_level is not None:
            return (f"Уровень доступа пользователя '{self.user_level}' меньше вашего уровня '{self.your_level}', "
                    f"а должен быть больше или равен")
        else:
            return 'Вы не залогинились.'


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
