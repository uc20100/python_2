# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def gen_fibonacci(step: int):
    """
    Генератор чисел Фибоначчи.

    :param step: количество шагов генератора
    """
    value_1 = 0
    value_2 = 1
    value_result = None

    for i in range(step):
        match i:
            case 0:
                value_result = 0
            case 1:
                value_result = 1
            case _:
                value_result = value_1 + value_2
                value_1 = value_2
                value_2 = value_result
        yield value_result


for item in gen_fibonacci(20):
    print(item, end=' ')
