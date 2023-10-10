"""
Модуль чтения CSV файла
"""

# Задание №7
# 📌 Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.

__all__ = ['read_csv']
import pickle


def read_csv(file_csv: str) -> tuple[bytes, bytes]:
    """
    Функция читает CSV файл и возвращает байтовый список

    :param file_csv: CSV файл
    :return: байтовая строка: [0] - CSV файл, [1] - словарь
    """
    result_str = ''
    with open(file_csv, 'r', encoding='utf-8') as f_read:
        for row in f_read:
            result_str += row
    str_bytes = pickle.dumps(result_str)

    result_list = []
    with open(file_csv, 'r', encoding='utf-8') as f_read_:
        for i, row_ in enumerate(f_read_, 0):
            if i == 0:
                key_1, key_2, key_3, key_4, key_5 = row_[:-1].split(',')
            else:
                val_1, val_2, val_3, val_4, val_5 = row_[:-1].split(',')
                result_list.append({key_1: val_1, key_2: val_2, key_3: val_3, key_4: val_4, key_5: val_5})
    dict_bytes = pickle.dumps(result_list)

    return str_bytes, dict_bytes


if __name__ == '__main__':
    list_bytes = read_csv('test_folder\\user_upgrade.csv')
    print(pickle.loads(list_bytes[0]))
    print()
    print(pickle.loads(list_bytes[1]))

