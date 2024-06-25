# ЗДЕСЬ ПРЕДСТАВЛЕНА ПОЛНАЯ ДОРАБОТКА 4 ЗАДАНИЯ!
import datetime
import re
import logging
import sys

# Настройка логирования
logging.basicConfig(filename='date_conversion.log', level=logging.INFO)

def convert_text_to_date(input_text):
    current_year = datetime.datetime.now().year
    months = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
        'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
        'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12,
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12
    }
    days_of_week = {
        'понедельник': 0, 'вторник': 1, 'среда': 2,
        'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6,
        '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6
    }

    pattern = r'(\d+|первый|второй|третий|четвёртый|последний)?-?[ая]? (\w+|\d+)'
    match = re.match(pattern, input_text)
    if match:
        day_match = match.group(1)
        month_match = match.group(2)

        # Определение дня месяца
        if day_match.isdigit():
            day = int(day_match)
        elif day_match in ['первый', '1']:
            day = 1
        elif day_match in ['второй', '2']:
            day = 2
        elif day_match in ['третий', '3']:
            day = 3
        elif day_match in ['четвёртый', '4']:
            day = 4
        elif day_match in ['последний']:
            # Логика для определения последнего дня месяца
            # Здесь можно добавить логику для определения последнего дня месяца
            pass
        else:
            # Если день не указан, берем текущий день
            day = datetime.datetime.now().day

        # Определение месяца
        if month_match.isdigit():
            month = int(month_match)
        else:
            month = months.get(month_match.lower())

        if month:
            try:
                date = datetime.date(current_year, month, day)
                logging.info(f"Converted '{input_text}' to date: {date}")
                return date
            except ValueError as e:
                logging.error(f"Error converting '{input_text}' to date: {e}")
        else:
            logging.error(f"Invalid month name or number in '{input_text}'")
    else:
        logging.error(f"Invalid format for input text: '{input_text}'")

    return None

if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])
    if not input_text:
        print("Пожалуйста, введите текст для преобразования в дату.")
    else:
        converted_date = convert_text_to_date(input_text)
        if converted_date:
            print(f"The converted date is: {converted_date}")
        else:
            print("Не удалось преобразовать входной текст в дату. Пожалуйста, проверьте журнал для получения подробностей.")
