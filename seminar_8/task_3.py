"""
Модуль преобразования файлов из JSON в CSV
"""
# Задание №3
# 📌 Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

__all__ = ['convert_to_csv']
import csv
import json


def convert_to_csv(file_json: str, file_csv: str):
    """
    Функция конвертирует файл JSON в CSV файл

    :param file_json: JSON файл
    :param file_csv: CSV файл
    :return:
    """
    with (
        open(file_json, 'r', encoding='utf-8') as f_read,
        open(file_csv, 'w', newline='', encoding='utf-8') as f_write
    ):
        load_dict = json.load(f_read)
        csv_write = csv.writer(f_write, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(['level', 'identifier', 'name'])
        for key, item in load_dict.items():
            for key_2, value in item.items():
                csv_write.writerow([key, key_2, value])


if __name__ == '__main__':
    convert_to_csv('my_file.json', 'my_file.csv')
