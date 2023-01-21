'''
Функция enumerate()

Функция enumerate() принимается к итерируемому объекту и возвращает новый 
итератор с кортежами из индекса и элементов входных данных

enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])

[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

Нельзя пройтись дважды
'''
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = enumerate(users)
# [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]
print(list(data))

data = enumerate(ids)
print(list(data))   # [(0, 4), (1, 5), (2, 9), (3, 14), (4, 7)]