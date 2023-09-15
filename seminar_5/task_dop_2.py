# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def gen_prime_numbers(n: int):
    """
    Генератор простых чисел.

    :param n: количество простых чисел
    :return: простые числа
    """
    prime_numbers = 1
    count = 0
    divider = 2

    while count < n:
        prime_numbers += 1
        divider = 2
        while prime_numbers % divider == 0 and prime_numbers > divider:
            prime_numbers += 1
            divider = 2
        count += 1
        yield prime_numbers


print(*gen_prime_numbers(20))
