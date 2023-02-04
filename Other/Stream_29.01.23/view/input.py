from view import output


def input_number(msg: str, error: str):
    while True:
        try:
            num = int(input(msg))
            return num
        except:
            output.print_error(error)


# def input_string():
#     string = input('Введите строку: ')
#     return string
