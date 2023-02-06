import view
import model


def start():
    pb = model.PhoneBook()
    choice = ''
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                view.information('\nВыбран пункт "Открыть файл"')
                pb.open()  # model.open_file()
                # view.info(1)
                view.information('\nФайл успешно открыт')
            case 2:
                view.information('\nВыбран пункт "Сохранить файл"')
                pb.save()  # model.save_file()
                # view.info(2)
                view.information('\nФайл успешно сохранен')
            case 3:
                view.information('\nВыбран пункт "Показать все контакты"')
                pb = pb.get()
                view.information('\nСписок контактов:')
                view.show_contacts(pb)
            case 4:
                # view.info(4)
                view.information('\nВыбран пункт "Создать контакты"\n')
                new_contact = list(view.create_new_contact())
                pb.new(new_contact)
                # view.info(5)
                view.information(
                    f'\nКонтакт "{new_contact[0]}" успешно создан\n')
            case 5:
                del_name = view.select_contact('\nВведите удаляемый контакт: ')
                contact = pb.get_contact(del_name)
                if contact:
                    confirm = view.delete_confirm(contact[0][0])
                    if confirm:
                        pb.delete(contact[0])
                        view.information(
                            f'\nКонтакт "{contact[0][0]}" успешно удален\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 6:
                name = view.select_contact('Введите изменяемый контакт: ')
                contact = pb.get_contact(name)
                if contact:
                    change_contact = view.change_contact()
                    pb.change(contact[1], list(change_contact))
                    view.information(
                        f'\nКонтакт "{contact[0][0]}" успешно изменен\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 7:
                view.information('\nВыбран пункт "Найти контакт"\n')
                find = view.find_contact()
                result = pb.search(find)
                # view.info(12)
                view.information('\nПо вашему запросу найдены:\n')
                view.show_contacts(result)
            case 8:
                # view.info(13)
                view.information('\nВыбран пункт меню "Выход из программы"\n')
                view.end_program()
                break
