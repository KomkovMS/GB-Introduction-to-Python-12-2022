
phonebook = []


def f_menu(choise: int):
    match choise:
        case 1:
            print('Вы выбрали: "Открыть файл"')
            f_open_file()
        case 2:
            print('Вы выбрали: "Сохранить файл"')
            f_save_file()
        case 3:
            print('Вы выбрали: "Показать все контакты"')
            f_show_contacts()
        case 4:
            print('Вы выбрали: "Создать контакт"')
            f_new_contact()
        case 5:
            print('Вы выбрали: "Удалить контакт"')
            f_del_contact()
        case 6:
            print('Вы выбрали: "Изменить контакт"')
            f_сhange_сontact()
        case 7:
            print('Вы выбрали: "Найти контакт"')
            f_search_contact()
        case 8:
            print('Выход из программы"')
            f_exit()
        case _:
            print('Вы ввели не корректный номер')
            f_input()
    return choise   # ???


def f_open_file():
    path = 'Sem_7\phone_book.csv'
    with open(path, 'r', encoding='utf-8') as data:
        phone_book.data.read().split('n')
    print('Файл открыт')
    return phone_book


def f_save_file()
