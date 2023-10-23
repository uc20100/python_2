# Задание №4
# 📌 Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    """
    Хранит списки чисел и строк, при создании нового экземпляра класса, старые данные сохраняются.
    """
    str_list = []
    number_list = []

    def __init__(self, num_, str_):
        self.str_list.append(str_)
        self.number_list.append(num_)

    def __str__(self):
        return f'Числа: {self.number_list}, строки: {self.str_list}'

    def __repr__(self):
        return f'Archive({self.number_list} {self.str_list})'


if __name__ == '__main__':
    t = Archive(5, 'five')
    print(t.number_list, t.str_list)
    z = Archive(6, 'six')
    print(z.number_list, z.str_list)
    print(t)
    print(f'{t = }')