# работа со строками и списками, словари

# .split()

my_string = 'Питон самый лучший в мире язык'
new_string = my_string.split()  # () по умолчанию (' ')
print(my_string)    # Питон самый лучший в мире язык
print(new_string)   # ['Питон', 'самый', 'лучший', 'в', 'мире', 'язык']

my_string = 'Питон самый лучший в мире язык'
new_string = my_string.split('и')
print(new_string)   # ['П', 'тон самый лучш', 'й в м', 'ре язык']

# .replace()
my_string = 'Питон самый лучший в мире язык'
# принимает 2 аргумента, что менять и на что
new_string = my_string.replace('и', '$')
print(new_string)   # П$тон самый лучш$й в м$ре язык

my_string = 'Питон самый лучший в мире язык'
new_string = my_string.replace('и', '$').replace(' ', '!!!')
print(new_string)   # П$тон!!!самый!!!лучш$й!!!в!!!м$ре!!!язык

# .strip() - убирает пробелы в начале и в конце строки
my_string = '          \tПитон самый лучший в мире язык\n'
new_string = my_string.strip()
print(my_string)  # Питон самый лучший в мире язык
print(new_string)   # Питон самый лучший в мире язык
# .lstrip() - убирает слева, .rstrip() - убирает справа

# startswith(), endswith() - если начинается и оканчивается
my_string = 'Питон самый лучший в мире язык'
if my_string.lower().startswith('пит'):
    print('Все верно')  # Все верно
if my_string.endswith('язык'):
    print('Все верно2')  # Все верно2

# lower(), # upper()
my_string = 'Питон самый лучший в мире язык'
new_string = my_string.lower()
print(new_string)   # питон самый лучший в мире язык
new_string = my_string.upper()
print(new_string)   # ПИТОН САМЫЙ ЛУЧШИЙ В МИРЕ ЯЗЫК

# join()
my_list = ['21', '23', 'asdasd', 'kfgyh']
add = '-'
new_list = add.join(my_list)
print(new_list)     # 21-23-asdasd-kfgyh

my_list = ['21', '23', 'asdasd', 'kfgyh']
print(' '.join(my_list))  # 21 23 asdasd kfgyh

# словари

#
my_dict = {32: '32', 1: 'один', 'Ключ': 214567, 'Список': [324, 325, 543, 346]}

print(my_dict[1])   # один
# print(my_dict[2])   # KeyError: 2

# лучше обращаться через метод get()
print(my_dict.get(2))   # None
print(my_dict.get(2, 'нет такого ключа'))   # нет такого ключа
print(my_dict.get(1, 'нет такого ключа'))   # один

my_dict = {32: '32', 3: 45, 1: 'один', 'Ключ': 214567}
print(my_dict.get(2, 0) + my_dict.get(3, 0))    # 45

# добавление в словарь нового ключа
my_dict = {32: '32', 3: 45, 1: 'один', 'Ключ': 214567}
my_dict['New'] = 'value'
print(my_dict)  # {32: '32', 3: 45, 1: 'один', 'Ключ': 214567, 'New': 'value'}
my_dict[32] = 'замена'
# {32: 'замена', 3: 45, 1: 'один', 'Ключ': 214567, 'New': 'value'}
print(my_dict)
my_dict[3] = my_dict.get(3) + 1
# {32: 'замена', 3: 46, 1: 'один', 'Ключ': 214567, 'New': 'value'}
print(my_dict)
