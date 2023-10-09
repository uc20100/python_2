"""
Модуль преобразования pickle файла в CSV файл
"""
# Задание №6
# 📌 Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

__all__ = ['pickle_to_csv']
import pickle
import csv


def pickle_to_csv(file_pickle: str, file_csv: str):
    """
    Функция преобразовывает pickle файл в CSV файл

    :param file_pickle: pickle файл
    :param file_csv: CSV файл
    :return:
    """
    with (open(file_pickle, 'rb') as f_read,
          open(file_csv, 'w', encoding='utf-8') as f_write):
        load_ = pickle.load(f_read)
        csv_write = csv.writer(f_write, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(list(load_[0].keys()))
        for item in load_:
            csv_write.writerow(list(item.values()))


if __name__ == '__main__':
    pickle_to_csv('test_folder\\user_upgrade.pickle', 'test_folder\\user_upgrade.csv')
