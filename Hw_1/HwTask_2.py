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
