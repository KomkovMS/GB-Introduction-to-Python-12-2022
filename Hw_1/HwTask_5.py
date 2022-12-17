# 5. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

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
