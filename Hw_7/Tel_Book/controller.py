import view  # 4
import model  # 13


def start():
    choice = ''  # 21
    while choice != 8:  # 22
        choice = view.main_menu()  # 3

        match choice:  # 5
            case 1:  # Открыть файл
                model.open_file()  # 14
                view.info(1)        # Файл успешно открыт
            case 2:  # Сохранить файл
                model.save_file()   # 33
                view.info(2)    # Файл успешно сохранен
            case 3:  # Показать все контакты
                view.info(3)    # Список контактов
                pb = model.get_phone_book()  # 19
                # или в 1 строку view.show_contacts(model.get_phone_book())
                view.show_contacts(pb)  # 20
            case 4:  # Создать контакт
                view.info(4)    # Выбран пункт "Создать контакт"
                new_contact = list(view.create_new_contact())  # 23
                model.add_new_contact(new_contact)   # 26
                view.info(5)    # Контакт успешно создан
            case 5:  # Удалить контакт
                view.info(6)    # Выбран пункт "Удалить контакт"
                del_ = view.delete_contact()
                model.f_del_contact(del_)
                view.info(7)    # Контакт успешно удален
            case 6:  # Изменить контакт
                view.info(8)    # Выбран пункт "Изменить контакт
                change_ = view.f_change_contact()
                model.change_cont(change_)
                view.info(9)    # Введите новые данные контакта
                new_contact = list(view.create_new_contact())  # 23
                model.add_new_contact(new_contact)
                view.info(10)   # Контакт успешно изменен
            case 7:  # Найти контакт
                view.info(11)   # Выбран пункт "Найти контакт
                find = view.find_contact()  # 28
                result = model.search_contact(find)  # 30
                view.info(12)  # По Вашему запросу найдены:
                view.show_contacts(result)  # 31
            case 8:  # Выход из программы
                view.info(13)   # Выбран пункт "Выход из программы
                exit()
            case _:         # рабоатет как else
                view.input_error()
