"""
Проверка всех модулей
"""

# Импорт модулей для задания 1
from file_many_format.task_1 import multiplication_json, generate_multiplication_file
import json
# Импорт модулей для задания 2
from file_many_format.task_2 import create_user_json
# Импорт модулей для задания 3
from file_many_format.task_3 import convert_to_csv
# Импорт модулей для задания 4
from file_many_format.task_4 import convert_to_json
# Импорт модулей для задания 5
from file_many_format.task_5 import json_to_pickle, clear_and_copy
# Импорт модулей для задания 6
from file_many_format.task_6 import pickle_to_csv
# Импорт модулей для задания №7
from file_many_format.task_7 import read_csv
import pickle
# Импорт модулей для домашнего задания
from file_many_format.task_home_work import generate_folder_and_file, info_folder

FOLDER = 'user_folder'
GENERATE_FOLDER = 'generate_folder\\other\\NoName\\просто_папка'

# * Задание №1
#   - Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
#   - Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
#   - Имена пишите с большой буквы.
#   - Каждую пару сохраняйте с новой строки.

# Формируем файл с псевдоименами и произведением чисел
generate_multiplication_file('numbers.txt', 8, 'pseudonyms.txt',
                             5, 'multiplication.txt')
# Формируем файл JSON
multiplication_json('multiplication.txt', 'multiplication.json')
# Печатаем JSON файл
with open('multiplication.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
print(f'Файл JSON: {new_dict = }')
print()

# Задание №2
# 📌 Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в
# JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные
# должны сохраняться.

create_user_json('user.json')
print()

# Задание №3
# 📌 Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

convert_to_csv('user.json', 'user.csv')

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

convert_to_json('user.csv', 'user_upgrade.json')

# Задание №5
# 📌 Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

# Подготавливаем директорию
clear_and_copy(FOLDER)
# преобразовываем json в pickle
json_to_pickle(FOLDER)

# Задание №6
# 📌 Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

pickle_to_csv(f'{FOLDER}\\user_upgrade.pickle', f'{FOLDER}\\user_upgrade.csv')

# Задание №7
# 📌 Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.
list_bytes = read_csv(f'{FOLDER}\\user_upgrade.csv')
print(f'pickle строка, вид_1: \n{pickle.loads(list_bytes[0])}')
print()
print(f'pickle строка, вид_2: {pickle.loads(list_bytes[1]) = }')
print()

# Домашнее задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
#     ○ Для дочерних объектов указывайте родительскую директорию.
#     ○ Для каждого объекта укажите файл это или директория.
#     ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.
print('ДОМАШНЕЕ ЗАДАНИЕ')
file_gen = dict(txt=10, doc=15, pdf=20, js=5, html=10, zip=5, rar=7, bmp=20, jpg=3, png=5, avi=7, mp4=10)
sort_fl = dict(Видео=['avi', 'mp4'], Изображения=['bmp', 'jpg', 'png'], Документы=['doc', 'exl', 'pdf'],
               Архивы=['zip', 'rar'], Интернет=['html', 'js'])
# Создаем файлы и каталоги (чтобы в ручную не мучиться)
generate_folder_and_file(directory=GENERATE_FOLDER, file_dict=file_gen, sort_dict=sort_fl, file_name='file_')
# Создаём отчёты о файлах и каталогах
inf_fl, *_ = GENERATE_FOLDER.split('\\')
info_folder(inf_fl, 'report_folder.json', 'report_folder.csv', 'report_folder.pickle')
# Проверяем на чтение pickle файл
with (open('report_folder.pickle', 'rb') as f_read):
    print(f'Проверка чтения инфы о каталогах: {pickle.load(f_read) = }')
