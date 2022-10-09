from cgi import print_arguments
from unittest import result


print('Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.')


def lst_gen(num, lst):
    for i in range(1, num+1):
        result = (1+1/i)**i
        lst.append(round(result, 2))


def lst_sum(lst):
    result = 0
    for i in range(0, len(lst)):
        result = result + lst[i]
    return result


args_lst = []
args_ = int(input('Введите число N: '))

lst_gen(args_, args_lst)
print(args_lst)
print(lst_sum(args_lst))
