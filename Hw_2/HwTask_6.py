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

number = input('Введите вещественное число: ')
summa = 0
for char in number:
    if char.isdigit():
        summa += int(char)

print(summa)


# решение на стриме дек 2022

# 1 вариант

number = input('Введите вещественное число: ')
# print(number)
# print(type(number))
number = number.split('.')
print(number)
# print(type(number))

summa = 0

for element in number:
    for dig in element:
        summa += int(dig)
print(summa)

# 2 вариант
num = input('Введите вещественное число: ')
num = num.replace('.', '').replace('-', '').replace(',', '')
print(num)

summ = 0

for element in num:
    summ += int(element)
print(summ)

# 3 вариант (оптимальный)
num = input('Введите вещественное число: ')

sum = 0

for element in num:
    if element.isdigit():
        sum += int(element)
print(sum)
