# Задание №1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

import time


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance


if __name__ == '__main__':
    one_str = MyStr('Hello world!', 'Evgeny Egipti')
    print(f'{one_str.upper() = }, {one_str.author.lower() = }, {one_str.time = }')
