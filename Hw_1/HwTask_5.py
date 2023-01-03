# 5. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math
my_list = []
size = 4
msg = 'Введиите координаты: '
name_axis = None
result = None

for i in range(size):
    if i < size / 2:
        name_axis = 'X'
        coordinate = int(input(f'{msg} {name_axis}{i+1}: '))
    else:
        name_axis = 'Y'
        coordinate = int(input(f'{msg} {name_axis}{i-1}: '))
    my_list.append(coordinate)

print(
    f'Вы ввели координаты: A({my_list[0]}, {my_list[2]});' +
    f' B({my_list[1]}, {my_list[3]})')

result = (((my_list[1] - my_list[0]) * (my_list[1] - my_list[0])) +
          ((my_list[3] - my_list[2])) * (my_list[3] - my_list[2])) ** 0.5

print(f'-> {round(result, 2)}')


# разбор решения на семинаре от преподавателя

first = input('Введите координаты точки А через пробел').split()
second = input('Введите координаты точки B через пробел').split()

distance = (float(first[0]) - float(second[0])) ** 2 + \
    (float(first[1])) - float(second[1]) ** 2

print(f'расстояние между точками равно {(round(math.sqrt(distance)), 2)}')


# решение на стриме дек 2022
def input_coords():
    try:
        coords = input(
            'Введите координаты точек A(x y), B(x y) через пробел и запятую: ')
        coords = coords.split(',')
        new_coords = []
        for item in coords:
            new_coords.append(tuple(map(float, item.split())))
        return new_coords
    except:
        print('Введите по шаблону A(x y), B(x y)')


a, b = input_coords()
# print(a)
# print(b)

distance = (b[0] - a[0])**2 + (b[1] - a[1])**2
print(
    f'Расстояние между точками {a=} и {b=} будет {round(math.sqrt(distance), 2)}')
