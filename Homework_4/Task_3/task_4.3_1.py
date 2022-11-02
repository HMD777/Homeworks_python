import random
print('Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.')


def array_num_gen(min, max, array, arr_len):
    for i in range(arr_len):
        array.append(random.randint(min, max))


def array_sort(array):
    array_temp = []
    array_temp_1 = []
    i = 0
    while i < len(array):
        j = i+1
        while j < len(array):
            if array[i] == array[j]:
                array_temp.append(array[i])
            j += 1
        i += 1
    for i in array:
        if i not in array_temp:
            array_temp_1.append(i)

    print(array_temp_1)


array = []

min = int(input('Введите минимальное число для массива:'))
max = int(input('Введите максимальное число для массива:'))
arr_len = int(input('Введите длинну массива массива:'))

array_num_gen(min, max, array, arr_len)
print(array)
array_sort(array)
