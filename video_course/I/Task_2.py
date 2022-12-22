# Вывести числа от 0 до n, n - вводить пользователь

index = 0
n = int(input('Введите число: '))

while index <= n:
    print(index, end=', ')
    index += 1

print('\n' + '>>>>>>>' * 10)
