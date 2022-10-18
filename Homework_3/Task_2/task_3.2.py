import random

print('Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')


def array_gen(array, array_len, min, max):
    for i in range(array_len):
        array.append(random.randint(min, max))


def array_sum(array, array_res):
    count = len(array)-1
    for i in range(len(array)):
        if i <= count:
            array_res.append(array[i] * array[count])
            count -= 1


array_ = []
array_res = []
array_len = int(input('\nВведите длинну массива: '))
min_ = int(input('Введите минимальное число массива: '))
max_ = int(input('Введите максимальное число массива: '))
array_gen(array_, array_len, min_, max_)
array_sum(array_, array_res)
print(f'Сгенерирован массив: {array_}')
print(f'Произведение пар чисел из списка равен: {array_res}')
