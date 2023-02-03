# 4 menu

commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']


list_msg = ['\nФайл успешно открыт\n',
            '\nФайл успешно сохранен\n',
            '\nСписок контактов: \n',
            '\nВыбран пункт "Создать контакт"\n',
            '\nКонтакт успешно удален\n',
            '\nКонтакт успешно изменен\n',
            '\nВыбран пункт "Найти контакт"\n',
            '\nВыбран пункт "Выход из программы"\n']


def main_menu() -> int:  # 5
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    choise = int(input('Выберите пункт меню: '))
    return choise


def info(number: int):
    for i, item in enumerate(list_msg, 1):
        if number == i:
            print(item)


def show_contacts(phone_list: list):    # 17
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:   # 22
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}.{contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()


def input_error():  # 21
    print('Ошибка ввода. Введите корректный пункт меню')


def create_new_contact():  # 24
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment


def find_contact():  # 27
    find = input('Введите искомый элемент: ')
    return find


def delete_contact():
    delete = input('Введите контакт для удаления: ')
    return delete


def f_change_contact():
    change = input('Введите контакт для изменения: ')
    return
