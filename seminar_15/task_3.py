# Задание №3
# 📌 Доработаем задачу 2.
# 📌 Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

# Задание №2
# 📌 На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

"""
Модуль декоратора с записью в JSON файл
"""
# Задание №3
# 📌 Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# 📌 Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой
# функции.

import random
from functools import wraps
from typing import Callable
import logging

__all__ = ['log_file', 'random_number']

logging.basicConfig(format='{levelname:<8} - {asctime}. {msg}',
                    style='{',
                    filename='log_info_2.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger_val = logging.getLogger(__name__)


def log_file(logger: logging.Logger):
    """
    Функция параметров декоратора.

    :param logger: переменная логирования.
    :return:
    """

    def info_func(func: Callable):
        """
        Функция декоратор.

        :param func: Декорируемая функция
        :return:
        """

        @wraps(func)
        def write_log(*args, **kwargs):
            """
            Функция записи log файла.

            :param args: Позиционные аргументы,
            :param kwargs: ключевые аргументы,
            :return: результат работы функции.
            """
            a = str(args).replace('(', '').replace(')', '')
            k = str(kwargs).replace("{'", '').replace("': ", '=').replace("}", '')
            result_value = func(*args, **kwargs)
            mes = f'Функция "{func.__name__}()", Аргументы: ({a}, {k}), Результат: {result_value}'
            logger.info(mes)
            return result_value

        return write_log

    return info_func


@log_file(logger_val)
def random_number(rand_min: int, rand_max: int, /, *, info_str: str) -> str:
    """
    Функция генерации рандомного числа.

    :param rand_min: минимальный предел рандомного числа;
    :param rand_max: максимальный предел рандомного числа;
    :param info_str: строка информации;
    :return: результирующая строка.
    """
    return info_str + ' ' + str(random.randint(rand_min, rand_max))


if __name__ == '__main__':
    print(random_number(1, 10, info_str='Рандомное число:'))

