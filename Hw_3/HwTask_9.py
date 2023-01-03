# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI
from datetime import datetime

my_list = []  # [2, 3, 5, 9, 3]

for _ in range(10):
    my_list.append(RI(0, 10))

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


# решение на стриме дек 2022

# 1 вариант
list_ = [RI(1, 10) for i in range(10)]

summ = 0
new_list = []

start = datetime.timestamp(datetime.now())
for i in range(len(list_)):
    if i % 2 != 0:
        summ += list_[i]
        new_list.append(list_[i])

print(f'{list_} -> на нечётных позициях элементы {new_list}, их сумма: {summ}')
# для 10 млн - 1.503998041152954
print(datetime.timestamp(datetime.now()) - start)


# 2 вариант

my_list_ = [RI(1, 10) for i in range(10)]

summa = 0
new_list_ = []

start = datetime.timestamp(datetime.now())
for i in range(1, len(my_list_), 2):
    summa += my_list_[i]
    new_list_.append(my_list_[i])

print(f'{my_list_} -> на нечётных позициях элементы {new_list_}, их сумма: {summa}')
# для 10 млн - 0.6803410053253174
print(datetime.timestamp(datetime.now()) - start)
