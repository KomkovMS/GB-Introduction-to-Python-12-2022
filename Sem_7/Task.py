'''
Создать телефонную книгу:

мои наброски

'''


def f_hello():
    print('\nДобро пожаловать в телефонную книгу!\n\n'
          'Вам доступен следующий функционал:\n'
          '1. Открыть файл\n'
          '2. Сохранить файл\n'
          '3. Показать все контакты\n'
          '4. Создать контакт\n'
          '5. Удалить контакт\n'
          '6. Изменить контакт\n'
          '7. Найти контакт\n'
          '8. Выход из программы\n')


f_hello()


def f_input() -> int:
    input_number = int(input('Что вы хотите сделать? Введите номер: '))
    return input_number


menu_number = f_input()


def f_save_file():
    file.write('')
    file.close()


menu_msg = f_menu(menu_number)


def f_show_contacts(number):
    return 0


def f_new_contact(number):
    return 0


def f_del_contact(number):
    return 0


def f_сhange_сontact(number):
    return 0


def f_search_contact(number):
    return 0


def f_exit(number):
    return 0
