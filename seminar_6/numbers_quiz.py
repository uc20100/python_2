# 2. Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
import random as rn


def start_quiz(min_number: int, max_number: int, attempts: int, /) -> bool:
    """
    Функция угадывает число

    :param min_number: минимальный предел числа
    :param max_number: максимальный предел числа
    :param attempts: количество попыток для угадывания
    :return: угадали или нет
    """
    random_number = rn.randint(min_number, max_number)
    if __name__ == '__main__':
        print(f'{random_number = }, {min_number = }, {max_number = }, {attempts = }')

    for i in range(attempts):
        user_number = int(input('Введите число: '))
        if random_number == user_number:
            print('Ура, вы угадали!')
            return True
        else:
            if user_number > random_number:
                print(f'Надо меньше. Осталось {attempts-i-1} попыток')
            else:
                print(f'Надо больше. Осталось {attempts - i - 1} попыток')
    print('Повезет в другой раз )))')
    return False


if __name__ == '__main__':
    start_quiz(1, 10, 3)
