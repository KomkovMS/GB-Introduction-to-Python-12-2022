# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиций может быть более двух, пользователь вводит индексы с клавиатуры.

import random


def get_my_list(num: int) -> list:
    list_ = []
    for i in range(-num, num + 1):
        list_.append(random.randint(-num, num))

    return list_


def input_int(count: str) -> list:
    count = list(map(int, count.split()))

    return count


def work_item(my_list: list, idx_list: list) -> int:
    result = 1
    for i in range(-len(my_list), len(my_list)):
        if i in idx_list:
            result *= my_list[i]

    return result


num = int(input('Введите целое число N (из него сформируем список от -N до N): '))
count = input('Введите индексы через пробел: ')

my_list = get_my_list(num)
index_list = input_int(count)
res = work_item(my_list, index_list)

print(num)
print(my_list)
print(index_list)
print(res)
