# Задайте список из n чисел последовательности (1 + 1/n)**n,
# выведеите его на экран, а так же сумму элементов списка.

# Пример:

# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


num = int(input('Enter a number: '))
res = 0
my_list = []

for i in range(1, num + 1):
    my_list.append(float(round((1 + 1 / i) ** i, 2)))

for i in range(len(my_list)):
    res += my_list[i]

print(f'Для n = {num} -> {my_list}\nСумма {res}')


# разбор ДЗ-2 на семинаре 4 задача 2
number = int(input('Enter a number: '))

my_list = []

for n in range(1, number + 1):
    my_list.append(round((1 + 1 / n) ** n, 2))

print(f'При n = {number} список -> ', end='')
print(*my_list, sep=', ')
print(f'И его сумма -> {sum(my_list)}')

# другой вариант решения
number = int(input('Enter a number: '))

my_list = []

for n in range(1, number + 1):
    num = round((1 + 1 / n) ** n, 2)
    my_list.append(num if num != int(num) else int(num))

print(f'При n = {number} список -> ', end='')
print(*my_list, sep=', ')
print(f'И его сумма -> {sum(my_list)}')


# num if num != int(num) else int(num) тоже самое что,

# if num != int(num):
#     num = num
# else:
#     num = int(num)
