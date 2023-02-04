phone_book = []


def load_phone_book():
    global phone_book
    with open('Other/Stream_29.01.23/pb.txt', 'r', encoding='UTF-8') as file:
        phone_book = file.readlines()


def get_all():
    global phone_book
    return phone_book


def get_contact(contact_id: int):
    global phone_book
    if 0 < contact_id < len(phone_book):
        return [phone_book[contact_id]]
    return []
