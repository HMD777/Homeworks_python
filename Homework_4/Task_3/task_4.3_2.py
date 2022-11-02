import random
print('Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.')


def array_num_gen(min, max, array, arr_len):
    for i in range(arr_len):
        array.append(random.randint(min, max))


def array_sort(array):
    array_temp = []
    i = 0
    while i < len(array):
        temp = 0
        j = i+1
        while j < len (array):
            if array [i] == array [j]:
                temp +=1
            j+=1
        if temp == 0:
            array_temp.append(array[i])
        i+=1
    print(array_temp)


array = []

min = int(input('Введите минимальное число для массива:'))
max = int(input('Введите максимальное число для массива:'))
arr_len = int(input('Введите длинну массива массива:'))

array_num_gen(min, max, array, arr_len)
print(array)
array_sort(array)
