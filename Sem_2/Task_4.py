# 2. Напишите программу, которая будет принимать на вход дробь и показывать
# первую цифру дробной части числа.

# *Примеры:*

# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# мое решение:

import math

number = float(input('Enter a number: '))
result = 0

if number * 10 % 10 > 0:
    result = math.floor(number * 10 % 10)
elif result == 0:
    result = 'нет'
print(f'{number} -> {result}')
