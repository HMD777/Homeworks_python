print(' Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci_neg(n):
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a - b


num = int(input('Введите число: '))

fib_data = list(fibonacci(num))
fib_data_2 = list(fibonacci_neg(num))

print(f'Результат: {fib_data_2[::-1] + fib_data}')
