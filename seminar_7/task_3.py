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
    multiplication('numbers.txt', 'pseudonyms.txt', 'multiplication.txt')
