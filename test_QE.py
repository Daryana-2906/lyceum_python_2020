from tasks_04.QER import sol_of_guadratic_equation

def test_two_roots():
    a, b, c = 2, 6, 0
    expected = (-3, 0)
    actual = sol_of_guadratic_equation(a, b, c)

    assert len(actual) == 2
    assert sorted(expected) == sorted(actual)


def test_one_root():
    a, b, c = 4, -4, 1
    expected = 0.5
    actual = sol_of_guadratic_equation(a, b, c)

    assert expected == actual

def test_no_roots():
    a, b, c = 3, -1, 7
    expected = 'no roots'
    actual = sol_of_guadratic_equation(a, b, c)

    assert expected == actual
