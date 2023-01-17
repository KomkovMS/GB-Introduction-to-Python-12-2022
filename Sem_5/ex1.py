from random import randint as RI

# List Comprehension - удобно создавать списки

# раньше
my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Comprehension

my_list = [x for x in range(10)]
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Пример вывода рандомного списка
my_list = [RI(0, 10) for x in range(10)]
print(my_list)  # [4, 4, 2, 8, 4, 8, 0, 1, 6, 5]

# Пример вывода рандомного списка c функцией


def pow(x):
    return x ** 2


my_list = [pow(x) for x in range(10)]
print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# при этом тоже самое будет если
my_list = [x ** 2 for x in range(10)]
print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# можно сгенерировать словарики
my_list = {x: x ** 2 for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(my_list)

# Функция map()

list_ = [x for x in range(10)]
print(list_)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# переведем в строки

# раньше
list_ = [x for x in range(10)]
for i in range(len(list_)):
    list_[i] = str(list_[i])
print(list_)    # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# сейчас при помощи функции map()
list_ = list(map(str, [x for x in range(10)]))
print(list_)    # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# пример со строкой

# введите с клавиатуры какие то данные через пробел и сделать их числами
my_str = '123 46 7823 312 153 232'
print(my_str.split())   # ['123', '46', '7823', '312', '153', '232']
my_str = list(map(int, my_str.split()))
print(my_str)   # [123, 46, 7823, 312, 153, 232]


# функция filter()

# например, запишем в новый список все значения, где есть цифра 4

str_ = '123 46 7823 312 4153 232 543 234'
str_ = list(filter(lambda x: '4' in x, str_.split()))
print(str_)     # ['46', '4153', '543', '234']

# или наоборот, где нет 4
str_1 = '123 46 7823 312 4153 232 543 234'
str_1 = list(filter(lambda x: not '4' in x, str_1.split()))
print(str_1)    # ['123', '7823', '312', '232']

# проверка на четность
str_2 = '123 46 7823 312 4153 232 543 234'
str_2 = list(filter(lambda x: x % 2 == 0, list(map(int, str_2.split()))))
print(str_2)    # [46, 312, 232, 234]

# пример без lambda


def comparsion(x):
    return x > 0


my_list_number = [x for x in range(-10, 10)]
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list_number)
print(list(filter(comparsion, my_list_number)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# enumerate()
str_3 = '123 46 7823 312 4153 232 543 234'
print(str_3)    # 123 46 7823 312 4153 232 543 234
my_list_3 = str_3.split()
print(my_list_3)    # ['123', '46', '7823', '312', '4153', '232', '543', '234']

# получаем значения (аргументы)
for i in my_list_3:
    print(i)
    # 123
    # 46
    # 7823
    # 312
    # 4153
    # 232
    # 543
    # 234

# получаем индексы
for i in range(len(my_list_3)):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7

# чтобы обратить и к индексам и к элементам:
for i, item in enumerate(my_list_3):
    print(i, item)
    # 0 123
    # 1 46
    # 2 7823
    # 3 312
    # 4 4153
    # 5 232
    # 6 543
    # 7 234

# если нужна нумерация не с нуля:
for i, item in enumerate(my_list_3, 5):
    print(i, item)
    # 5 123
    # 6 46
    # 7 7823
    # 8 312
    # 9 4153
    # 10 232
    # 11 543
    # 12 234

# zip()
my_list_4 = '23 5432 67 78 96 234 54 7654'.split()
my_list_5 = [x for x in range(1, 9)]
# [('23', 1), ('5432', 2), ('67', 3), ('78', 4), ('96', 5), ('234', 6), ('54', 7), ('7654', 8)]
print(list(zip(my_list_4, my_list_5)))

# lambda - односрочная функция


def power(x):
    return x ** 2


def f(x): return x ** 2


print(f(5))  # 25


def print_smile(name):
    print(f'{name}, Улыбнись!')  # Stone, Улыбнись!


def on_ckick(): return print_smile('Stone')


on_ckick()
