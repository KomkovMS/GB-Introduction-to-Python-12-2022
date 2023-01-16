'''
С клавиатуры вводится некоторый набор чисел. 
'''

# ex-1
data = list(map(int, (input().split())))  # 1 2 3 4 5
print(data)   # [1, 2, 3, 4, 5]

# ex-2
data1 = map(int, (input().split()))  # 1 2 3 4 5

for e in data1:
    print(e)
    # 1
    # 2
    # 3
    # 4
    # 5


print('*' * 20 + '\n')
# тоже самое, что и:
# ex-3
data2 = map(int, '1 2 3 4 5'.split())
for x in data2:
    print(x)
    # 1
    # 2
    # 3
    # 4
    # 5

print('*' * 20 + '\n')

# ex-4
data3 = list(map(int, '1 2 3 4 5'.split()))
for y in data3:
    print(y)
    # 1
    # 2
    # 3
    # 4
    # 5
