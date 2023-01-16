'''
Функция map() принимает указанную функцию к каждому элементу итерируемого
объекта и возвращает итератор с новыми объектами.
'''


def f(x):
    return x + 10


res = map(f, [1, 2, 3, 4, 5])

print(list(res))    # [11, 12, 13, 14, 15]


# тоже самое, что и:

print(list(map(lambda x: x + 10, [1, 2, 3, 4, 5])))  # [11, 12, 13, 14, 15]