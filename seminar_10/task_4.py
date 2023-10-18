# Задание №4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
import random

from task_3 import User


class Employee(User):
    def __init__(self, *args, **kwargs):
        self.id = str(random.randint(1, 999999)).rjust(6, '0')
        self.level = 0
        for char in self.id:
            self.level += int(char)
        self.level %= 7
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    u2 = Employee('Evgeny', 'Egipti', 20)
    print(f'{u2.full_name()}')
    print(f'{u2.id = }')
    print(f'{u2.level = }')
    print(f'{u2.current_age = }')
