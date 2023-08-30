# Задание №6 Которые не доделали на семинаре
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
from typing import Tuple

R_SIZE = 2
BILL = 50
BIG_MONEY = 5_000_000

CASH_INDEX = 0
COUNT_INDEX = 1
BALANCE_INDEX = 2
MULTIPLICITY = 3

data_atm = [0, 0, 0, BILL]


def add_3_percent(args: list) -> str:
    """
    Функция при каждой 3-й операции индексирует вклад на 3%
    :param args: взнос/выдача, счетчик, баланс, кратность взноса/выдачи
    :return: информация об операции
    """
    if args[COUNT_INDEX] >= 2:
        args[COUNT_INDEX] = 0
        args[BALANCE_INDEX] = args[BALANCE_INDEX] * 1.03
        return f'Счетчик {args[COUNT_INDEX]}. Вам начислено 3%, баланс {round(args[BALANCE_INDEX], R_SIZE)} '
    else:
        args[COUNT_INDEX] += 1
        return f'Счетчик {args[COUNT_INDEX]}'


def replenishment(args: list) -> str:
    """
    Функция пополняет баланс
    :param args: взнос, счетчик, баланс, кратность взноса/выдачи
    :return: информация об операции
    """
    if not args[CASH_INDEX] % args[MULTIPLICITY]:
        print(add_3_percent(data_atm))
        args[BALANCE_INDEX] = args[BALANCE_INDEX] + args[CASH_INDEX]
        return f'Вы положили {round(args[CASH_INDEX], R_SIZE)}₽, баланс {round(args[BALANCE_INDEX], R_SIZE)}₽'
    else:
        return f'Ошибка операции, укажите сумму кратную {round(args[MULTIPLICITY], R_SIZE)}, баланс {round(args[BALANCE_INDEX], R_SIZE)}₽'


def cash_withdrawal(args: list) -> str:
    """
    Функция выдачи наличных
    :param args: сумма выдачи, счетчик, баланс, кратность взноса/выдачи
    :return: информация об операции
    """
    if not args[CASH_INDEX] % args[MULTIPLICITY]:
        if args[BALANCE_INDEX] >= args[CASH_INDEX] * 1.015:
            percent = args[CASH_INDEX] * 0.015
            print(add_3_percent(data_atm))
            if 30 < percent < 600:
                args[BALANCE_INDEX] -= args[CASH_INDEX] * 1.015
                return f'Вы сняли {round(args[CASH_INDEX], R_SIZE)}₽, баланс {round(args[BALANCE_INDEX], R_SIZE)}₽, 1.5% комиссия({round(percent, R_SIZE)}₽)'
            else:
                args[BALANCE_INDEX] -= args[CASH_INDEX]
                return f'Вы сняли {round(args[CASH_INDEX], R_SIZE)}₽, баланс {round(args[BALANCE_INDEX], R_SIZE)}₽, без комиссии'
        else:
            return f'За снятие взимается плата 1.5%, у вас не хватает средств. Баланс {round(args[BALANCE_INDEX], R_SIZE)}₽'
    else:
        return f'Ошибка операции, укажите сумму кратную {round(args[MULTIPLICITY], R_SIZE)}, баланс {round(args[BALANCE_INDEX], R_SIZE)}₽'


def get_tax(args: list) -> str | None:
    """
    Функция взимает налог на роскошь
    :param args: выдача/взнос, счетчик, баланс, кратность взноса/выдачи
    :return: информация об операции
    """
    if args[BALANCE_INDEX] > BIG_MONEY:
        tax_val = args[BALANCE_INDEX] * 0.1
        args[BALANCE_INDEX] -= tax_val
        return f'Взяли налог на роскошь 10% ({round(tax_val, R_SIZE)}₽), баланс {round(args[BALANCE_INDEX], R_SIZE)}₽'
    else:
        return None







info_str: str = '\n   МЕНЮ \n' \
                + '1. Пополнить сумма (например: 1 500)\n' \
                + '2. Снять сумма (например: 2 300)\n' \
                + '3. Выйти (например: 3)\n'
print(info_str)

while True:
    str_val = input(f'Введите данные через пробел: ').strip()
    list_val = str_val.split(' ')
    if len(list_val) == 2 and list_val[0].isdigit() and list_val[1].isdigit() or len(list_val) == 1 and list_val[0].isdigit():
        type_com = int(list_val[0])
        if len(list_val) == 2:
            data_com = int(list_val[1])
            match type_com:
                case 1:
                    print_val = get_tax(data_atm)
                    print(print_val) if print_val else None
                    data_atm[CASH_INDEX] = data_com
                    print(replenishment(data_atm))
                case 2:
                    print_val = get_tax(data_atm)
                    print(print_val) if print_val else None
                    data_atm[CASH_INDEX] = data_com
                    print(cash_withdrawal(data_atm))
                case _:
                    print('Не верный формат. Введите данные через пробел, (например: 1 500)')
        else:
            if type_com == 3:
                print(f'Баланс: {round(data_atm[BALANCE_INDEX], R_SIZE)} \n   До свидания')
                break
            else:
                print('Не верный формат. Введите данные через пробел, (например: 1 500)')
    else:
        print('Не верный формат. Введите данные через пробел, (например: 1 500)')
