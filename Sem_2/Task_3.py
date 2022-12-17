# 1. Напишите программу, которая будет на вход принимать число N и выводить
# числа от -N до N

# *Примеры:*

# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# мое решение:

# Вариант 1
n = int(input('Enter a number: '))

m = -n

while n >= m:
    print(m)
    m += 1

# Вариант 2

for i in range(-n, n+1):
    print(i)

# Вариант 3 (на семинаре от преподавателя)

my_list = []

for i in range(-n, n+1):
    my_list.append(i)

print(*my_list, sep=', ')
