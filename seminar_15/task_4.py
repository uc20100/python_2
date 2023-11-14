# Задание №4
# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.
import locale
from datetime import datetime
from datetime import date

# loc = locale.getlocale()

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # the ru locale is installed


def convert_text_to_date(date_str: str):
    """
    Функция преобразовывает строковое представление даты в объект date, логирует ошибки если они есть.

    :param date_str: строковое представление даты;
    :return: дата в формате date.
    """

    date_str.lower()
    week, weekday, month = date_str.split()
    for item in ('а', 'е', 'и', 'о', 'э', 'ю', 'я'):
        weekday = weekday.replace(item, '')
    week, weekday, month = (int(week[:1]), weekday[:2].title(), month[:3].lower())
    str_d = f'{weekday} {month}'.encode('utf-8').decode('cp1251')
    read_date = datetime.strptime(str_d, '%a %b')
    month = read_date.month
    weekday = read_date.isoweekday()
    week_iso = month * 4 + week - 1

    return date.fromisocalendar(datetime.now().year, week_iso, weekday)


if __name__ == '__main__':
    print(convert_text_to_date('1-й четверг ноября'))
