# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random as rnd


def random_number(name: str, lines: int):
    """
    Функция заполняет файл случайными числами


    :param name: имя файла
    :param lines: количество строк
    :return:
    """
    with open(f'{name}', 'a', encoding='utf-8') as f:
        for _ in range(lines):
            print(f'{rnd.randint(-1_000, 1000)} | {rnd.uniform(-1_000, 1_000)}', file=f)


# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

def pseudonyms(name: str, lines):
    """
    Функция генерит псевдоимена.

    :param name: имя файла
    :param lines: количество строк
    :return:
    """
    vowels = ('а', 'е', 'и', 'о', 'э', 'ю', 'я')
    count = 0

    with open(f'{name}', 'w', encoding='utf-8') as f:
        while count < lines:
            result_str = ''
            for _ in range(8):
                result_str += chr(rnd.randint(0x430, 0x44f))
            for item in vowels:
                if item in result_str:
                    result_str = result_str[0].upper() + result_str[1::]
                    print(result_str, file=f)
                    count += 1
                    break


# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def multiplication(number_file: str, pseudonyms_file: str, result_file):
    """
    Функция создает новый файл из двух заданных.

    :param number_file: файл с числами
    :param pseudonyms_file: файл с псевдоименами
    :param result_file: скомпилированный файл
    :return:
    """
    with (
        open(f'{number_file}', 'r', encoding='utf-8') as nf,
        open(f'{pseudonyms_file}', 'r', encoding='utf-8') as pf,
        open(f'{result_file}', 'w', encoding='utf-8') as rf
    ):
        print()
        mul_result = 0
        end_nf = False
        end_pf = False
        while True:
            if not (nf_read := nf.readline()[:-1]):
                if end_pf:
                    break
                else:
                    end_nf = True
                    nf.seek(0, 0)
                    nf_read = nf.readline()[:-1]
            if not (pf_read := pf.readline()[:-1]):
                if end_nf:
                    break
                else:
                    end_pf = True
                    pf.seek(0, 0)
                    pf_read = pf.readline()[:-1]

            list_number = nf_read.split('|')
            mul_result = int(list_number[0]) * float(list_number[1])
            if mul_result < 0:
                rf.write(f'{pf_read.upper()}  {abs(mul_result)}\n')
            else:
                rf.write(f'{pf_read.lower()}  {round(mul_result, 0):.0f}\n')


if __name__ == '__main__':
    random_number('numbers.txt', 3)
    pseudonyms('pseudonyms.txt', 5)
    multiplication('numbers.txt', 'pseudonyms.txt', 'multiplication.txt')
