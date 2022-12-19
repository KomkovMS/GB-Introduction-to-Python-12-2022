# Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

# мое решение (НЕПРАВИЛЬНО)
my_list = ['dads', 'awev', '123d', 'vzsd']
result = ''

for i in range(len(my_list)):
    if my_list[i].isdigit():
        result = 'yes'
        break
    else:
        result = 'no'
print(f'присутствует ли в заданном списке строк некое число? - {result}')

# решение преподавателя на семинаре

my_list_2 = ['ASDF12', 'FВЫ34QWE', '12fsd456dfsdf', 'sdgsdfafsd213sdfv']
search = input('Введите искомое число: ')

for item in my_list_2:
    if search in item:
        print(f'Число {search} входит в заданный список')
        break
else:
    print(f'Число {search} НЕ ходит в заданный список')

# решение № 2 преподавателя на семинаре

my_list_3 = ['ASDF12', 'FВЫ34QWE', '12fsd456dfsdf', 'sdgsdfafsd213sdfv']
search = input('Введите искомое число: ')

trigger = True  # 1

for item in my_list_3:
    if search in item:
        print(f'Число {search} входит в заданный список')
        trigger = False  # 0
        break
if trigger:
    print(f'Число {search} НЕ ходит в заданный список')
