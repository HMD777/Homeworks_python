import random

print('Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.')


def solver(k):
    result = ""
    while k > 0:
        if k > 1:
            z = random.randint(0, 100)
            if z == 0 or z == 1:
                result = result + 'X**' + str(k) + ' + '
            else:
                result = result + str(z) + '*X**' + str(k) + ' + '
            k -= 1
        elif k == 1:
            z = random.randint(0, 100)
            y = random.randint(0, 100)
            if z == 0:
                if y > 0:
                    result = result + 'X' + ' + ' + str(y)
                else:
                    result = result + 'X'
            else:
                if y > 0:
                    result = result + str(z) + '*X' + ' + ' + str(y)
                else:
                    result = result + str(z) + '*X'
            k -= 1
    return result


def copy_to_file(file_name, res):
    file = open(file_name, 'w')
    file.write(res)
    file.close()


def sum_from_file(file_name_1, file_name_2):
    file_1 = open(file_name_1, 'r')
    file_2 = open(file_name_2, 'r')
    data_1 = file_1.read()
    data_2 = file_2.read()
    lst_1 = data_1.split(' + ')+data_2.split(' + ')
    lst_1_1 = []
    lst_1_2 = []

    for i in lst_1:
        a = i.count('*')
        b = i.count('X')
        if a > 2:
            lst_1_1.append(i.split('*X**'))
        elif a == 2:
            x = i.split('X**')
            x[0] = "1"
            lst_1_1.append(x)
        elif a == 1:
            x = i.split('*X')
            x[-1] = "1"
            lst_1_1.append(x)
        elif a == 0 and b == 1:
            x = i.split('X')
            x[0] = "1"
            x[-1] = "1"
            lst_1_1.append(x)
        elif a == 0 and b == 0:
            z = i + "x" + "0"
            x = z.split('x')
            lst_1_1.append(x)

    i = 0
    j = len(lst_1_1)
    while i < j:
        k = i+1
        while k < j:
            if int(lst_1_1[k][1]) > 1:
                if lst_1_1[i][1] == lst_1_1[k][1]:
                    x = int(str(lst_1_1[i][0]))+int(str(lst_1_1[k][0]))
                    y = str(x) + '*X**' + str(lst_1_1[k][1])
                    lst_1_2.append(y)

            if int(lst_1_1[k][1]) == 1:
                if lst_1_1[i][1] == lst_1_1[k][1]:
                    x = int(str(lst_1_1[i][0]))+int(str(lst_1_1[k][0]))
                    y = str(x) + '*X'
                    lst_1_2.append(y)
            if int(lst_1_1[k][1]) == 0:
                if lst_1_1[i][1] == lst_1_1[k][1]:
                    x = int(str(lst_1_1[i][0]))+int(str(lst_1_1[k][0]))
                    y = str(x)
                    lst_1_2.append(y)
            k += 1
        i += 1

    result = " + ".join(lst_1_2)
    file_1.close()
    file_2.close()
    return result


k = int(input('Введите степень k: '))
result_1 = solver(k)
result_2 = solver(k)
print(result_1)
print(result_2)
file_name_1 = 'task_4.5_1.txt'
file_name_2 = 'task_4.5_2.txt'
file_name_3 = 'task_4.5_3.txt'

copy_to_file(file_name_1, result_1)
copy_to_file(file_name_2, result_2)

result_3 = sum_from_file(file_name_1, file_name_2)
print(result_3)
copy_to_file(file_name_3, result_3)

