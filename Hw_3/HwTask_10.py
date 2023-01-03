# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
from random import randint as RI


def mult_numbers(my_list: list) -> list:
    my_list_result = []
    size = len(my_list)
    if size % 2 == 0:
        size = int(len(my_list)/2)
    else:
        size = int(len(my_list)/2 + 1)

    for i in range(size):
        my_list_result.append(my_list[i] * my_list[- 1 - i])

    return my_list_result


my_list = [2, 3, 4, 5, 6]
print(f'{my_list} -> {mult_numbers(my_list)}')


# решение на стриме дек 2022

list_ = [RI(1, 10) for i in range(9)]
print(list_)

new_list = []

for i in range(len(list_)//2):
    new_list.append(list_[i] * list_[- i - 1])

if len(list_) % 2 != 0:
    new_list.append(list_[len(list_) // 2] ** 2)

print(new_list)
