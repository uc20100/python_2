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

print()
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

print('')
# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = {"Евгений": ("одежда", "еда", "палатка"), "Алексей": ("одежда", "еда", "компас"),
        "Роман": ("одежда", "посуда", "пила", "топор")}

same_things = None
for item in hike:
    if item == list(hike.keys())[0]:
        same_things = set(hike[item])
    else:
        same_things = same_things & set(hike[item])
print(f'Вещи которые взяли все: {same_things}')

one_things = None
other_things = {1, 2}
other_things.clear()
unique_things = {1, 2}
unique_things.clear()
for i in hike:
    for j in hike:
        if i == j:
            one_things = set(hike[j])
        else:
            other_things |= set(hike[j])
    unique_things = unique_things | (one_things - other_things)
    other_things.clear()
print(f'Уникальные вещи: {unique_things}')

one_things = None
other_things = {1, 2}
other_things.clear()
not_things = {1, 2}
not_things.clear()
for i in hike:
    for j in hike:
        if i == j:
            one_things = set(hike[j])
        else:
            if other_things == set():
                other_things = set(hike[j])
            else:
                other_things &= set(hike[j])
    not_things = other_things - one_things
    if not_things != set():
        print(f'У {i} нет {not_things}, которую взяли все')
    other_things.clear()
