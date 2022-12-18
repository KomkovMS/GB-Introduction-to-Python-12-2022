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
