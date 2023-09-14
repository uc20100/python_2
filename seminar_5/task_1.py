# 1. Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def string_decomposition(value: str):
    """
    Функция декомпозирует расположение и название файла.

    :param value: расположение файла
    :return: результат декомпозиции
    """
    path = value[:value.rfind('\\')+1]
    *_, name_file_all = value.split('\\')
    name_file, type_file = name_file_all.split('.')

    return path, name_file, type_file


print(string_decomposition('C:\Program Files\Windows Defender\example.doc'))