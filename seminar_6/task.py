# 8. Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

from puzzles import date, mystery, numbers_quiz, chess

# Модуль игры угадай число
numbers_quiz.start_quiz()
print()
print()

# Модуль игры угадай загадку
for mystery_str, variant_solution in mystery.get_dict().items():
    n_answer = mystery.solution(mystery_str, variant_solution)
    if n_answer > 0:
        mystery.save(mystery_str, n_answer)
mystery.view()
print()
print()

# Модуль проверки даты
date_str = '29.02.2000'
print(f'Проверка даты {date_str} = {date.check(date_str)}')
print()
print()

# ДЗ
# Модуль шахматы
# Проверка хорошей и плохой расстановки ферзей
good = [12, 36, 77, 84, 28, 41, 53, 65]
bad = [12, 36, 77, 84, 28, 41, 53, 63]

print(f'{chess.beating_queen(*good) = }')
print(f'{chess.beating_queen(*bad) = }')
print()
print()

# Генерация хорошей расстановки ферзей
print('Хорошие расстановки ферзей:')
good_queen = chess.random_queen()
for n, item in enumerate(good_queen, 1):
    print(f'{n} - {item}')
