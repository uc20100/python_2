# 2. Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

def bonuses(*, name: list, rate: list, percent: list) -> dict:
    """
    Премии сотрудников.

    :param name: имя
    :param rate: ставка
    :param percent: процентная ставка
    :return: ведомость премий
    """
    yield {name_: rate_ * float(percent_[:-1])*0.01 for name_, rate_, percent_ in list(zip(name, rate, percent))}


name_user = ['Иванов', 'Петров', 'Сидоров']
rate_user = [100, 200, 300]
percent_user = ['10.5%', '5.5%', '6.1%']

for item in bonuses(name=name_user, rate=rate_user, percent=percent_user):
    print(item)
