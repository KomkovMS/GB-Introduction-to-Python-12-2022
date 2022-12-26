# A. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.

# Пример:
# если k = 2,
# то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

# polynomial

# Пояснение к ДЗ
# 1 - функция генерирует многочлен по максимальной степени
# 2 - функция делает из словаря строку
# 3 - функция делает из строки словарь
# 4 - функция складывает два словарика

import random

# 1


def create_equation() -> dict:
    k = int(input('Введите максимальную степень: '))
    equation = {}
    for n in range(k, -1, -1):
        equation[n] = random.randint(-100, 100)

    return equation

# 2


def decode(equation: dict) -> str:
    new_equation = []
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' ' + ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+ -', '- ')\
        .replace('*x**0', '').replace(' 1*x', ' x')\
        .replace('-1*x', '-x').replace('x**1', 'x')

    return new_equation[1:]

# 3


def encode(equation: str) -> dict:
    equation = equation.replace(' + ', ' ').replace(' - ', ' -')\
        .replace(' -x', ' -1*x').replace(' x', ' 1*x')\
        .replace('*x ', '*x**1 ').split()[:-2]
    dict_equation = {}
    for item in equation:
        i = item.split('*x**')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        else:
            dict_equation[int(0)] = int(i[0])

    return dict_equation

# 4


def addition(first_eq: dict, second_eq: dict) -> dict:
    res_eq = {}
    res_eq.update(first_eq)
    res_eq.update(second_eq)
    for key in res_eq:
        res_eq[key] = first_eq.get(key, 0) + second_eq.get(key, 0)

    return res_eq


if __name__ == '__main__':
    equation1 = create_equation()
    equation2 = create_equation()
    str_eq1 = decode(equation1)
    str_eq2 = decode(equation2)
    print(str_eq1)
    data = open('polynomial_1.txt', 'w')
    data.writelines(str_eq1)
    print(str_eq2)
    data = open('polynomial_2.txt', 'w')
    data.writelines(str_eq2)
    dict_eq1 = encode(str_eq1)
    dict_eq2 = encode(str_eq2)
    dict_final = addition(dict_eq1, dict_eq2)
    str_final = decode(dict_final)
    print(str_final)
    data = open('str_final.txt', 'w')
    data.writelines(str_final)
