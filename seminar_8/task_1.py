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

__all__ = ['multiplication_json']
if __name__ == '__main__':
    from file_func.task_1 import random_number
    from file_func.task_2 import pseudonyms
    from file_func.task_3 import multiplication
import json


def multiplication_json(in_file: str, out_file: str):
    """
    Функция создает файл в формате JSON из текстового файла

    :param in_file: файл в текстовом формате
    :param out_file: файл в формате JSON
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
    # Формируем текстовый файл с псевдо именами и произведением чисел (из прошлого семинара)
    random_number('numbers.txt', 8)
    pseudonyms('pseudonyms.txt', 5)
    multiplication('numbers.txt', 'pseudonyms.txt', 'multiplication.txt')
    # Формируем файл JSON
    multiplication_json('multiplication.txt', 'multiplication.json')

    with open('multiplication.json', 'r', encoding='utf-8') as f:
        new_dict = json.load(f)
    print(f'{new_dict = }')
