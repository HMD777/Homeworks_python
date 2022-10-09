import math
print('Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')


def find_distance(x_a, x_b, y_a, y_b):
    result = math.sqrt(((x_b-x_a)**2)+((y_b-y_a)**2))
    print(f'Расстояние между точками X и Y равен: {result}')


X_a = input('Введите координту точки A(x): ')
Y_a = input('Введите координту точки A(y): ')
X_b = input('Введите координту точки B(x): ')
Y_b = input('Введите координту точки B(y): ')

find_distance(float(X_a), float(X_b), float(Y_a), float(Y_b))
