# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from decimal import Decimal
from fractions import Fraction


def read_value(number_val: int) -> list:
    """
    Функция возвращает введенные переменные в формате list
    :param number_val: номер вводимых переменных
    :return: переменные в формате list
    """
    while True:
        str_val = input(f'Введите строку {number_val} в формате a/b: ')
        list_val = str_val.split('/')
        if len(list_val) == 2 and list_val[0].isdigit() and list_val[1].isdigit():
            list_val.append(str_val)
            return list_val
        else:
            print('Не верный формат. Введите числа в формате a/b')


val_1 = read_value(1)
val_2 = read_value(2)

print(f'Сумма дробей:                 {Decimal(val_1[0]) / Decimal(val_1[1]) + Decimal(val_2[0]) / Decimal(val_2[1])}')
print(f'Проверка суммы дробей:        {Fraction(val_1[2]) + Fraction(val_2[2])}')
print()
print(f'Произведение дробей:          {Decimal(val_1[0]) / Decimal(val_1[1]) * Decimal(val_2[0]) / Decimal(val_2[1])}')
print(f'Проверка произведения дробей: {Fraction(val_1[2]) * Fraction(val_2[2])}')



