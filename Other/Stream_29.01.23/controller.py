# def input_number():   ------------------->>> view
#     num = int(input('Введите число: '))
#     return num


# def num_pow(num: int):  ------------------->>> model
#     return num**2


# def print_result(result: int):  ------------------->>> view
#     print(result)
from view import input, output
import model
import phone_book

phone_book.load_phone_book()
contacts = phone_book.get_all()
output.print_contact(contacts)
con_id = input.input_number('Введите ID контакта: ',
                            'ID должно быть целым цислом')
output.print_contact(phone_book.get_contact(con_id - 1))

# number = input.input_number()

# num_2 = model.num_pow(number)

# output.print_result(num_2)
