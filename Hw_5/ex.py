from random import choice

candy = 100
res = candy

list_users = ['Max', 'Ira']
count = 0
mixed_list = []
first_move = choice(list_users)
mixed_list.append(first_move)
for user in list_users:
    if user != first_move:
        mixed_list.append(user)
print(list_users)
print(mixed_list)

is_winner = False
winner_name = None

while not is_winner:
    for user in mixed_list:
        print(f'ход пользователя {user}')
        user_number = int(input('Сколько забераете конфет?: '))
        res = res - user_number
        print(f'На столе осталось {res} конфет')
        if res == 0:
            is_winner = True
            winner_name = user
            break
else:
    print(f'Победа! Поздравляем тебя - {winner_name}!!!')
