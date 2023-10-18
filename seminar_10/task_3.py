# Задание №3
# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class User:
    current_age = None

    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.__age = age
        self.current_age = age

    def birthday(self):
        self.__age += 1
        self.current_age = self.__age

    def full_name(self):
        return self.first_name + ' ' + self.second_name


if __name__ == '__main__':
    u1 = User('Udjin', 'Egipti', 20)
    print(f'{u1.current_age = }')
    u1.birthday()
    u1.birthday()
    u1.birthday()
    print(f'{u1.full_name() = }')
    print(f'{u1.current_age = }')
    u1.current_age = 10
    print(f'{u1.current_age = }')
    u1.birthday()
    print(f'{u1.current_age = }')
