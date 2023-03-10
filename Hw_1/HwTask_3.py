# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

# Пример:

# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

my_list = []
size = 2
for i in range(size):
    coordinate = int(input(f'Enter coordinate № {i+1} : '))
    my_list.append(coordinate)

x = my_list[0]
y = my_list[1]

if x > 0 and y > 0:
    print(f'При условии x = {x}, y = {y} точка находится в I четверти')
elif x > 0 and y < 0:
    print(f'При условии x = {x}, y = {y} точка находится в IV четверти')
elif x < 0 and y > 0:
    print(f'При условии x = {x}, y = {y} точка находится во II четверти')
else:
    print(f'При условии x = {x}, y = {y} точка находится во III четверти')


# разбор решения на семинаре от преподавателя

x, y = input('Введите координаты через пробел: ').split(' ')

x, y = int(x), int(y)
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')

# решение на стриме дек 2022


def input_float():
    while True:
        try:
            coords = input('Введите координаты через пробел: ')
            coords = list(map(float, coords.split()))
            if len(coords) == 2:
                return coords
            else:
                print('Введите только две координаты')
        except:
            print('ОШИБКА! Введите веществнное число')


x, y = input_float()

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Одна из точек лежит на оси')
