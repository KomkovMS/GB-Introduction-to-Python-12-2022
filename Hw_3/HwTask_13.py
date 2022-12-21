# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так:

# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def f_fib(k: int, list_fib: list) -> list:
    for i in range(1, k):
        list_fib.append(list_fib[i] + list_fib[i-1])

    for j in range(k):
        list_fib.insert(0, (list_fib[1] - list_fib[0]))

    return list_fib


k = 8  # int(input('Введите число'))
list_fib = [0, 1]
fib_res = f_fib(k, list_fib)

print(f'для k={k} список будет выглядеть так: \n'
      f'{fib_res}')
