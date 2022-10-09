print('Напишите программу для проверки истинности утверждения ¬(X V Y V Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')
list_X = [0, 0, 0, 0, 1, 1, 1, 1]
list_Y = [0, 0, 1, 1, 0, 0, 1, 1]
list_Z = [0, 1, 0, 1, 0, 1, 0, 1]

result_1 = []
result_2 = []


def disjunction(data_1, data_2, data_3, result):
    stop = len(data_1)
    start = 0
    while stop > start:
        if (data_1[start] + data_2[start] + data_3[start]) == 0:
            result.append(0)
        else:
            result.append(1)
        start = start+1


def conjunction_func(data_1, data_2, data_3, result):
    stop = len(data_1)
    start = 0
    while stop > start:
        if (data_1[start] + data_2[start] + data_3[start]) == 3:
            result.append(1)
        else:
            result.append(0)
        start = start+1


def reverse_func(data):
    stop = len(data)
    start = 0
    while stop > start:
        if data[start] == 0:
            data[start] = 1
        else:
            data[start] = 0
        start = start+1


def function_check(data_1, data_2):
    if data_1 == data_2:
        print('\nВыражение данных двух предикат является истинным!')
    else:
        print('\nВыражение данных двух предикат является ложным!')


print('Выржание левой стороны')
print(f'X = {list_X}')
print(f'Y = {list_Y}')
print(f'Z = {list_Z}')

disjunction(list_X, list_Y, list_Z, result_1)

print(f'\nРезультат дизьюнкции левой стороны:\nL = {result_1}')
reverse_func(result_1)
print(f'\nРезультат отрицания дизьюнкции левой стороны:\nL = {result_1}')

reverse_func(list_X)
reverse_func(list_Y)
reverse_func(list_Z)
print('\nРезультат отрицания выржания в правой стороне')
print(f'X = {list_X}')
print(f'Y = {list_Y}')
print(f'Z = {list_Z}')

conjunction_func(list_X, list_Y, list_Z, result_2)
print(f'\nРезультат коньюнкции правой стороны:\nR = {result_2}')

function_check(result_1, result_2)
