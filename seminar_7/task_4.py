# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random as rnd


def file_generator(type_file: str, min_name: int = 6, max_name: int = 30,
                   min_size: int = 256, max_size: int = 4096, n_file: int = 42):
    """
    Функция создает рандомные файлы с рандомными именами и размером.

    :param type_file: расширение файла
    :param min_name: минимальная длина имени файла
    :param max_name: максимальная длина имени файла
    :param min_size: минимальный размер файла
    :param max_size: максимальный размер файла
    :param n_file: количество сгенерированных файлов`
    :return:
    """
    for _ in range(n_file):
        file_name = ''
        for _ in range(rnd.randint(min_name, max_name)):
            file_name += chr(rnd.randint(0x61, 0x7A))
        with open(f'{file_name}.{type_file}', 'w', encoding='utf-8') as f:
            file_size = rnd.randint(min_size, max_size)
            for _ in range(file_size):
                f.write(chr(rnd.randint(0, 0xFF)))
            f.truncate(file_size)


if __name__ == '__main__':
    file_generator('txt', n_file=2)
