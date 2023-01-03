# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# 1*1=1 2*(1*1) 3*(2*(1*1)) 4*(3*(2*(1*1))

def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * fact(n - 1)


n = int(input('Enter number: '))
my_list = []

for i in range(1, n + 1):
    i = fact(i)
    my_list.append(i)

print(my_list)
