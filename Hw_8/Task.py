'''
Строчный калькулятор (созданный на 6 семинаре) перевести в архитектуру

'''
my_input = input('Введите выражение: ')

my_input = my_input.replace(' ', '').replace(
    '+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
# print(my_input)

if my_input.startswith(' -'):
    my_input = '-' + my_input[3:]

my_input = my_input.split()
orig_example = my_input.copy()
operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             }


def calculate(operator_1, operator_2):
    i = 0
    while operator_1 in my_input or operator_2 in my_input:
        if my_input[i] in [operator_1, operator_2]:
            my_input[i-1] = operation.get(my_input[i]
                                          )(int(my_input[i - 1]), int(my_input[i+1]))
            my_input.pop(i)
            my_input.pop(i)
        else:
            i += 1


while len(my_input) > 1:
    calculate('*', '/')
    calculate('+', '-')

print(f'{" ".join(orig_example)} = {my_input[0]}')
