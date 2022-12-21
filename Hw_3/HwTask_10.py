# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


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
print(mult_numbers(my_list))
