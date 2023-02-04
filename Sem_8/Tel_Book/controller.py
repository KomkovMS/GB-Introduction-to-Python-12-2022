import view
import model


def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_file()
                view.info(1)
            case 2:
                model.save_file()
                view.info(2)
            case 3:
                view.info(3)
                pb = model.get_phone_book()
                view.show_contacts(pb)
            case 4:
                view.info(4)
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
                view.info(5)
            case 5:
                pass
            case 6:
                pass
            case 7:
                view.info(11)
                find = view.find_contact()
                result = model.search_contact(find)
                view.info(12)
                view.show_contacts(result)
            case 8:
                view.info(13)
                exit()
            case _:
                view.input_error()
