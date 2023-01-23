# 5. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# предыдущее решение (Hw_1/HwTask_5.py):

import math
# my_list = []
# size = 4
# msg = 'Введиите координаты: '
# name_axis = None
# result = None

# for i in range(size):
#     if i < size / 2:
#         name_axis = 'X'
#         coordinate = int(input(f'{msg} {name_axis}{i+1}: '))
#     else:
#         name_axis = 'Y'
#         coordinate = int(input(f'{msg} {name_axis}{i-1}: '))
#     my_list.append(coordinate)

# print(
#     f'Вы ввели координаты: A({my_list[0]}, {my_list[2]});' +
#     f' B({my_list[1]}, {my_list[3]})')

# result = (((my_list[1] - my_list[0]) * (my_list[1] - my_list[0])) +
#           ((my_list[3] - my_list[2])) * (my_list[3] - my_list[2])) ** 0.5

# print(f'-> {round(result, 2)}')


# текущее решение:

def get_coordinate():
    coordinate = input(
        'Введите координаты точек A(x y), B(x y) через пробел и запятую: ')\
        .split(',')
    new_coordinate = [tuple(map(float, item.split())) for item in coordinate]
    return new_coordinate


x, y = get_coordinate()

len = (y[0] - x[0])**2 + (y[1] - x[1])**2
print(f'{x=} и {y=} -> {round(math.sqrt(len), 2)}')
