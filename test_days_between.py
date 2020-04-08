from days_between import get_days_between_days

def test_first():
    first_date = '21.06.2020'
    second_date = '14.09.2020'
    expected = '85'
    actual = get_days_between_days(first_date, second_date)

    assert expected == actual

def test_second():
    first_date = '08.04.1020'
    second_date = '13.02.1020'
    expected = '55'
    actual = get_days_between_days(first_date, second_date)

    assert expected == actual
