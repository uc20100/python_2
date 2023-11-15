# Задание №5
# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

import locale
from datetime import date, datetime
import logging

# Локаль почему-то не переключается на кодировку utf-8, перекодирую в функции
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # the ru locale is installed

logging.basicConfig(format='{levelname:<8} - {asctime}. {msg}, в строке {lineno:03d}',
                    style='{',
                    filename='log_date_err_2.log',
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
        if not week.isdigit():
            week, _ = week.split('-')
            week = int(week)
        else:
            week = int(week)

        if not month.isdigit():
            if month == 'мая':
                month = 'май'
            month = month[:3].lower()
            month = datetime.strptime(month.encode('utf-8').decode('cp1251'), '%b').month
        else:
            month = int(month)

        if not weekday.isdigit():
            weekday = weekday[:2].title()
        else:
            weekday = int(weekday)

        week_iso = month * 4 + week
        if isinstance(weekday, str):
            date_val = datetime.strptime(
                f'{datetime.now().year} {week_iso} {month} {weekday}'.encode('utf-8').decode('cp1251'),
                '%Y %W %m %a')
        else:
            date_val = datetime.strptime(
                f'{datetime.now().year} {week_iso} {month} {weekday}'.encode('utf-8').decode('cp1251'),
                '%Y %W %m %u')

        if date_val.month == month:
            return date_val.day
        else:
            logger_val.error(f'week = {week_str}, weekday = {weekday_str}, month = {month_str}')
    except ValueError as e:
        logger_val.error(str(e).encode('cp1251').decode('utf-8'))
    return None


if __name__ == '__main__':
    print(convert_text_to_date('4 понедельник ноябре'))
