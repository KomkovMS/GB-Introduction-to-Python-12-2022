from random import randint, choice, sample, shuffle

# 1. Задать случайное число от 0 до 100
print(randint(0, 100))  # 61

# 2. выбрать победителя лотереи из списка players
players = ['Max', 'Leo', 'Kate', 'Bill']
print(choice(players))  # Max (случайный выбор)

# 3. выбрать 3-х победителей лотереии из списка players
print(sample(players, 3))   # ['Bill', 'Max', 'Leo'] (случайная последов-сть)

# 4. перемещать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
shuffle(cards)
# ['9', 'K', 'Q', 'T', '8', 'A', '7', '6', 'J'] (случайная последов-сть)
print(cards)
