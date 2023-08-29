# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

HEX = 16


def int_to_hex_char(in_value: int) -> str:
    """
       Функция выполняет перекодирование десятичного числа от 0 до 15 в
       шестнадцатеричный формат
       :param in_value: число в десятичном формате
       :return: число в шестнадцатеричном формате
    """
    match in_value:
        case 10:
            result = 'A'
        case 11:
            result = 'B'
        case 12:
            result = 'C'
        case 13:
            result = 'D'
        case 14:
            result = 'E'
        case 15:
            result = 'F'
        case _:
            result = str(in_value)
    return result


def int_to_new(in_value: int, calculation_system: int) -> str:
    """
    Функция выполняет перекодирование десятичного числа в
    выбранный формат
    :param in_value: число в десятичном формате
    :param calculation_system: система исчисления
    :return: результат в выбранной системе исчисления
    """
    result = ''
    while in_value >= calculation_system:
        result = int_to_hex_char(in_value % calculation_system) + result
        in_value //= calculation_system
    else:
        result = int_to_hex_char(in_value) + result
    if calculation_system == HEX:
        result = '0x' + result
    return result


while True:
    in_str = input('Введите целое число: ')
    if in_str.isdigit():
        value = int(in_str)
        break
    else:
        print('Ошибка преобразования, повторите ввод целого числа.')

print(f'Результат:  {int_to_new(value, HEX)}')
print(f'Проверка:   {hex(value)}')
