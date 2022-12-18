# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int

import random

my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)

shaker_list = []

for i in range(len(my_list)):
    i = random.randrange(len(my_list))
    shaker_list.append(my_list.pop(i))
print(shaker_list)
