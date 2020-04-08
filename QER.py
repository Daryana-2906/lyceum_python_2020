def sol_of_guadratic_equation(a, b, c):
    import math
    try:
        root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if root1 != root2:
            return root1, root2
        else:
            return root1
    except ValueError:
        return 'корней нет'
    
 if __name__ == '__main__':
    a = int(input('введите коэффициент перед х^2: '))
    b = int(input('введите коэффициент перед х: '))
    c = int(input('введите свободный член: '))

    print(sol_of_guadratic_equation(a, b, c))
