from datetime import datetime

from pytz import timezone
import pytz


def list_all_timezones():
    for tz in pytz.all_timezones:
        print(tz)


if __name__ == '__main__':
    current_date_time = datetime.now()
    print(current_date_time)  # ANSI

    current_date_time_str = current_date_time.strftime(
        '%d/%m/%Y %H:%M:%S')  # More on these patterns at https://man7.org/linux/man-pages/man3/strftime.3.html

    print(current_date_time_str)  # DD/MM/YYYY HH24:mm:SS

    datetime_as_str = "14/08/2023 20:03:06"
    str_as_datetime = datetime.strptime(datetime_as_str, '%d/%m/%Y %H:%M:%S')
    print(str_as_datetime)

    sao_paulo_timezone = timezone('America/Sao_Paulo')
    sao_paulo_datetime = current_date_time.astimezone(sao_paulo_timezone)
    sao_paulo_datetime_str = sao_paulo_datetime.strftime('%d/%m/%Y %H:%M:%S')
    print(sao_paulo_datetime_str)

    lisbon_timezone = timezone('Europe/Lisbon')
    lisbon_datetime = current_date_time.astimezone(lisbon_timezone)
    lisbon_datetime_str = lisbon_datetime.strftime('%d/%m/%Y %H:%M:%S')
    print(lisbon_datetime_str)

    # list_all_timezones()
