'''
Строчный калькулятор (созданный на 6 семинаре) перевести в архитектуру

'''


# def start() -> str:
#     my_input = input('Введите выражение: ')
#     return my_input


# def func_str(my_str: str) -> list:
#     my_str = my_str.replace(' ', '').replace(
#         '+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
#     if my_str.startswith(' -'):
#         my_str = '-' + my_input[3:]
#     return my_str.split()


# start_input = start()

# my_input = func_str(start_input)

# orig_example = my_input.copy()

# operation = {'+': lambda x, y: x + y,
#              '-': lambda x, y: x - y,
#              '*': lambda x, y: x * y,
#              '/': lambda x, y: x / y,
#              }


# def calculate(operator_1, operator_2):
#     i = 0
#     while operator_1 in my_input or operator_2 in my_input:
#         if my_input[i] in [operator_1, operator_2]:
#             my_input[i-1] = operation.get(my_input[i]
#                                           )(int(my_input[i - 1]), int(my_input[i+1]))
#             my_input.pop(i)
#             my_input.pop(i)
#         else:
#             i += 1


# while len(my_input) > 1:
#     calculate('*', '/')
#     calculate('+', '-')


# def print_result(my_input, orig_example):
#     print(f'{" ".join(orig_example)} = {my_input[0]}')


# result = print_result(my_input, orig_example)
