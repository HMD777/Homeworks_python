import math

print('Напишите программу, которая будет преобразовывать десятичное число в двоичное.')


def converter(data):
    result = str()
    num = data
    while num > 0:
        if num % 2 == 0:
            result += str(0)
            num = math.floor(num/2)
        elif num % 2 != 0:
            result += str(1)
            num = math.floor(num/2)
    return result[::-1]


num = int(input('\nВведите число для преобразования: '))
print(f'Результат: {converter(num)}')
