import random
print(
    'Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.')


def lst_gen(num, lst):
    for i in range(num):
        res = random.randint(-num, num)
        lst.append(res)


def copy_to_file(file_name, lst):
    file = open(file_name, 'w')
    for i in lst:
        file.write(str(i)+'\n')
    file.close()


def sum_from_file(file_name):
    file = open(file_name, 'r')
    data = file.read()
    lst = data.split()
    result = 0
    for i in lst:
        result = result + int(i)
    file.close()
    return result


lst_1 = []
args_ = int(input('Введите число N: '))
lst_gen(args_, lst_1)
print(f'Сгенерированный список для копирования в новый файл:\n{lst_1}')

file_name = 'task_4.txt'
copy_to_file(file_name, lst_1)

print(
    f'Результат суммирования чисел с файла равен:\n{sum_from_file(file_name)}')
