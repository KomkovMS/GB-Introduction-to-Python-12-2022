# list Comprehension
list_ = []

for i in range(1, 101):
    # if (i % 2 == 0):
    list_.append(i)

# print(list_)

# тоже самое, что и:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_list = [i for i in range(1, 21) if i % 2 == 0]
print(my_list)

# [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]
my_list1 = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(my_list1)


def f(x):
    return x ** 3


# [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]
my_list2 = [f(i) for i in range(1, 21) if i % 2 == 0]
print(my_list2)

# [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]
my_list3 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(my_list3)
