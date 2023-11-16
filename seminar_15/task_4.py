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
    for item_ in ('а', 'е', 'и', 'о', 'э', 'ю', 'я', 'у'):
        weekday = weekday.replace(item_, '')
    try:
        week, _ = week.split('-')
        if month == 'мая':
            month = 'май'
        week, weekday, month = int(week), weekday[:2].title(), month[:3].lower()
        month = datetime.strptime(month.encode('utf-8').decode('cp1251'), '%b').month
        weekday = weekday.encode('utf-8').decode('cp1251')
        week_iso = datetime(datetime.now().year, month, 2, ).isocalendar().week
        try:
            # Точное вычисление недели в году в зависимости от года, недели в году, дня недели
            test_moth = datetime.strptime(
                f'{datetime.now().year} {week_iso} {weekday}', '%Y %W %a').month
            if test_moth != month:
                week_iso += week
            else:
                week_iso += week - 1

            date_val = datetime.strptime(
                f'{datetime.now().year} {week_iso} {weekday}',
                '%Y %W %a')
        except ValueError:
            logger_val.error('Ошибка преобразование строки в дату')
            return None

        if date_val.month == month:
            return date_val.day
        else:
            logger_val.error(f'{week_str} {weekday_str} нет в {month_str}')
            return None
    except ValueError as e:
        logger_val.error(str(e).encode('cp1251').decode('utf-8'))


if __name__ == '__main__':
    str_date = ['1-й понедельник января', '1-й вторник февраля', '1-я среда марта',
                '1-й ЧТ АПР', '3-я среда мая', '1-я субб июнь',
                '1-й воскресенье июля', '1-й понед авгус', '1-й понедельник сентябрь',
                '1-й понедельник октября', '4-й понедельник ноября', '1-й понедельник декабря']
    for item in str_date:
        print(f'{item} - {convert_text_to_date(item)}')
