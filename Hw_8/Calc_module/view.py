
def start() -> str:
    my_input = input('Введите выражение: ')
    return my_input


def print_result(my_input, orig_example):
    print(f'{" ".join(orig_example)} = {my_input[0]}')
