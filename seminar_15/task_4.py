# Задание №4
# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.

import locale
from datetime import date, datetime
import logging

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # the ru locale is installed

logging.basicConfig(format='{levelname:<8} - {asctime}. {msg}, в строке {lineno:03d}',
                    style='{',
                    filename='log_date_err.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.ERROR,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger_val = logging.getLogger(__name__)


def convert_text_to_date(date_str: str):
    """
    Функция преобразовывает строковое представление даты в объект date, логирует ошибки если они есть.

    :param date_str: строковое представление даты;
    :return: дата в формате date или None если не удалось преобразовать.
    """
    date_str.lower()
    try:
        week, weekday, month = date_str.split()
        weekday_str = weekday
        month_str = month
        week_str = week
    except ValueError as e:
        logger_val.error(e)
        return None
    for item in ('а', 'е', 'и', 'о', 'э', 'ю', 'я', 'у'):
        weekday = weekday.replace(item, '')
    try:
        week, _ = week.split('-')
        if month == 'мая':
            month = 'май'
        week, weekday, month = int(week), weekday[:2].title(), month[:3].lower()
        month = datetime.strptime(month.encode('utf-8').decode('cp1251'), '%b').month
        week_iso = month * 4 + week
        date_val = datetime.strptime(
            f'{datetime.now().year} {week_iso} {month} {weekday}'.encode('utf-8').decode('cp1251'),
            '%Y %W %m %a')
        if date_val.month == month:
            return date_val.day
        else:
            logger_val.error(f'{week_str} {weekday_str} нет в {month_str}')
    except ValueError as e:
        logger_val.error(str(e).encode('cp1251').decode('utf-8'))
    return None


if __name__ == '__main__':
    print(convert_text_to_date('1-й понедельник ноября'))
