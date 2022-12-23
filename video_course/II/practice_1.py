
#         0123456789101112
frinds = 'Максим Леонид'        # False

print('Я' in frinds)

print(len(frinds))  # 13
print(frinds.find('Лео'))  # 7
print(frinds.find('123Лео'))    # -1

print(frinds.split())   # ['Максим', 'Леонид']
print(frinds.split(';'))  # ['Максим Леонид']

frinds = 'Максим Леонид'
print(frinds.isdigit())  # False

frinds = 'Максим Леонид "123"'
print(frinds.isdigit())  # False

num_list = '1234567'
print(num_list.isdigit())   # True

frinds = 'Максим Леонид'
print(frinds.upper())   # МАКСИМ ЛЕОНИД

frinds = 'МаКСим ЛеОНид'
print(frinds.lower())   # максим леонид

my_str = 'Леона́рдо Пиза́нский — первый крупный математик средневековой Европы. \
    Наиболее известен под прозвищем Фибона́ччи. Отец Фибоначчи по торговым делам \
        часто бывал в Алжире, и Леонардо изучал там математику у арабских \
            учителей. Позже Фибоначчи посетил Египет, Сирию, Византию, Сицилию'

print(len(my_str))
print(my_str.find('первый'))


friends = ['Max', 'Leo', 'Kate']
friends.append('Ron')
print(friends)  # ['Max', 'Leo', 'Kate', 'Ron']

friends.pop()
print(friends)  # ['Max', 'Leo', 'Kate']

friends.clear()
print(friends)  # []

friends = ['Max', 'Leo', 'Kate']
friends.remove('Kate')
print(friends)  # ['Max', 'Leo']

friends = ['Max', 'Leo']
del friends[0]
print(friends)  # ['Leo']


hero = 'Superman'
if hero.find('man') != -1:
    print(f'В слове {hero} есть слово man')  # В слове Superman есть слово man
if 'man' in hero:
    print(f'В слове {hero} есть слово man')  # В слове Superman есть слово man


goals = ['стать гуру языка python', 'здоровье', 'накормить кота']
if 'здоровье' in goals:
    print('Все хорошо')  # Все хорошо
