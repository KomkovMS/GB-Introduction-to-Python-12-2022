import view
import mat_oper


def st_input():
    start = view.start()
    return start


def func_str(my_str: str) -> str:
    my_str = my_str.strip().replace(' ', '').replace('+', ' + ').\
        replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    return my_str


def verification(s_input, my_str) -> list:
    if my_str.startswith(' -'):
        my_str = '-' + s_input[3:]
    return my_str.split()


def calculate(my_input, operator_1, operator_2):
    i = 0
    while operator_1 in my_input or operator_2 in my_input:
        if my_input[i] in [operator_1, operator_2]:
            my_input[i-1] = mat_oper.operation.get(my_input[i])(
                int(my_input[i - 1]), int(my_input[i+1]))
            my_input.pop(i)
            my_input.pop(i)
        else:
            i += 1
