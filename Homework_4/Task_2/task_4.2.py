print('Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.')


def rule_two(num):
    data = [0, 2, 4, 6, 8]
    res = num % 10
    if (res in data):
        return True
    else:
        return False


def rule_three(num):
    res = 0
    while num > 0:
        digit = num % 10
        res = res + digit
        num = num // 10
    if (res % 3 == 0):
        return True
    else:
        return False


def rule_four(num):
    digit_1 = num % 10
    digit_2 = (num // 10) % 10
    if (digit_1 + digit_2) == 0 or (digit_2*10+digit_1) % 4 == 0:
        return True
    else:
        return False


def rule_five(num):
    if num % 10 == 0 or num % 10 == 5:
        return True
    else:
        return False


def rule_six(num):
    if (num % 2) == 0 and (num % 3) == 0:
        return True
    else:
        return False


def rule_seven(num):
    digit_1 = (num % 10)*2
    digit_2 = num // 10
    if (digit_2-digit_1) % 7 == 0:
        return True
    else:
        return False


def rule_eight(num):
    digit_1 = num % 10
    digit_2 = (num//10) % 10
    digit_3 = ((num//10)//10) % 10
    res = digit_3*100+digit_2*10+digit_1
    if res == 0 or res % 8 == 0:
        return True
    else:
        return False


def rule_nine(num):
    res = 0
    while num > 0:
        digit = num % 10
        res = res + digit
        num = num // 10
    if (res % 9 == 0):
        return True
    else:
        return False


def num_calc(num):
    result = []
    calc = num
    while calc > 1:
        while rule_two(calc) is True:
            calc = calc / 2
            result.append(2)
        while rule_three(calc) is True:
            calc = calc / 3
            result.append(3)
        while rule_four(calc) is True:
            calc = calc / 4
            result.append(4)
        while rule_five(calc) is True:
            calc = calc / 5
            result.append(5)
        while rule_six(calc) is True:
            calc = calc / 6
            result.append(6)
        while rule_seven(calc) is True:
            calc = calc / 7
            result.append(7)
        while rule_eight(calc) is True:
            calc = calc / 8
            result.append(8)
        while rule_nine(calc) is True:
            calc = calc / 9
            result.append(9)
        if calc > 1:
            result.append(int(calc))
        calc -= calc
    print(result)


num = int(input('Введите натуральное число: '))
if num < 0:
    num_calc(-num)
else:
    num_calc(num)
