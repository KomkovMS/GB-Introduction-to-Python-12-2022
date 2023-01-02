# 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

my_list = []

for i in range(3):
    val = int(input(f'Введите значение 1 или 0: '))
    my_list.append(val)

x = my_list[0]
y = my_list[1]
z = my_list[2]

value_1 = not (x or y or z)
value_2 = (not x) and (not y) and (not z)
print(value_1 == value_2)

# другое решение от ученика

for i in range(2):
    x = i
    for j in range(2):
        y = j
        for k in range(2):
            z = k
            bool = not (x or y or z) == ((not x) and (not y) and (not z))
            print(f'{x, y, z} - {bool}')

# решение преподавателя на семинаре
print('x' * 20)

flag = True
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not (x or y or z) != ((not x) and (not y) and (not z)):
                print('Условие не выполнено')
                flag = False
if flag:
    print('Выражение при любом значении верно')

# решение преподавателя на семинаре 2

print('x' * 20)

flag = True
for x in [True, False]:  # можно было поставить range(2) или кортеж (0,1)
    for y in [True, False]:
        for z in [True, False]:
            expression = not (x or y or z) == ((not x) and (not y) and (not z))
            print(x, y, z, expression)


# решение на стриме дек 2022

flag = True

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            expression = not (x or y or z) == (not x and not y and not z)
            print(f'{x=} {y=} {z=} -> {expression}')
            if not expression:
                flag = False

if flag:
    print('Выражение всегда верно')
else:
    print('Выражение не всегда верно')

# x y z
# t t t
# t t f
# t f t
# t f f
# f t t
# f t f
# f f t
# f f f
