data = [x for x in range(10)]

res = filter(lambda x: x % 2 == 0, data)
# тоже самое, что и:
res = filter(lambda x: not x % 2, data)
print(res)  # <filter object at 0x000001E52DCBB970>
print(list(res))        # [0, 2, 4, 6, 8]
