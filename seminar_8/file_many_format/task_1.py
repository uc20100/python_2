"""
Модуль генерации файла JSON произведения чисел
"""
# * Задание №1
#   - Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
#   - Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
#   - Имена пишите с большой буквы.
#   - Каждую пару сохраняйте с новой строки.

__all__ = ['multiplication_json', 'generate_multiplication_file']
# Импорт для функции generate_multiplication_file
from file_func.task_1 import random_number
from file_func.task_2 import pseudonyms
from file_func.task_3 import multiplication
# Импорт для функции multiplication_json
import json


def generate_multiplication_file(number_file: str, row_number_file: int, pseudonyms_file: str,
                                 row_pseudonyms_file: int, multiplication_file: str):
    """
    Функция генерит файл с псевдоименами и произведением чисел.

    :param number_file: Файл с номерами
    :param row_number_file: Количество срок в файле с номерами
    :param pseudonyms_file: Файл с псевдоименами
    :param row_pseudonyms_file: Количество срок в файле с псевдоименами
    :param multiplication_file: Файл с произведением чисел и псевдоименами
    :return:
    """
    # Формируем текстовый файл с псевдо именами и произведением чисел (из прошлого семинара)
    random_number(number_file, row_number_file)
    pseudonyms(pseudonyms_file, row_pseudonyms_file)
    multiplication(number_file, pseudonyms_file, multiplication_file)


def multiplication_json(in_file: str, out_file: str):
    """
    Функция создает файл в формате JSON из текстового файла.

    :param in_file: Файл в текстовом формате
    :param out_file: Файл в формате JSON
    :return: 
    """
    json_dict = {}
    with(open(in_file, 'r', encoding='utf-8') as f_in,
         open(out_file, 'w', encoding='utf-8') as f_out):
        while read_str := f_in.readline():
            key, value = read_str.split()
            if value.isdigit():
                value = int(value)
            else:
                value = float(value)
            json_dict[key.upper()] = value
        json.dump(json_dict, f_out, ensure_ascii=False, separators=(',\n', ':'), )


if __name__ == '__main__':
    # Формируем файл с псевдоименами и произведением чисел
    generate_multiplication_file('../numbers.txt', 8, 'pseudonyms.txt',
                                 5, 'multiplication.txt')
    # Формируем файл JSON
    multiplication_json('../multiplication.txt', 'multiplication.json')
    # Печатаем JSON файл
    with open('../multiplication.json', 'r', encoding='utf-8') as f:
        new_dict = json.load(f)
    print(f'Файл JSON: {new_dict = }')


