# 'A * x ** 2 + B * x + C = 0'
# '32 * x ** 2 + 4 * x - 6 = 0'
# (32, 4, -6)

# решение на семинаре - не доработано

from math import sqrt

my_str = 'A*x**2 + B*x + C = 0'


def conv(my_str):
    new_str = my_str.split('x')
    print(new_str)
    new_str2 = []
    for i in range(len(new_str)):
        new_str2.append(new_str[i].replace('**2', '').replace('*', '').replace(
            ' ', '').replace('+', '').replace('0', '').replace('=', ''))
    return new_str2


def roots_equ(a, b, c):
    d = b ** 2 - 4 * a * c
    x_1 = (-b + sqrt(d)) / a * 2
    x_2 = (-b - sqrt(d)) / a * 2
    return d, x_1, x_2


equation = '-3*x**2 + 78*x - 9 = 0'
str_new = conv(equation)
for i in range(len(str_new)):
    str_new[i] = int(str_new[i])
print(str_new)


print(roots_equ(str_new[0], my_str[1], my_str[2]))
