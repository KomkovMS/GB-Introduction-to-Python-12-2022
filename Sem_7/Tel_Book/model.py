

phone_book = []  # 6
path = 'Sem_7/Tel_Book/phone_book.txt'  # 7


def open_file():  # 8
    global phone_book  # 9
    global path  # 10
    with open(path, 'r', encoding='UTF-8') as data:  # 11
        file = data.readlines()  # 12
    for contact in file:  # 15
        phone_book.append(contact.strip().split(';'))  # 16


def save_file():    # 32
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))


def get_phone_book():  # 18
    global phone_book
    return phone_book


def add_new_contact(new_contact: list):  # 25
    global phone_book
    phone_book.append(new_contact)


def f_del_contact(del_contact: str):
    global phone_book
    for contact in phone_book:
        for field in contact:
            if del_contact in field:
                phone_book.remove(contact)
                break
    return phone_book


def search_contact(find: str):  # 29
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result


def change_cont(change_: str):
    global phone_book
    for contact in phone_book:
        for field in contact:
            if change_ in field:
                phone_book.remove(change_, phone_book.append(
                    add_new_contact(change_)))
                break
    return phone_book
