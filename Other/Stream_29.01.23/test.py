# отличие try-except от if-else:

num = input('Введите число: ')

try:
    int(num)
    print(int(num))
except:
    print('Это срока')
