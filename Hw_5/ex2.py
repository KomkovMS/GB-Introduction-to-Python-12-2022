# логика победителя
# ОСТm+1K
# m - условие игры - сколько можно макс забрать за 1 ход
# +1 дает преимущество последнего хода
# K - количество конфет

candy = 2021
m = 28
res = candy
list_ = ['player_1', 'player_2']
while res > 0:
    for player in list_:
        winner_move = res % (m + 1)
        if winner_move == 0:
            winner_move += 1
        else:
            res = res - winner_move
            break
    print(f'{player} забрал {winner_move}')
    print(f'осталось {res}')
