# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

STR_INDEX = 1
UTF8_INDEX = 0

user_word = input('Введите строку текста: ').split()
user_word_utf_8 = [i.encode('UTF-8') for i in user_word]
list_str_utf8 = list(zip(user_word_utf_8, user_word))
list_str_utf8.sort()
max_len_word = 0
for item in list_str_utf8:
    if max_len_word < len(item[STR_INDEX]):
        max_len_word = len(item[STR_INDEX])
for i, item in enumerate(list_str_utf8, 1):
    print(f'{i} {item[STR_INDEX]: >{max_len_word}}')
