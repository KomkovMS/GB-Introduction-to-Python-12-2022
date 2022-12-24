friends = ['Max', 'Leo', 'Kate']
print(friends)      # ['Max', 'Leo', 'Kate']
print(type(friends))    # <class 'list'>
friend = friends[0]
print(friend)           # Max
print(type(friend))     # <class 'str'>

# как добавить возраст другу?
friend = {
    'name': 'Max',
    'age': 23
}

print(friend)  # {'name': 'Max', 'age': 23}
print(type(friend))  # <class 'dict'>

print(friend['age'])    # 23

friend['has_car'] = True
print(friend)   # {'name': 'Max', 'age': 23, 'has_car': True}

friend['has_car'] = False
print(friend)   # {'name': 'Max', 'age': 23, 'has_car': False}

# удаление ключа и значения
del friend['age']
print(friend)   # {'name': 'Max', 'has_car': False}

# работа оператора in и словаря
if 'name' in friend:
    print('Есть имя')   # Есть имя
else:
    print('нет')


friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# по ключам
for key in friend.keys():
    print(key)              # name      # age    # has_car
for key in friend.keys():
    print(friend[key])      # Max       # 23     # True
    # тоже самое что и
for key in friend:
    print(key)              # name      # age    # has_car
    print(friend[key])      # Max       # 23     # True

# по значениям
for value in friend.values():
    print(value)            # Max       # 23     # True


# по паре ключ-значение
for item in friend.items():
    print(item)             # ('name', 'Max') # ('age', 23) # ('has_car', True)

for key, val in friend.items():
    print(key)              # name      # age    # has_car
    print(val)              # Max       # 23     # True
