'''
1. Создайте программу для игры с конфетами человек против человека.
a) Добавьте игру против бота
b) Подумайте как наделить бота 'интеллектом'

'''
from random import randint as RI
from random import choice

# человек против бота:
print('*' * 45)
print('\n  ПРИВЕТСТВУЕМ ВАС В ИГРЕ "К О Н Ф Е Т Ы!\n')
print('*' * 45)
######################################################################


def input_candy(msg):
    while True:
        try:
            number = abs(
                int(input(f'\n{msg}')))
            if number > 0:
                return number
        except:
            print('ОШИБКА! Введите целое число')


msg_1 = 'Сколько конфет положите на стол? '
candy = input_candy(msg_1)
msg_2 = 'Сколько максимум конфет будем брать за один ход? '
candy_m = input_candy(msg_2)

######################################################################
print()
print('*' * 45)
print(f'\nИ так условие: \n- на столе лежит >>> {candy} конфет(-а)(-ы)\n')
print('- меня зовут Бот Ботыч, и мы будем делать\n ход друг после друга\n')


def get_users():
    list_users = []
    list_users.append(input(f'Как Вас зовут? '))
    list_users.append('Бот Ботыч')
    return list_users


list_users = get_users()
######################################################################


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

print(f'- за один ход можно забрать не более,\n  чем {candy_m} конфет.\n'
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
            if user == 'Бот Ботыч':
                user_number = res % (candy_m + 1)
                if user_number == 0:
                    user_number = RI(1, candy_m)
                res = res - user_number
                print(f'Я забрал со стола {user_number} конфет (-у)(-ы)')
            else:
                while True:
                    user_number = abs(
                        int(input('Сколько ты забираешь конфет?: ')))
                    if user_number == 0:
                        print('Вы должны забрать хотя бы 1 конфету')
                        continue
                    if user_number > candy_m:
                        print(f'Вы не можете забрать больше {candy_m} конфет!')
                    elif res < user_number <= candy_m:
                        print(f'Вы не можете забрать конфет больше,\n'
                              'чем осталось на столе!')
                    else:
                        res = res - user_number
                        break
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
