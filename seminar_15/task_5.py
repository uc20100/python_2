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
                    level=logging.DEBUG,
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
        month_str = month
        week_str = week
    except ValueError as e:
        logger_val.error(e)
        return None
    for item_ in ('а', 'е', 'и', 'о', 'э', 'ю', 'я', 'у'):
        weekday = weekday.replace(item_, '')

    if not week.isdigit():
        try:
            week, _ = week.split('-')
            week = int(week)
        except ValueError:
            logger_val.error(f'Ошибка конвертации строки "{week_str}"')
            return None
    else:
        week = int(week)

    if not month.isdigit():
        if month == 'мая':
            month = 'май'
        month = month[:3].lower().encode('utf-8').decode('cp1251')
        try:
            month = datetime.strptime(month, '%b').month
        except ValueError:
            logger_val.error(f'Ошибка конвертации строки "{month_str}"')
            return None
    else:
        month = int(month)

    if not weekday.isdigit():
        weekday = weekday[:2].title().encode('utf-8').decode('cp1251')
    else:
        weekday = int(weekday)
    # Номер недели в году в зависимости от месяца
    week_iso = datetime(datetime.now().year, month, 2, ).isocalendar().week

    try:
        # Точное вычисление недели в году в зависимости от года, месяца, дня недели
        test_moth = datetime.strptime(
            f'{datetime.now().year} {week_iso} {weekday}', '%Y %W %a').month
        if test_moth != month:
            week_iso += week
        else:
            week_iso += week - 1
        # Вычисление дня в зависимости от года, месяца, дня недели в году
        if isinstance(weekday, str):
            date_val = datetime.strptime(
                f'{datetime.now().year} {week_iso} {weekday}', '%Y %W %a')
        else:
            date_val = datetime.strptime(
                f'{datetime.now().year} {week_iso} {weekday}', '%Y %W %u')
        if date_val.month != month:
            logger_val.error(f'Задали слишком большое количество "{week_str}"')
            return None
    except ValueError:
        logger_val.error('Ошибка преобразование строки в дату')
        return None

    return date_val.day


if __name__ == '__main__':
    str_date = ['1-й понедельник января', '1-й вторник февраля', '1-я среда марта',
                '1-й четверг апреля', '1-я пятница мая', '1-я суббота июня',
                '1-й воскресенье июля', '1-й понедельник август', '1-й понедельник сентябрь',
                '1-й понедельник октября', '4-й понедельник ноября', '1-й понедельник декабря']
    for item in str_date:
        print(f'{item} - {convert_text_to_date(item)}')


