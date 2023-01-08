"""
Написать программу, которая состоит из 4-х этапов:
- создает список из рандомных четырех значных чисел;
- принимает с консоли цифру и удаляет ее из всех элементов списка;
- цифры каждого элемента суммирует пока результат не станет однозначным числом
- из финального списка убирает все дублирующие элементы;

после каждого этапа выводить результаты в консоль

Пример:
- 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
- 2 этап: Введите цифру: 3
- 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
- 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
- 3 этап: [3, 1, 5, 5, 3, 5, 4]
- 4 этап: [3, 1, 5, 4]

"""

from random import randint as RI

# мое решение:


def get_random_number_list() -> list:
    my_list = [RI(1000, 10000) for _ in range(10)]
    print(my_list)
    # можно было так в 1 строку: list_ = list(map(str, list_))
    # или сразу my_list = [str(RI(1000, 10000)) for _ in range(10)]
    for i in range(len(my_list)):
        my_list[i] = str(my_list[i])
    return my_list


def get_change_list(list_: list, number: str) -> list:
    for i in range(len(list_)):
        for item in list_[i]:
            if item == number:
                list_[i] = list_[i].replace(item, '')
                break

        list_[i] = int(list_[i])
    return list_


def get_sum_num(change_list: list) -> list:
    size = len(change_list)
    summa = 0
    for i in range(size):
        change_list[i] = list(''.join(str(change_list[i])))
        for j in range(len(change_list[i])):
            change_list[i][j] = int(change_list[i][j])
            summa += change_list[i][j]
        change_list[i] = summa
        summa = 0

    return change_list


# 1 этап
my_list = get_random_number_list()

# 2 этап
num_input = input('Введите целое число от 0 до 9: ')
change_list = get_change_list(my_list, num_input)
print(change_list)

# 3 этап
sum_num = get_sum_num(change_list)

for item in sum_num:
    while item > 10:
        sum_num = get_sum_num(sum_num)
        item -= 1
print(sum_num)

# 4 этап
sum_num = list(set(sum_num))
print(sum_num)
