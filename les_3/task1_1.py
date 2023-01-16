'''
В файле хранятся числа, нужно выбрать четные и составить список пар 
(число; квадрат числа)

Пример:
1 2 3 5 8 15 23 38
Получить:
[(2,4), (8,64), (38, 1444)]
'''

path = 'C:/Python/Python_12.2022/les_3/file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers .append(int(data[:space_pos]))
    data = data[space_pos + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)
