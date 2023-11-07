# Задание №1
# 📌 Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

def modification_str(in_str: str):
    """
    Функция удаляет в строке все символы не латинского алфавита и пробелов и переводит их в нижний регистр.

    :param in_str: исходная строка;
    :return: модифицированная строка.
    """
    ret_str = in_str
    en_chr = [chr(i + j) for i in range(0x41, 0x7A, 0x5A - 0x41 + 7) for j in range(0x5A - 0x41 + 1)]
    en_chr.append(chr(0x20))
    for item in in_str:
        if not (item in en_chr):
            ret_str = ret_str.replace(item, '')
    return ret_str.lower()


if __name__ == '__main__':
    print(modification_str('Hello World, Привет мир!'))
