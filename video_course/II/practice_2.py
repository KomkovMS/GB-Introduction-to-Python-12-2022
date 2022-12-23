friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'quest', 'user')

if 'Max' in friends:
    print('Уменя есть этот друг')   # Уменя есть этот друг

if 'M' in friend_name:
    print('Буква М есть в имени друга')  # Буква М есть в имени друга

# while
friends = ['Max', 'Leo', 'Kate']
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)   # Max Leo Kate
    i += 1

# for
# перебор списка
friends = ['Max', 'Leo', 'Kate']
for friend in friends:
    print(friend)   # Max Leo Kate
print('end')    # end
# перебор строки
friend_name = 'Max'
for letter in friend_name:
    print(letter)   # M a x
print('end')    # end
# перебор кортежа
roles = ('admin', 'quest', 'user')
for item in roles:
    print(item)  # admin quest user
print('end')    # end
