

phone_book = []
path = 'Sem_8/Tel_Book/phone_book.txt'


def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))


def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))


def get_phone_book():
    global phone_book
    return phone_book


def get_contact(text: str):
    global phone_book
    result = []
    for i, contact in enumerate(phone_book):
        for field in contact:
            if text in field:
                result.append((contact, i))
                break
    if len(result) > 1:
        return False
    elif result == []:
        return result
    else:
        return result[0]


def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)

# Это из моего ДЗ
# def f_del_contact(del_contact: str):
#     global phone_book
#     for contact in phone_book:
#         for field in contact:
#             if del_contact in field:
#                 phone_book.remove(contact)
#                 break
#     return phone_book


def delete_contact(contact: list):
    global phone_book
    phone_book.remove(contact)


def change_contact(index: int, new: list):
    global phone_book
    phone_book[index][0] = new[0] if new[0] != '' else phone_book[index][0]
    phone_book[index][1] = new[1] if new[1] != '' else phone_book[index][1]
    phone_book[index][2] = new[2] if new[2] != '' else phone_book[index][2]


def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

# Это из моего ДЗ
# def change_cont(change_: str):
#     global phone_book
#     for contact in phone_book:
#         for field in contact:
#             if change_ in field:
#                 phone_book.remove(contact)
#                 break
#     return phone_book
