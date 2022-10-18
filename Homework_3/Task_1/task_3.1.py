import random

print('Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')

def odd_sum (array):
    result = 0
    for i in range(len(array)):
        if i%2!=0:
            result = result + array[i]
    return result

def array_gen (array, array_len, min, max):
    for i in range(array_len):
        array.append(random.randint(min, max))

array_ = []
array_len = int(input ('\nВведите длинну массива: '))
min_ = int(input ('Введите минимальное число массива: '))
max_ = int(input ('Введите максимальное число массива: '))
array_gen(array_, array_len, min_, max_)
print(f'Сгенерирован массив: {array_}')
print(f'Сумма нечетных возиций равен: {odd_sum(array_)}')