a = input('text: ')

def result(a):
    b = []
    nums = a.split(' ')
    for num in nums:
        if num.isdigit():
            b.append(num)
        return b

print(result(a))
