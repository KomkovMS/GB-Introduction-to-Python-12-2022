cities = ['Las vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']

print(type(cities))     # <class 'list'>
print(cities)           # ['Las vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']

# избавиться от повторяющихся элементов - преобразовать список в множество
cities = set(cities)
print(type(cities))     # <class 'set'>
print(cities)           # {'Moscow', 'Paris', 'Las vegas'}

cities = {'Las vegas', 'Paris', 'Moscow'}

# добавление элемента в множество .add()
cities.add('Burma')
print(cities)           # {'Paris', 'Las vegas', 'Moscow', 'Burma'}

# удаление элемента .remove()
cities.remove('Paris')
print(cities)           # {'Las vegas', 'Burma', 'Moscow'}

# использование оператора in
print('Las vegas' in cities)    # True

# использование цикла for
for city in cities:
    print(city)         # Las vegas     # Burma     # Moscow

# семеяная пара собирается в отпуск
# каждый из супругов собирает в поездку вещи
# Max взял эти вещи:
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Kate взяла эти вещи:
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# какие вещи взяли супруги? (объединение)
# {'Помада', 'Телефон', 'Бритва', 'Рубашка', 'Шорты', 'Зонтик'}
print(max_things | kate_things)

# найти вещи повторяющиеся? (пересечение)
print(max_things & kate_things)  # {'Шорты', 'Телефон'}

# какие вещи взял max, но не взяла kate? (вычитание)
print(max_things - kate_things)  # {'Бритва', 'Рубашка'}

# какие вещи взяла kate, но не взял max? (вычитание)
print(kate_things - max_things)  # {'Зонтик', 'Помада'}
