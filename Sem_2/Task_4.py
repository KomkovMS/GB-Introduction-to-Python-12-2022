# 2. Напишите программу, которая будет принимать на вход дробь и показывать
# первую цифру дробной части числа.

# *Примеры:*

# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# мое решение:

# Вариант 1

import math

number = float(input('Enter a number: '))
result = 0

if number * 10 % 10 > 0:
    result = math.floor(number * 10 % 10)
elif result == 0:
    result = 'нет'
print(f'{number} -> {result}')

# вариант 2
number = float(input('Enter a number: '))
result = 0
if number * 10 % 10 > 0:
    result = int(number * 10 % 10)
elif result == 0:
    result = 'нет'
print(f'{number} -> {result}')

# Вариент 3
number = float(input('Enter a number: '))
result = 0
if number % 1 != 0:  # тоже самое что: number != int(number)
    result = int(number * 10 % 10)
else:
    result = 'нет'
print(f'{number} -> {result}')

# вариант 4 (решение другого ученика на семинаре)
number = float(input('Enter a number: '))
result = 0
if number - int(number) == 0:
    result = 'нет'
else:
    result = int((number - int(number)) * 10)

print(f'{number} -> {result}')

# вариант 5 (решение преподавателя)
num = input('Enter a number: ')
result = num.split('.')
if len(result) > 1:
    result = result[1][0]
else:
    result = 'no'

print(f'{num} -> {result}')
