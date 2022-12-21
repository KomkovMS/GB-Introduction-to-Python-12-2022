# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов,
# отличной от 0.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


#  решение другим способом


def f_get_list_result(my_list: list) -> list:
    for item in my_list:
        item = str(round(item - int(item), 2))
        for i in range(len(item)):
            if item[i] == '.':
                list_result.append(float(item[i-1:]))
    return list_result


def f_result(list_result: list) -> float:
    max_item = list_result[0]
    min_item = list_result[0]
    for item in list_result:
        if item > max_item:
            max_item = item
        if item < min_item:
            min_item = item
        result = max_item - min_item
    return result


my_list = [1.1, 1.2, 3.1, 5, 10.01]

list_result = []
list_result = f_get_list_result(my_list)

result = 0
result = f_result(list_result)

print(f'{my_list} => {result}')
