'''
Введите число. Вывести на экран его квадрат

'''


def get_square_number(number: int) -> int:
    result = number ** 2
    return result


def input_number() -> int:
    number = int(input('Введите число: '))
    return number


def print_result(number: int, result: int) -> int:

    print(f'Квадрат числа {number} = {result}')


number = input_number()
result = get_square_number(number)
print_result(number, result)
