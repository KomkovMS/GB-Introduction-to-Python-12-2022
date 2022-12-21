# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def get_binary_number(inp_num: int) -> int:
    num_2 = []
    division = 0
    tempo = 0
    while inp_num > 0:
        division = inp_num // 2
        tempo = inp_num - division * 2
        num_2.append(tempo)
        inp_num = inp_num // 2

    num_2.reverse()
    res = int(''.join(map(str, num_2)))
    return res


inp_num = int(input('Enter number: '))
print(f'{inp_num} -> {get_binary_number(inp_num)}')
