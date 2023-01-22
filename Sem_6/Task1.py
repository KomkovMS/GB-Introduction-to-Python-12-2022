'''
Дана последовательность чисел. Получить список уникальных элементов заданной
последовательности.

*Пример:*

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

'''

# мое решение: (.pop(), .get(), .keys())

import random
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
my_dict = {}

for item in my_list:
    my_dict[item] = my_dict.get(item, 0) + 1
    if my_dict[item] >= 2:
        my_dict.pop(item)

new_list = list(my_dict.keys())
print(f'{my_list} -> {new_list}')


# решение одногрупников # 1:

list_ = [1, 2, 3, 5, 1, 5, 3, 10]
dict_ = {}
new_list_ = []

for i in range(len(list_)):
    dict_[list_[i]] = dict_.get(list_[i], 0) + 1
print(dict_)

for key, item in my_dict.items():
    if item == 1:
        new_list_.append(key)
print(new_list_)


# решение одногрупников # 2 (??? у меня не получается правильный вывод):

# list_1 = [13, 0, 3, 1, 2, 3, 5, 1, 5, 3, 10]
# print(list_1)
# list_2 = []

# for x in range(len(list_1)):
#     f = True
#     for y in range(len(list_2)):
#         if list_1[x] == list_2[y] and x != y:
#             f = False
#             break
#     if f == True:
#         list_2.append(list_1[x])
# print(list_2)


# решение одногрупников # 3 через .count()

my_list_3 = [1, 2, 3, 5, 1, 5, 3, 10]
new_list_4 = []
print(my_list_3)
for el in my_list_3:
    if my_list_3.count(el) == 1:
        new_list_4.append(el)
print(new_list_4)


# решение преподавателя на семинаре

my_list_5 = [random.randint(0, 10) for _ in range(15)]
print(my_list_5)

my_list_6 = [x for x in my_list_5 if my_list_5.count(x) == 1]
print(my_list_6)


# Как работает .count(x):

some_list = [random.randint(0, 10) for _ in range(15)]
print(some_list)

for element in some_list:
    print(f'{element} встречается >>> {some_list.count(element)} раз')
