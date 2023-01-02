# 1. Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.

# Пример:

# 6 -> да
# 7 -> да
# 1 -> нет


week = 7
day = int(input(f'Введите день недели цифрой: '))

while True:
    if day == 0 or day > week:
        day = int(
            input(f'Вы ввели {day} - это не день недели, повторите ввод: '))
    if day < 0:
        day *= -1
    else:
        if day == week - 1 or day == week:
            print(f'{day} -> да, этот день является выходным')
            break
        else:
            print(f'{day} -> нет, этот день НЕ является выходным')
            break


# разбор решения на семинаре от преподавателя

day = int(input('Введите день недели: '))

if 0 < day < 8:
    if day > 5:
        print('Выходной')
    else:
        print('Будни')
else:
    print('ты что то не то ввел')


# решение на стриме дек 2022
def input_int():
    while True:
        try:  # попробуй ввести число...
            number = int(input('Введите целое число: '))
            return number
        except:
            print('ОШИБКА! Введите целое число')


day = input_int()

if 0 < day < 8:
    if day < 6:
        print('будни')
    else:
        print('выходные')
else:
    print('Соррян, но ты что-то не то ввел')
