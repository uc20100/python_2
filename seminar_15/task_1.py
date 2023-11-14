# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(format='{levelname:<8} - {asctime}. В модуле "{name}" '
                           'в строке {lineno:03d} функция "{funcName}()" '
                           'в {created} секунд, произошла ошибка: {msg}',
                    style='{',
                    filename='log_err.log',
                    filemode='w',
                    encoding='utf-8',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)


def division_two_numbers(number_1, number_2):
    """
    Функция деления двух чисел.

    :param number_1: число 1;
    :param number_2: число 2;
    :return: результат деления или None в случае деления на ноль.
    """
    rez = None
    try:
        rez = number_1 / number_2
    except ZeroDivisionError as e:
        logger.error(e)
    return rez


if __name__ == '__main__':
    print(division_two_numbers(1, 0))
