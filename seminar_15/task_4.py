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
    except ValueError as e:
        logger_val.error(e)
        return None
    weekday_str = weekday
    for item in ('а', 'е', 'и', 'о', 'э', 'ю', 'я', 'у'):
        weekday = weekday.replace(item, '')
    try:
        week, _ = week.split('-')
        if month == 'мая':
            month = 'май'
        week, weekday, month = (int(week), weekday[:2].title(), month[:3].lower())
    except ValueError as e:
        logger_val.error(e)
        return None

    str_d = f'{weekday} {month}'.encode('utf-8').decode('cp1251')
    try:
        read_date = datetime.strptime(str_d, '%a %b')
    except ValueError as e:
        logger_val.error(str(e).encode('cp1251').decode('utf-8'))
        return None
    month = read_date.month
    weekday = read_date.isoweekday()
    week_iso = month * 4 + week - 1

    try:
        result_val = date.fromisocalendar(datetime.now().year, week_iso, weekday)
        if result_val.month != month:
            logger_val.error(f'Ошибка количества "{weekday_str} = {week}"')
            return None
        return result_val
    except ValueError as e:
        logger_val.error(str(e).encode('cp1251').decode('utf-8'))

    return None


if __name__ == '__main__':
    print(convert_text_to_date('1-й четверг октября'))
