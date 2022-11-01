from math import factorial
from decimal import *


def chudnovsky():
    pi = Decimal(0)
    k = 0
    n = 100
    getcontext().prec = n
    while k < n:
        pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3)
                                                               * (factorial(3*k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi


def count_float(num):
    result = 0
    while num < 1:
        num *= 10
        result += 1
    return result


def num_check(num):
    result = 0
    i = 0
    while i < len(num):
        if num[i] != '.':
            result += int(num[i])
        i += 1
    if result == 1:
        return True
    else:
        False


pi = chudnovsky()
str_pi = str(pi)


print('Вычислить число П c заданной точностью d (Пример - при $d = 0.001, π = 3.141)')
num = input('Введите число d: ')

if num.find('.') == True:
    if num[-1] == '1':
        if num_check(num) == True:
            num1 = float("{:30}".format(num))
            num2 = count_float(num1)
            print(str_pi[:num2+2])
        else:
            print('Ошибка! Введите данные по формату!')
    else:
        print('Ошибка! Введите данные по формату!')
else:
    print('Ошибка! Вы ввели не верные данные!')
