# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


quarter_number = int(input(f'Enter quarter number: '))

if quarter_number == 1:
    print(f'Для четверти: {quarter_number} x > 0, y > 0')
elif quarter_number == 2:
    print(f'Для четверти: {quarter_number} x < 0, y > 0')
elif quarter_number == 3:
    print(f'Для четверти: {quarter_number} x < 0, y < 0')
elif quarter_number == 4:
    print(f'Для четверти: {quarter_number} x > 0, y < 0')
else:
    print(f'{quarter_number} - такой четверти не существует')

# разбор решения на семинаре от преподавателя

choice = int(input('Введите номер четверти: '))

match choice:
    case 1:
        print(f'Для четверти: {quarter_number} x > 0, y > 0')
    case 2:
        print(f'Для четверти: {quarter_number} x < 0, y > 0')
    case 3:
        print(f'Для четверти: {quarter_number} x < 0, y < 0')
    case 4:
        print(f'Для четверти: {quarter_number} x > 0, y < 0')
    case _:
        print(f'{quarter_number} - такой четверти не существует')

# решение на стриме дек 2022


def input_int():
    while True:
        try:
            number = int(input('Введите номер четверти: '))
            if 0 < number < 5:
                return number
            else:
                print('Такой четверти нет, попробуйте еще раз')
        except:
            print('ОШИБКА! Введите целое число')


match input_int():
    case 1:
        print(f'1 четветь x > 0, y > 0')
    case 2:
        print(f'2 четветь x < 0, y > 0')
    case 3:
        print(f'3 четветь x < 0, y < 0')
    case 4:
        print(f'4 четветь x > 0, y < 0')
    case _:
        print(f'такой четверти не существует')
