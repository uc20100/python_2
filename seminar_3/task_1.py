# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

# STR_INDEX = 1
# UTF8_INDEX = 0
#
# user_word = input('Введите строку текста: ').split()
# user_word_utf_8 = [i.encode('UTF-8') for i in user_word]
# list_str_utf8 = list(zip(user_word_utf_8, user_word))
# list_str_utf8.sort()
# max_len_word = 0
# for item in list_str_utf8:
#     if max_len_word < len(item[STR_INDEX]):
#         max_len_word = len(item[STR_INDEX])
# for i, item in enumerate(list_str_utf8, 1):
#     print(f'{i} {item[STR_INDEX]: >{max_len_word}}')


# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

user_str = input('Введите строку текста: ')
user_dict = {}
for item in user_str:
    if not user_dict.get(item):
        user_dict[item] = 1
    else:
        user_dict[item] += 1
print(user_dict)

