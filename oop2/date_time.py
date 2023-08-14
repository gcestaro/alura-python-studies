from datetime import date, datetime, timezone, timedelta

if __name__ == '__main__':
    current_date = date.today()
    print(current_date)  # ANSI

    current_date = current_date.strftime('%d/%m/%Y')
    print(current_date)  # DD/MM/YYYY

    current_date_time = datetime.now()
    print(current_date_time)  # ANSI

    current_date_time = current_date_time.strftime('%d/%m/%Y %H:%M:%S')
    print(current_date_time)  # DD/MM/YYYY HH24:mm:SS

    datetime_as_str = "14/08/2023 19:44:29"
    str_as_datetime = datetime.strptime(datetime_as_str, '%d/%m/%Y %H:%M:%S')
    print(str_as_datetime)

    lisbon_timezone = timezone(timedelta(0))
    print(lisbon_timezone)

    sao_paulo_timezone = timezone(timedelta(hours=-3))
    print(sao_paulo_timezone)

    sao_paulo_date_time = str_as_datetime.astimezone(sao_paulo_timezone)
    sao_paulo_date_time_str = sao_paulo_date_time.strftime('%d/%m/%Y %H:%M:%S')

    lisbon_date_time = str_as_datetime.astimezone(lisbon_timezone)
    lisbon_date_time_str = lisbon_date_time.strftime('%d/%m/%Y %H:%M:%S')

    print(sao_paulo_date_time_str)
    print(lisbon_date_time_str)
