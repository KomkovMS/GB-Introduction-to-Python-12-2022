import view  # 4
import model  # 13


def start():
    choice = ''  # 21
    while choice != 8:  # 22
        choice = view.main_menu()  # 3

        match choice:  # 5
            case 1:  # Открыть файл
                model.open_file()  # 14
                view.info(1)
            case 2:  # Сохранить файл
                model.save_file()   # 33
                view.info(2)
            case 3:  # Показать все контакты
                view.info(3)
                pb = model.get_phone_book()  # 19
                # или в 1 строку view.show_contacts(model.get_phone_book())
                view.show_contacts(pb)  # 20
            case 4:  # Создать контакт
                view.info(4)
                new_contact = list(view.create_new_contact())  # 23
                model.add_new_contact(new_contact)   # 26
            case 5:  # Удалить контакт
                del_ = view.delete_contact()
                model.f_del_contact(del_)
                view.info(5)
            case 6:  # Изменить контакт
                view.info(6)
                change_ = view.f_change_contact()
                model.change_cont(change_)
            case 7:  # Найти контакт
                view.info(7)
                find = view.find_contact()  # 28
                result = model.search_contact(find)  # 30
                view.show_contacts(result)  # 31
            case 8:  # Выход из программы
                view.info(8)
                exit()
            case _:         # рабоатет как else
                view.input_error()
