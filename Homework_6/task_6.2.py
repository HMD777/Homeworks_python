import random
from functools import reduce

print('Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')


def odd_sum(array):
    result = 0
    for i in range(len(array)):
        if i % 2 != 0:
            result = result + array[i]
    return result


array_len = int(input('\nВведите длинну массива: '))
min_ = int(input('Введите минимальное число массива: '))
max_ = int(input('Введите максимальное число массива: '))

array_ = [random.randint(min_, max_) for i in range(array_len)]


print(f'Сгенерирован массив: {array_}')
print(f'Сумма нечетных возиций равен: {odd_sum(array_)}')
