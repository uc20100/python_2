"""
Модуль конвертации файлов CSV в JSON
"""
# Задание №4
# 📌 Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы
# функции.

__all__ = ['convert_to_json']
import json


def convert_to_json(file_csv: str, file_json: str):
    """
    Функция конвертирует файл CSV в JSON добавляя переменные

    :param file_csv: CSV файл
    :param file_json: JSON файл
    :return:
    """
    with (open(file_csv, 'r', encoding='utf-8') as f_read,
          open(file_json, 'w', encoding='utf-8') as f_write):
        list_json = []
        for i, row in enumerate(f_read, 0):
            if i == 0:
                key_level, key_identifier, key_name = row[:-1].split(',')
            else:
                value_level, value_identifier, value_name = row[:-1].split(',')

                id_ = str(i).rjust(10, '0')
                value_name = value_name[0].upper() + value_name[1::]
                hash_ = f'{value_name}_{value_identifier}'
                list_json.append({'id': id_, key_level: value_level, key_identifier: value_identifier,
                                  key_name: value_name, 'хеш': hash_})

        json.dump(list_json, f_write, ensure_ascii=False)


if __name__ == '__main__':
    convert_to_json('my_csv.csv', 'new_json.txt')
