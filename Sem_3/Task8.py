# 3. Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# my decision

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "ertqwe"]
search = input('Введите строку для поиска: ')
count = 0

for i in range(len(my_list)):
    if search == my_list[i]:  # здесь нужно использовать не in, a ==
        count += 1
        if count == 2:
            print(f'список: {my_list}, ищем {search}, ответ: {i}')
            break
else:
    print(f'список: {my_list}б ищем {search}, ответ: -1')

# решение группы на семинаре

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "ertqwe"]
# search = input('Введите строку для поиска: ')

# position = 0

# for item in my_list:
#     if search == item:
#         count += 1
#     if count == 2:
#         break
#     position += 1
# if count >= 2:
#     print(position)
# else:
#     print('-1')

# другое решение

list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
list_2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
list_3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
list_4 = ["123", "234", 123, "567"]
list_5 = []


def search_str(my_list, my_str):
    value_1 = 0
    value_2 = 0
    for i in my_list:
        if i == my_str:
            if value_1 == 1:
                print(f'позиция второго вхождения {value_2}')
                break
            value_1 = 1
        value_2 += 1
    else:
        print('Нет второго вхождения -1')


search_str(list_1, "qwe")
search_str(list_2, "йцу")
search_str(list_3, "йцу")
search_str(list_4, "123")
search_str(list_5, "123")


# решение преподавателя

def check(my_list: list, search: str):
    count = 0
    for i in range(len(my_list)):
        if search == my_list[i]:
            count += 1
            if count == 2:
                print(f'Второй индекс вхождения - {i}')
                break
    else:
        print('Второго вхождения нет')


print(list_1.index('qwe', 2))  # аналогично check(list_1, 'qwe')
check(list_2, "йцу")
check(list_3, "йцу")
check(list_1, "123")
