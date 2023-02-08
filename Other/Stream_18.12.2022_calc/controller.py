import operations

import model
import view

def calculate():
    result = 0

    number = view.input_number()
    model.set_memory(number)

    while True:
        oper = view.input_operation()
        model.set_operation(oper)
        if oper == '=':
            break

        number = view.input_number()
        model.set_number(number)

        first = model.get_memory()
        oper = model.get_operation()
        second = model.get_number()

        for operation in operations.operation:
            if oper == operation:
                result = operations.operation.get(oper)(first, second)
        view.print_result(result)
        model.set_memory(result)
