from datetime import datetime, timedelta

week_day = input('Введите день недели с большой буквы: ')

def get_date_by_week_day(week_day):

    week_days = {'Понедельник': 0, 'Вторник': 1, 'Среда': 2, 'Четверг': 3, 'Пятница': 4, 'Суббота': 5, 'Воскресенье': 6}
    today = datetime.today()
    today_week_day = today.weekday()

    if today_week_day < week_days[week_day]:
        final_date = today - timedelta(days=today_week_day) + timedelta(days=week_days[week_day])
    elif today_week_day > week_days[week_day]:
        final_date = today + timedelta(days=6 - today_week_day) + timedelta(days=1 + week_days[week_day])
    elif today_week_day == week_days[week_day]:
        final_date = today

    end = datetime.strftime(final_date, '%d.%m.%Y')
    return end

print(get_date_by_week_day(week_day))
