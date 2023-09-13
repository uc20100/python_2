# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

# Задание из второго семинара
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
MULTIPLICITY = 50
BIG_MONEY = 5_000_000

COUNT_INDEX = 0
BALANCE_INDEX = 1
STORY_INDEX = 2

data_atm = [0, 0, []]


def add_3_percent(*, data: list) -> str:
    """
    Функция при каждой 3-й операции индексирует вклад на 3%.

    :param data: счетчик операций, баланс счета, история операций
    :return: информация об операции
    """
    if data[COUNT_INDEX] >= 2:
        data[COUNT_INDEX] = 0
        data[STORY_INDEX].append(data[BALANCE_INDEX] * 0.03)
        data[BALANCE_INDEX] *= 1.03
        return f'Счетчик {data[COUNT_INDEX]}. Вам начислено 3%, баланс {round(data[BALANCE_INDEX], R_SIZE):_}₽ '
    else:
        return f'Счетчик {data[COUNT_INDEX]}'


def replenishment(*, cash: int, data: list) -> str:
    """
    Функция пополняет баланс.

    :param cash: сумма взноса
    :param data: счетчик операций, баланс счета, история операций
    :return: информация об операции
    """
    if not cash % MULTIPLICITY:
        print(add_3_percent(data=data_atm))
        data[STORY_INDEX].append(cash)
        data[BALANCE_INDEX] += cash
        data[COUNT_INDEX] += 1
        return f'Вы положили {cash}₽, баланс {round(data[BALANCE_INDEX], R_SIZE):_}₽'
    else:
        return f'Ошибка операции, укажите сумму кратную {MULTIPLICITY}₽, баланс {round(data[BALANCE_INDEX], R_SIZE):_}₽'


def cash_withdrawal(*, cash: int, data: list) -> str:
    """
    Функция выдачи наличных.

    :param cash: сумма выдачи
    :param data: счетчик операций, баланс счета, история операций
    :return: информация об операции
    """
    if not cash % MULTIPLICITY:
        cash_percent = cash * 0.015
        if cash_percent < 30:
            cash_percent = 30
        elif cash_percent > 600:
            cash_percent = 600
        if data[BALANCE_INDEX] >= cash + cash_percent:
            print(add_3_percent(data=data_atm))
            data[BALANCE_INDEX] -= cash + cash_percent
            data[STORY_INDEX].append(-cash)
            data[STORY_INDEX].append(-cash_percent)
            data[COUNT_INDEX] += 1
            if 30 < cash_percent < 600:
                return (f'Вы сняли {cash}₽, баланс {round(data[BALANCE_INDEX], R_SIZE):_} , '
                        f'1.5% комиссия ({round(cash_percent, R_SIZE)}₽)')
            else:
                return (f'Вы сняли {cash}₽, баланс {round(data[BALANCE_INDEX], R_SIZE):_}₽, '
                        f'комиссия ({cash_percent}₽)')
        else:
            return (f'За снятие взимается плата ({cash_percent}₽), у вас не хватает средств. '
                    f'Баланс {round(data[BALANCE_INDEX], R_SIZE):_}₽')
    else:
        return f'Ошибка операции, укажите сумму кратную {MULTIPLICITY}₽, баланс {round(data[BALANCE_INDEX], R_SIZE):_}₽'


def get_tax(*, data: list) -> str | None:
    """
    Функция взимает налог на роскошь.

    :param data: счетчик операций, баланс счета, история операций
    :return: информация об операции
    """
    if data[BALANCE_INDEX] > BIG_MONEY:
        tax_val = data[BALANCE_INDEX] * 0.1
        data[BALANCE_INDEX] -= tax_val
        data[STORY_INDEX].append(-tax_val)
        return f'Взяли налог на роскошь 10% ({round(tax_val, R_SIZE)}₽), баланс {round(data[BALANCE_INDEX], R_SIZE):_}₽'
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
    if len(list_val) == 2 and list_val[0].isdigit() and list_val[1].isdigit() or len(list_val) == 1 and list_val[
        0].isdigit():
        type_com = int(list_val[0])
        if len(list_val) == 2:
            data_com = int(list_val[1])
            match type_com:
                case 1:
                    print_val = get_tax(data=data_atm)
                    print(print_val) if print_val else None
                    print(replenishment(cash=data_com, data=data_atm))
                case 2:
                    print_val = get_tax(data=data_atm)
                    print(print_val) if print_val else None
                    print(cash_withdrawal(cash=data_com, data=data_atm))
                case _:
                    print('Не верный формат. Введите данные через пробел, (например: 1 500)')
        else:
            if type_com == 3:
                print(f'Баланс: {round(data_atm[BALANCE_INDEX], R_SIZE):_}₽ \n   До свидания')
                break
            else:
                print('Не верный формат. Введите данные через пробел, (например: 1 500)')
    else:
        print('Не верный формат. Введите данные через пробел, (например: 1 500)')
