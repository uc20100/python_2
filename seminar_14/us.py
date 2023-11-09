class Us:
    """
    Класс 'Us'

     Атрибуты:
    - self.name (str): имя пользователя;
    - self.identifier (str): id пользователя;
    - self.level (str | int): уровень доступа пользователя.

     Dunder методы:
    - __init__(self, name, identifier, level): конструктор класса;
    - __eq__(self, other): сравнение двух экземпляров класса;
    - __hash__(self): возвращает собственный hash;
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
    u = Us('Evgeny', 'uc', 7)
    print(u)
