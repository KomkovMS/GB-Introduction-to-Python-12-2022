# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list = []  # [2, 3, 5, 9, 3]

for _ in range(10):
    my_list.append(random.randint(0, 10))

print(my_list)

# вариант 1


def Sum_odd(my_list: list):
    sum_Odd_Position = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            sum_Odd_Position += my_list[i]
    print(sum_Odd_Position)


Sum_odd(my_list)

# вариант 2


def Sum_odd_2(my_list: list):
    sum_Odd_Position = 0
    for i in range(1, len(my_list), 2):
        sum_Odd_Position += my_list[i]
    print(sum_Odd_Position)


Sum_odd_2(my_list)
