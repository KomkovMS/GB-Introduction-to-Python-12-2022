# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int

import random

my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)

shaker_list = []

for i in range(len(my_list)):
    i = random.randrange(len(my_list))
    shaker_list.append(my_list.pop(i))
print(shaker_list)


# разбор ДЗ-2 на семинаре 4 задача 3

def create_list():
    new_list = []
    for i in range(10):
        new_list.append(i)

    return new_list


my_list = create_list()


def my_shuffle(my_list: list):
    ni = random.randint(0, len(my_list) - 1)
    for i in range(len(my_list)):
        my_list[i], my_list[ni] = my_list[ni], my_list[i]


print(my_list)
my_shuffle(my_list)
print(my_list)

# другой вариант


def create_list():
    new_list = []
    for i in range(10):
        new_list.append(i)

    return new_list


my_list = create_list()


def my_shuffle(my_list: list):
    new_list = []
    while len(my_list) > 0:
        ni = random.randint(0, len(my_list) - 1)
        new_list.append(my_list.pop(ni))

    return new_list


print(my_list)
print(my_shuffle(my_list))
