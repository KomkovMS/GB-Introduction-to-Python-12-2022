# 2. Напишите программу, которая на вход принимает 5 чисел и находит
# максимальное из них.

# Примеры:

# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# вариант 1

num_1 = int(input("Number 1: "))
num_2 = int(input("Number 2: "))
num_3 = int(input("Number 3: "))
num_4 = int(input("Number 4: "))
num_5 = int(input("Number 5: "))

arr = [num_1, num_2, num_3, num_4, num_5]
max = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]

print(f'{num_1}, {num_2}, {num_3}, {num_4} и {num_5} -> {max}')

# вариант 2

for i in arr:
    if i > max:
        max = i
print(f'{num_1}, {num_2}, {num_3}, {num_4} и {num_5} -> {max}')

# вариант 3

max = 0
list = []
for i in range(5):
    num = int(input(f'Введите число: {i + 1}: '))
    list.append(num)
    if num > max:
        max = num
print(f'{list} -> {max}')

# вариант 4

my_list = []

for i in range(5):
    numb = int(input(f'Enter {i+1} number: '))
    my_list.append(numb)

maxim = 0

for item in my_list:
    if item > maxim:
        maxim = item

print(f'Maximum = {maxim}')
