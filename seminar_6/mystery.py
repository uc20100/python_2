# 4. Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

def solution(mystery_str: str, variant_solution: list, attempts: int):
    """
    Функция отгадывания загадки

    :param mystery_str: загадка
    :param variant_solution: варианты ответов
    :param attempts: количество попыток
    :return: возвращаем номер попытки с которой угадали загадку
    """
    print(f'Угадайте загадку: {mystery_str}. У вас есть {attempts} попытки.')
    for i in range(attempts):
        answer = input('Ваш ответ: ').lower()
        for item in variant_solution:
            if answer == item.lower():
                print("Ура, загадка разгадана!")
                return i
        else:
            print(f'У вас осталось {attempts-i-1} попыток')
    return 0

if __name__ == '__main__':
    data = ('Зимой и летом, одним цветом', ['Елка', 'Сосна', 'Пихта'], 3)
    solution(*data)
