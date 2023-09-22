"""
Модуль проверки достоверности даты по Григорианскому календарю
"""
from sys import argv
__all__ = ['check']


# 7. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

def _type_year(check_year: int) -> bool:
    """
    Функция определяет високосный год или нет

    :param check_year: год
    :return: True-високосный, False-нет
    """
    if not check_year % 400:
        return True
    elif not check_year % 100:
        return False
    elif not check_year % 4:
        return True
    else:
        return False


def check(value: str) -> bool:
    """
    Функция проверяет достоверность даты

    :param value: дата в формате DD.MM.YYYY
    :return: True - достоверный, False - нет
    """
    date_list = value.split('.')
    if len(date_list) == 3:
        for item in date_list:
            if not item.isdigit():
                return False
        day, month, year = date_list
        day, month, year = int(day), int(month), int(year)
        if 1 <= year <= 9999:
            if 1 <= month <= 12:
                if day <= 31 and month in (1, 3, 5, 7, 8, 10, 12):
                    return True
                elif day <= 30 and month in (4, 6, 9, 11):
                    return True
                elif day <= 28 and month == 2 or day == 29 and month == 2 and _type_year(year):
                    return True
    return False


if __name__ == '__main__':
    if len(argv) > 1:
        print(f'{check(argv[1]) = }')
    else:
        print(f'{check("") = }')

