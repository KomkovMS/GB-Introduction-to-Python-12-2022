# Вывести четные числа от 0 до n

idx = 2
num = int(input('Введите число: '))

while idx <= num:
    print(idx, end=', ')
    idx += 2

print('\n' + '>>>>>>>' * 20)
# или

i = 0
number = int(input('Введите число: '))

while i <= number:
    if i % 2 == 0 and i != 0:
        print(i, end=', ')
    i += 1
