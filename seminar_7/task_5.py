# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from task_4 import file_generator


def any_file_generator(**kwargs):
    """

    :param kwargs: именованные аргументы
    :return:
    """
    for type_f, n_f in kwargs.items():
        file_generator(type_file=type_f, n_file=n_f)


if __name__ == '__main__':
    file_dict = dict(txt=3, doc=1, pdf=2)
    any_file_generator(**file_dict)
