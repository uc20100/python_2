# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. Если ФИО не соответствует
# условию, выведите:
#
#
# ФИО должно состоять только из букв и начинаться с заглавной буквы
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре
# недопустимы. Если такого предмета нет, выведите:
#
#
# Предмет {Название предмета} не найден
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# В противном случае выведите:
#
#
# Оценка должна быть целым числом от 2 до 5
#
# Результат теста должен быть целым числом от 0 до 100
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов
# вместе взятых.
#
# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
#
#
# Математика,Физика,История,Литература
# Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен
# иметь следующие методы:
# Атрибуты класса:
#
# name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и
# информацию об оценках и результатах тестов для каждого предмета в виде словаря.
#
# Магические методы (Dunder-методы):
#
# __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их
# результатами. Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.
#
# __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается,
# что name начинается с заглавной буквы и состоит только из букв.
#
# __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.
#
# __str__(self): Возвращает строковое представление студента, включая имя и список предметов.
# Студент: Иван Иванов
# Предметы: Математика, История
#
# Методы класса:
#
# load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения
# данных из файла и добавляет предметы в атрибут subjects.
#
# add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка
# является целым числом от 2 до 5.
#
# add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету.
# Убеждается, что результат теста является целым числом от 0 до 100.
#
# get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
#
# get_average_grade(self): Возвращает средний балл по всем предметам.

import csv


class Value:
    """
        Дескриптор класса Student.

         Dunder методы:
        - __init__(self, min_value: int = None, max_value: int = None): конструктор класса,
        - __set_name__(self, owner, name): вызывается при создании атрибута класса,
        - __set__(self, instance, value): выполняет действие при задании значения атрибуту класса,
        - __get__(self, instance, owner): выполняет действие при обращении к атрибуту класса.
        """

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.min_value is None and self.max_value is None:
            val = value.replace(' ', '')
            if value.istitle() and val.isalpha():
                setattr(instance, self.param_name, value)
            else:
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            if self.min_value <= value <= self.max_value and isinstance(value, int):
                setattr(instance, self.param_name, value)
            else:
                if self.param_name == '_grade':
                    raise ValueError(f'Оценка должна быть целым числом от {self.min_value} до {self.max_value}')
                elif self.param_name == '_test_score':
                    raise ValueError(
                        f'Результат теста должен быть целым числом от {self.min_value} до {self.max_value}')


class Student:
    """
    Класс 'студент'

     Атрибуты:
    - name (str): ФИО студента,
    - subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.

     Методы:
    - load_subjects(self, subjects_file): Загружает предметы из файла CSV,
    - add_grade(self, subject, grade): Добавляет оценку по заданному предмету,
    - add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету,
    - get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета,
    - get_average_grade(self): Возвращает средний балл по всем предметам.

     Dunder методы:
    - __init__(self, name, subjects_file): Конструктор класса,
    - __str__(self): Возвращает строковое представление студента, включая имя и список предметов.
    """
    name = Value()
    grade = Value(2, 5)
    test_score = Value(0, 100)

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = dict(rating={}, test={})
        with open(subjects_file, 'r', encoding='utf-8') as f_read:
            for item in f_read:
                list_subjects = item[:-1].split(',')
            for item in list_subjects:
                self.subjects['rating'][item] = []
                self.subjects['test'][item] = []

    def __str__(self):
        """
        Функция возвращает строковое представление студента, включая имя и список предметов.

        :return:
        """
        ret_str = f'{self.name}\nПредметы:'
        for item in self.subjects['rating']:
            if self.subjects['rating'][item]:
                ret_str += f' {item},'
        return ret_str[:-1]

    def add_grade(self, subject, grade):
        """
        Функция добавляет оценку по заданному предмету.

        :param subject: предмет,
        :param grade: оценка.
        :return:
        """
        self.grade = grade
        if not (subject in self.subjects['rating'].keys()):
            raise ValueError(f'Предмет {subject} не найден')
        list_grade = self.subjects['rating'][subject]
        list_grade.append(self.grade)
        self.subjects['rating'][subject] = list_grade

    def add_test_score(self, subject, test_score):
        """
        Функция добавляет результат теста по заданному предмету.

        :param subject: предмет,
        :param test_score: результат теста.
        :return:
        """
        self.test_score = test_score
        if not (subject in self.subjects['test'].keys()):
            raise ValueError(f'Предмет {subject} не найден')
        list_grade = self.subjects['test'][subject]
        list_grade.append(self.test_score)
        self.subjects['test'][subject] = list_grade

    def get_average_test_score(self, subject):
        """
        Функция возвращает средний балл по тестам для заданного предмета.

        :param subject: предмет,
        :return: средний балл.
        """
        return sum(self.subjects['test'][subject]) / len(self.subjects['test'][subject])

    def get_average_grade(self):
        """
        Функция возвращает средний балл по всем предметам.

        :return: средний балл по всем предметам.
        """
        sum_ = 0
        len_ = 0
        for _, val in self.subjects['rating'].items():
            sum_ += sum(val)
            len_ += len(val)
        return sum_ / len_


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)

# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История
