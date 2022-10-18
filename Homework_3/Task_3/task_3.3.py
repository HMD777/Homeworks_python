import random


print('Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.')


def array_gen(array, array_len, min, max):
    for i in range(array_len):
        array.append(round(random.uniform(min, max), 2))


def array_sum(array):
    min = array[0] % 1
    max = array[len(array)-1] % 1
    for i in array:
        if i % 1 < min:
            min = i % 1
        elif i % 1 > max:
            max = i % 1
    result = round(max, 2) - round(min, 2)
    return result


array_ = []
array_len = int(input('\nВведите длинну массива: '))
min_ = int(input('Введите минимальное число массива: '))
max_ = int(input('Введите максимальное число массива: '))
array_gen(array_, array_len, min_, max_)

print(f'Сгенерирован массив: {array_}')

print(
    f'Разница между максимальным и минимальным значением дробной части элементов: {array_sum(array_)}')
