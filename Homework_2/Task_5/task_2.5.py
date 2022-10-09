import random
print('Реализуйте алгоритм перемешивания списка')


def lst_gen(num, lst):
    for i in range(num):
        res = random.randint(-num, num)
        lst.append(res)


def lst_shuffle(lst_1):
    for i in range(len(lst_1)):
        rand = random.randint(0, len(lst_1)-1)
        temp = lst_1[rand]
        lst_1[rand] = lst_1[i]
        lst_1[i] = temp


lst_1 = []
args_ = int(input('Введите число N: '))
lst_gen(args_, lst_1)
print(f'Сгенерированный список:\n{lst_1}')
lst_shuffle(lst_1)
print(f'Перемешанный список:\n{lst_1}')
