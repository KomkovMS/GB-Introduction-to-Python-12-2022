# 4. Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.

# *Пример:*

# Для N = 5: 1, -3, 9, -27, 81

# мое решение:
num = int(input('Enter a number: '))
res = 1
list = [1]
i = 1

while i < num:
    res *= -3
    list.append(res)
    i += 1
print(f'Для N = {num} -> ')
print(* list, sep=", ")

# мой вариант в варианте преподавателя (оптимально)
num = int(input('Enter a number: '))
my_list = []
x = 1

for i in range(1, num + 1):
    my_list.append(x)
    x *= -3
print(*my_list, sep=', ')

# другое решение на семинаре (оптимально)

my_list = []
number = int(input('Enter a number: '))
for i in range(0, number):
    my_list.append((-3) ** i)
print(* list, sep=", ")

# другое решение на семинаре

num = int(input('Enter a number: '))
res = 1

print(f'Для N = {num} -> ')
for i in range(num):
    print(res, end=' ')
    res *= -3

# другое решение на семинаре
print('\n')
num = int(input('Enter a number: '))
print(f'Для N = {num} -> ')
for i in range(0, num):
    res = (-3) ** i
    print(res, end=' ')
