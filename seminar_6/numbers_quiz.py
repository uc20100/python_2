# 3. Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
import random as rn
from sys import argv

__all__ = ['start_quiz']


def start_quiz(min_number: int = 1, max_number: int = 10, attempts: int = 3) -> bool:
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
                print(f'Надо меньше. Осталось {attempts - i - 1} попыток')
            else:
                print(f'Надо больше. Осталось {attempts - i - 1} попыток')
    print('Повезет в другой раз )))')
    return False


if __name__ == '__main__':
    gen_param = (int(argv[i]) for i in range(1, len(argv)))
    start_quiz(*gen_param)
