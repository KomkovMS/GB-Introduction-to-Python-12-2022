# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов,
# отличной от 0.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

# входные данные для генерации случайных вещественных чисел
my_list = []
size_items = 10
zeros_after_min = 0
zeros_after_max = 3
size_min_list = 0
size_max_list = 10

# генерируем и возвращаем список случайных вещественных чисел


def list_random_material_numbers(my_list: list,
                                 size_items: int,
                                 zeros_after_min: int,
                                 zeros_after_max: int,
                                 size_min_list: int,
                                 size_max_list: int
                                 ) -> list:
    for _ in range(size_items):
        amount = random.randint(zeros_after_min, zeros_after_max)
        number = round(random.uniform(size_min_list, size_max_list), amount)
        if number == int(number):
            my_list.append(int(number))
        else:
            my_list.append(number)

    return my_list


my_list = list_random_material_numbers(my_list,
                                       size_items,
                                       zeros_after_min,
                                       zeros_after_max,
                                       size_min_list,
                                       size_max_list)

list_result = []

# перебираем список и забираем дробную часть, возвращаем список целых чисел,
# которые не равны нулю


def get_list_result(my_list: list) -> list:
    for item in my_list:
        item -= int(item)
        if item != 0:
            list_result.append(round(item, 3)*1000)
    return list_result


list_result = get_list_result(my_list)

result = 0

# находим максимум и минимум, возвращаем результата вычитания


def get_Difference_InNumbers(list_result: list) -> float:
    max_item = list_result[0]
    min_item = list_result[0]

    for item in list_result:
        if item > max_item:
            max_item = item
        if item < min_item:
            min_item = item

    print(f'max = {max_item/1000}, min = {min_item/1000}')
    result = (max_item - min_item)/1000
    return result


print(f'{my_list} => {get_Difference_InNumbers(list_result)}')
