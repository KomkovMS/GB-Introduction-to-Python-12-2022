commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы\n']


def main_menu() -> int:
    print('\nГлавное меню:\n')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    choise = ''
    while True:
        try:
            choise = int(input('Выберите пункт меню: '))
            if 0 < choise < 9:
                return choise
            else:
                print('Введите значение от 1 до 8')
        except ValueError:
            print('Введите корректное значение')


def information(message: str):
    print(message)


def show_contacts(phone_list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}.{contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()


def input_error():
    print('Ошибка ввода. Введите корректный пункт меню')


def empty_request():
    print('Искомый контакт не найден')


def end_program():
    print('\nДо свидания! Программа завершена!')


def many_request():
    print('Введите более точные данные. Найдено более одного контакта')


def create_new_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment


def find_contact():
    find = input('Введите искомый элемент: ')
    return find


def select_contact(message: str):
    contact = input(message)
    return contact


def change_contact():
    print('Введите новые данные (если изменения не требуются, нажмите Enter)')
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment


def delete_confirm(contact: str):
    result = input(
        f'\nВы действительно хотите удалить контакт:\n{contact}?\n\n(y/n): ').lower()
    if result == 'yes' or result == 'y' or result == 'да':
        return True
    else:
        return False
