from random import randint as RI

# решение на стриме дек 2022

# 1 этап

list_ = [str(RI(1000, 10000)) for _ in range(10)]
print(list_)

# 2 этап
while True:
    number = input('Введите цифру: ')
    if len(number) == 1:
        break
    else:
        print('Введите однозначное число')


for i in range(len(list_)):
    list_[i] = list_[i].replace(number, '')

print(list_)

# 3 этап:
for i in range(len(list_)):
    while len(list_[i]) > 1:
        m = 0
        for k in list_[i]:
            m += int(k)
        list_[i] = str(m)

print(list_)

# 4 этап:
print(list(set(list_)))
