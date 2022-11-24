from functools import reduce

print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')


def sum_nbrs(arg):
    lst = [int(i) for i in arg if i != '.' and i != ',']
    result = reduce((lambda x, y: x + y), lst)
    return result


args_ = input('\nВведите число: ')
print(
    f'Результат суммирования цифр в числе {args_} равен {sum_nbrs(args_)}')
