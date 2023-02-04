# def print_result(result: int):
#     print(f'Ваш результата {result}')


def print_error(msg: str):
    print(msg)


def print_contact(contacts: list):
    if len(contacts) > 1:
        for contact in contacts:
            contact = contact.strip().split(';')
            print(f'{contact[0]:20} {contact[1]:15} {contact[2]:20}')
    elif len(contacts) == 1:
        contacts = contacts[0].strip().split(';')
        print(f'{contacts[0]:20} {contacts[1]:15} {contacts[2]:20}')
    else:
        print(f'Контакт не существует')
