'''
1. Создайте программу для игры с конфетами человек против человека.

Условие задачи: 
На столе лежит заданное количество конфет. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход.

a) Добавьте игру против бота
b) Подумайте как наделить бота 'интеллектом'
'''
from random import choice

# человек против человека:
print('*' * 45)
print('\n     ПРИВЕТСТВУЕМ ВАС В ИГРЕ "КОНФЕТЫ!\n')
print('*' * 45)
######################################################################


def input_candy():
    while True:
        try:
            number = abs(
                int(input('\nСколько конфет положите на стол? ')))
            if number > 0:
                return number
        except:
            print('ОШИБКА! Введите целое число')


candy = input_candy()
######################################################################
print()
print('*' * 45)
print(f'\nИ так условие: \n- на столе лежит >>> {candy} конфет(-а)(-ы)\n')
print('- играют два игрока делая ход друг после друга\n')


def get_user():
    list_user = []
    for i in range(1, 3):
        list_user.append(input(f'Введите имя {i}-го игрока: '))
    return list_user


list_users = get_user()
######################################################################

print('\n- первый ход определяется жеребьёвкой.\n')


def get_first_move(list_: list) -> str:
    return choice(list_)


first_move = get_first_move(list_users)


def get_mixed_list(li_users, first):
    mixed_list = []
    mixed_list.append(first)
    for user in li_users:
        if user != first:
            mixed_list.append(user)
    return mixed_list


new_list = get_mixed_list(list_users, first_move)

print(f'По результатам жеребьевки начинает >>> {new_list[0]}\n')


######################################################################

print('- за один ход можно забрать не более,\n  чем 28 конфет.\n'
      '- все конфеты оппонента достаются сделавшему\n  последний ход.\n'
      '\nУдачи!\n')
print('=================== START ===================\n')
######################################################################

res = candy

is_winner = False
winner_name = None


while not is_winner:
    for user in new_list:
        print(f'ход пользователя >>> {user}')
        while True:
            user_number = abs(int(input('Сколько забираете конфет?: ')))
            if user_number > 28:
                print(f'Вы не можете забрать больше 28 конфет!')
            elif res < user_number <= 28:
                print(f'Вы не можете забрать конфет больше,\n'
                      'чем осталось на столе!')
            else:
                res = res - user_number
                break
        if res > 0:
            print(f'На столе осталось >> {res} конфет')
        else:
            print(f'На столе не осталось конфет!\n')
            is_winner = True
            winner_name = user
            break
else:
    print('*' * 45)
    print(f'\nПобеда! Поздравляем тебя - {winner_name}!!!\n')
    print('*' * 45)
print()
print('================== THE END ==================\n')
