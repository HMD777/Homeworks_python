print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')


def sum_nbrs(arg):
    result = 0
    for i in arg:
        if i == '.' or i == ',':
            result = result + 0
        else:
            result = result + int(i)
    return result


args_ = input('\nВведите число: ')
print(f'Результат суммирования цифр в числе {args_} равен {sum_nbrs(args_)}')
