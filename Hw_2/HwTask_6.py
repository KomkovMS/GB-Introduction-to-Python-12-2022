# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.

# Пример:

# 6782 -> 23
# 0,56 -> 11

num = input('Enter a number: ')
res = 0
my_list = []

for i in range(len(num)):
    my_list.append(num[i])

for i in range(len(my_list)):
    if my_list[i] != '.':
        res += int(my_list[i])

print(f'{num} -> {res}')
