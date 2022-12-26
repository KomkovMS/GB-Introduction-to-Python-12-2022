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


# Разбор ДЗ на семинаре 4

number = '0.94'
summa = 0
for char in number:
    if char != '.' and char != ',' and char != '-':
        summa += int(char)

print(summa)

# оптимальное решение

number = '0.94'
summa = 0
for char in number:
    if char.isdigit():
        summa += int(char)

print(summa)
