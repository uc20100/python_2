# 8. Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

from puzzles import date, mystery, numbers_quiz

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
