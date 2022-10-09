print('Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')


def num_sum_product(arg, result):
    result_1 = 1
    for i in range(2, arg+2):
        for j in range(1, i):
            result_1 = result_1 * j
        result.append(result_1)
        result_1 = 1


result_ = []
args_ = int(input('Введите число: '))
num_sum_product(args_, result_)
print(result_)
