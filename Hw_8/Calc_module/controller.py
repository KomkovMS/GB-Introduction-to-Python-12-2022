import model
import view

start_input = model.st_input()

my_input = model.func_str(start_input)

my_input = model.verification(start_input, my_input)

orig_example = my_input.copy()


while len(my_input) > 1:
    model.calculate(my_input, '*', '/')
    model.calculate(my_input, '+', '-')

view.print_result(my_input, orig_example)
