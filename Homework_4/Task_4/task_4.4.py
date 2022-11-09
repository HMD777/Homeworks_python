import random

print('Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.')


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


def copy_to_file(file_name, res):
    file = open(file_name, 'w')
    file.write(res)
    file.close()


k = int(input('Введите степень k: '))
result = solver(k)
print(result)
file_name = 'task_4.4.txt'
copy_to_file(file_name, result)
