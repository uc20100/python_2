# 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

SIDE_A = 7
SIDE_B = 8
SIDE_C = 7

if SIDE_A > SIDE_B + SIDE_C or SIDE_B > SIDE_A + SIDE_C or SIDE_C > SIDE_A + SIDE_B:
    print('Треугольника с такими сторонами не существует')
elif SIDE_A == SIDE_B == SIDE_C:
    print('Это равносторонний треугольник')
elif SIDE_A == SIDE_B or SIDE_A == SIDE_C or SIDE_C == SIDE_B:
    print('Это равнобедренный треугольник')
else:
    print('Это разносторонний треугольник')



# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу 
# и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. 

MIN_LIMIT = 0
MAX_LIMIT = 100_000

while True:
    user_number = int(input('Введите положительное число, меньше 100 000: '))
    if MIN_LIMIT > user_number or user_number > MAX_LIMIT:
        print('Не верный формат числа')
    else:
        break

i = 1
while i < user_number:
    if user_number % i == 0 and not i == 1:
        print('Число составное')
        break
    i += 1
else:
    if user_number == 0:
        print('Число не простое и не составное')
    else:
        print('Число простое')



# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:  
#     from random import randint  
#     num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint 

LOWER_LIMIT = 0
UPPER_LIMIT = 1_000
NUMBER_OF_ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(1, NUMBER_OF_ATTEMPTS+1):
    user_num = int(input(f'Угадайте число (попытка {i}): '))
    if num > user_num:
        print('Надо больше')
    elif num < user_num:
        print('Надо меньше')
    else:
        print('Ура! Вы угадали')
        break
else:
    print(f'Попытки исчерпаны. Число было {num}')




# -------------------------------------------------------------------------------------------------------------------------------
# ЗАДАЧИ КОТОРЫЕ НЕ ДОДЕЛАЛИ НА СЕМИНАРЕ

# Задание №9
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

print('                ТАБЛИЦА УМНОЖЕНИЯ')
for i in range(2, 10, 4):
    for j in range(2, 10):
        for k in range(0, 4):
            print(f'{i+k} X {j} = {((i+k)*j):{2}}    ', end='')
        print('')
    print('')



# Задание №8
# 📌 Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

spruce_rows = int(input('Задайте количество рядов елки: '))

for i in range(1, spruce_rows*2, 2):
    for _ in range(((spruce_rows*2)-i)//2):
        print(' ', end='')
    for _ in range(i):
        print('*', end='')
    print('')



# Задание №7
# 📌 Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# 📌 Для цифры верните её квадрат, например 5 - 25
# 📌 Для двузначного числа произведение цифр, например 30 - 0
# 📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
# 📌 Если число не из диапазона, запросите новое число
# 📌 Откажитесь от магических чисел
# 📌 В коде должны быть один input и один print

MIN_NUMBER = 1
MAX_NUMBER = 999
SQUARE = 1
MULTIPLICATION = 2

while True:
    user_number_str = input(f'Введите число от {MIN_NUMBER} до {MAX_NUMBER}: ')
    if MIN_NUMBER <= int(user_number_str) <= MAX_NUMBER:
        break

if len(user_number_str) == SQUARE:
    result_value = f'Квадрат числа {user_number_str} = {int(user_number_str)**2}'
elif len(user_number_str) == MULTIPLICATION:
    result_value = f'Произведение цифр числа {user_number_str} = {int(user_number_str[0])*int(user_number_str[1])}'
else:
    new_number = ''
    new_number += user_number_str[2]
    new_number += user_number_str[1]
    new_number += user_number_str[0]
    result_value = f'Зеркальное отображение числа {user_number_str} = {new_number}'
print(result_value)
        
   
