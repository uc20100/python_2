# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет
# следующие атрибуты:
#
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным
# положительным целым числом.
#
# Ваша задача:
#
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
# (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать
# исключения InvalidNameError и InvalidAgeError, если данные неверные.
#
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер
# (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр
# в его ID (по остатку от деления на 7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают
# корректно при передаче неверных данных.

class InvalidAgeError(Exception):
    """
    Класс ошибки возраста.

     Атрибуты:
    - self.value: значение переменной в которой произошла ошибка.

     Dunder методы:
    - __init__(self, value): конструктор класса;
    - __str__(self): возвращает строковое представление ошибки.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid age: {self.value}. Age should be a positive integer.'


class InvalidNameError(Exception):
    """
    Класс ошибки ФИО.

     Атрибуты:
    - self.value: значение переменной в которой произошла ошибка.

     Dunder методы:
    - __init__(self, value): конструктор класса;
    - __str__(self): возвращает строковое представление ошибки.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid name: {self.value}. Name should be a non-empty string.'


class InvalidIdError(Exception):
    """
    Класс ошибки id.

     Атрибуты:
    - self.value: значение переменной в которой произошла ошибка.

     Dunder методы:
    - __init__(self, value): конструктор класса;
    - __str__(self): возвращает строковое представление ошибки.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid id: {self.value}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Value:
    """
    Дескриптор класса Person и Employee.

     Методы:
    - validate(self, value): валидация значений атрибутов класса.

     Dunder методы:
    - __init__(self, value=None): конструктор класса;
    - __set_name__(self, owner, name): вызывается при создании атрибута класса;
    - __set__(self, instance, value): выполняет действие при задании значения атрибуту класса;
    - __get__(self, instance, owner): выполняет действие при обращении к атрибуту класса.
    """

    def __set_name__(self, owner, name):
        """
        Функция выполняет действие при создании атрибута класса.

        :param owner:
        :param name:
        :return:
        """
        self.param_name = '_' + name

    def __set__(self, instance, value):
        """
        Функция выполняет действие при задании значения атрибуту класса.

        :param instance:
        :param value:
        :return:
        """
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        """
        Функция выполняет действие при чтении атрибуту класса.

        :param instance:
        :param owner:
        :return:
        """
        return getattr(instance, self.param_name)

    def validate(self, value):
        """
        Функция валидирует значения атрибута.

        :param value: значение атрибута.
        :return:
        """
        if self.param_name[1:] in ('first_name', 'second_name', 'surname'):
            if not isinstance(value, str) or value == '':
                raise InvalidNameError(value)
        elif self.param_name[1:] == 'age':
            if not isinstance(value, int) or value < 0:
                raise InvalidAgeError(value)
        elif self.param_name[1:] == 'user_id':
            if not isinstance(value, int) or len(str(value)) < 6 or value < 0:
                raise InvalidIdError(value)
        else:
            raise ValueError('Неизвестный параметр')


class Person:
    """
    Класс персона.

     Атрибуты:
    - self.first_name: имя;
    - self.second_name: фамилия;
    - self.surname: отчество;
    - self.age: возраст.

     Методы:
    - birthday(self): добавляет к возрасту один год;
    - get_age(self): возвращает возраст.

     Dunder методы:
    - __init__(self, first_name, second_name, surname, age): конструктор класса;
    - __str__(self): возвращает строковое представление класса (для пользователя).
    """
    first_name = Value()
    second_name = Value()
    surname = Value()
    age = Value()

    def __init__(self, first_name, surname, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.surname = surname
        self.age = age

    def __str__(self):
        """
        Функция возвращает строковое представление класса (для пользователя).

        :return:
        """
        return f'{self.first_name} {self.second_name} {self.surname}, {self.age} лет'

    def birthday(self):
        """
        Функция добавляет к возрасту один год.

        :return:
        """
        self.age += 1

    def get_age(self):
        """
        Функция возвращает возраст.

        :return:
        """
        return self.age


class Employee(Person):
    """
    Класс Сотрудник.

     Атрибуты:
    - self.user_id: id сотрудника.

     Методы:
    - get_level(self): возвращает уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

     Dunder методы:
    - __init__(self, first_name, surname, second_name, age, user_id): конструктор класса;
    - __str__(self): возвращает строковое представление класса (для пользователя).
    """
    user_id = Value()

    def __init__(self, first_name, surname, second_name, age, user_id):
        super().__init__(first_name, surname, second_name, age)
        self.user_id = user_id

    def __str__(self):
        """
        Функция возвращает строковое представление сотрудника.

        :return:
        """
        return f'{self.first_name} {self.second_name} {self.surname}, {self.age} лет, id: {self.user_id}'

    def get_level(self):
        """
        Функция вычисляет уровень сотрудника.

        :return: уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
        """
        level_str = str(self.user_id % 7)
        level = 0
        for item in level_str:
            level += int(item)
        return level


if __name__ == '__main__':
    person = Person("", "John", "Doe", 30)
    print(person)
    # Ожидаемый ответ:
    # Invalid name: . Name should be a non-empty string.

    # person = Person("Alice", "Smith", "Johnson", -5)
    # Ожидаемый ответ:
    # __main__.InvalidAgeError: Invalid age: -5. Age should be a positive integer.

    # employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
    # Ожидаемый ответ:
    # __main__.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.

    # person = Person("Alice", "Smith", "Johnson", 25)
    # print(person.get_age())
    # Ожидаемый ответ:
    # 25
