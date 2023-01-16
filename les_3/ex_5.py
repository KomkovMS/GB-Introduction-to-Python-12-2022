list_ = []
for i in range(1, 20):
    list_.append(i)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list_)

# тоже самое, что и:

li = [x for x in range(1, 20)]
print(li)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

li = map(lambda x: x + 10, li)
print(li)   # <map object at 0x00000280E287BF10>
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print(list(li))
