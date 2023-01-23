'''
Задайте список из n чисел последовательности (1 + 1/n)**n,
выведеите его на экран, а так же сумму элементов списка.

Пример:

Для n=4 -> [2, 2.25, 2.37, 2.44]
Сумма 9.06

'''

# предыдущее решение (Hw_2/HwTask_7.py):

# num = int(input('Enter a number: '))
# res = 0
# my_list = []

# for i in range(1, num + 1):
#     my_list.append(float(round((1 + 1 / i) ** i, 2)))

# for i in range(len(my_list)):
#     res += my_list[i]

# print(f'Для n = {num} -> {my_list}\nСумма {res}')

# текущее решение:

num = int(input('Enter a number: '))
my_list = [float(round((1 + 1 / x) ** x, 2)) for x in range(1, num + 1)]
res = 0
for i in range(len(my_list)):
    res += my_list[i]

print(f'Для n = {num} -> {my_list}\nСумма {res}')
