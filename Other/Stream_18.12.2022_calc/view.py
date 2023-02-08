from decimal import Decimal

def input_number():
    while True:
        try:
            number = float(input('Введите число: '))
            number = Decimal(str(number))
            return number
        except:
            print('Введите число!')

def input_operation():
    while True:
        operation = input('Введите оператор: ')
        if operation in ['+', '-', '*', '/', '^', '=']:
            return operation
        else:
            print('Проверьте правильность ввода оператора (+, -, *, /, ^, =)')

def print_memory(value):
    print(value)

def print_result(value: Decimal):
    if value == int(value):
        print(f'Результат: {int(value)}')
    else:
        print(f'Результат: {round(value, 4)}')