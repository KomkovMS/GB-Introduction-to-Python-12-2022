# Найдите корни квадратного уравнения Ax² + Bx + C = 0, создав функцию для их
# нахождения.
# В качестве коэффициентов A, B и C для проверки работы функции передайте
# не менее трёх наборов данных, в одном из них коэффициент A = 0.

import math

equation = '32 * x ** 2 + 4 * x - 6 = 0'


def create_koef(equation: str) -> tuple:
    new_koef = []
    nq = equation.replace(' ', '').replace('=0', ''). \
        replace('+', ' ').replace('-', ' -').split()
    print(nq)
    for item in nq:
        if item.startswith('x'):
            new_koef.append(1)
        elif item.startswith('-x'):
            new_koef.append(-1)
        else:
            new_koef.append(int(item.split('*x')[0]))
    return new_koef


create_koef(equation)


def solution(koef: list):
    a, b, c = koef
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)

        return x1, x2
    elif disc == 0:
        x = -b / (2 * a)

        return x
    else:

        return None


print(solution(create_koef(equation)))
