# Возьмите код из прошлой задачи "Управление информацией о сотрудниках и их возрасте".
#
# Ваша задача - написать набор тестов для класса Employee, чтобы убедиться, что он работает правильно.
#
# Тесты должны быть написаны с использованием модуля unittest и лежать в class TestEmployee(unittest.TestCase).
#
# Тесты:
#
# test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov",
# именем "Ivan", отчеством "Ivanovich" и убедитесь, что метод full_name() возвращает правильное полное имя в
# формате "Ivanov Ivan Ivanovich".
#
# test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с возрастом 30, вызовите метод
# birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.
#
# test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с зарплатой 50000,
# вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.
#
# test_employee_str: Тестирование метода __str__(). Создайте объект Employee с данными: фамилия "Ivanov", имя "Ivan",
# отчество "Ivanovich", возраст 30, должность "manager" и зарплата 50000. Убедитесь, что метод __str__() возвращает
# правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".
#
# test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией "Ivanov" и
# убедитесь, что атрибут last_name не возвращает в верхнем регистре "Ivan".
#
# Тесты должны проходить успешно и не вызывать ошибок.
#
# Запускать тесты не надо, автотест это сделает сам:

# Введите ваше решение ниже

import unittest


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        """
        Выполняется перед запуском теста.
        """
        self.user = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager',
                             50000)

    def test_employee_full_name(self):
        """"
        Тестирование метода full_name().
        """
        self.assertEqual(self.user.full_name(), 'Ivanov Ivan Ivanovich')

    def test_employee_birthday(self):
        """
        Тестирование метода birthday().
        """
        self.user.birthday()
        self.assertEqual(self.user.get_age(), 31)

    def test_employee_raise_salary(self):
        """
        Тестирование метода raise_salary().
        """
        self.user.raise_salary(10)
        self.assertEqual(self.user.salary, 55000.0)

    def test_employee_str(self):
        """
        Тестирование метода __str__().
        """
        self.assertEqual(str(self.user), 'Ivanov Ivan Ivanovich (Manager)')

    def test_employee_last_name_title(self):
        """
        Тестирование атрибута last_name.
        """
        self.assertNotEqual(self.user.last_name, 'Ivan')


if __name__ == '__main__':
    unittest.main()
