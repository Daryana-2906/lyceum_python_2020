from datetime import datetime

def get_days_between_days(first_date, second_date):

    first_date = datetime.strptime(first_date, '%d.%m.%Y')
    second_date = datetime.strptime(second_date, '%d.%m.%Y')

    if first_date < second_date:
        delta = second_date - first_date
    elif first_date > second_date:
        delta = first_date - second_date

    end = str(delta)
    return end.split( )[0]

if __name__ == '__main__':
    user_first_date = input('first date in format DD.MM.YYYY: ')
    user_second_date = input('second date in format DD.MM.YYYY: ')
    print('there are', get_days_between_days(user_first_date, user_second_date), 'days between these dates')
