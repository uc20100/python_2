# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# 📌 list-архивы также являются свойствами экземпляра

class Archive:
    str_list = []
    number_list = []

    def __init__(self, num_, str_):
        self.str_list.append(num_)
        self.number_list.append(str_)


if __name__ == '__main__':
    t = Archive(5, 'five')
    print(t.number_list, t.str_list)
    z = Archive(6, 'six')
    print(z.number_list, z.str_list)
