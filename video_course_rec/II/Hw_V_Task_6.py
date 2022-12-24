# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные
# элементы исходного.

# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]

# В этом случае ответ будет:
# [5, 8]


my_list_1 = [2, 2, 5, 12, 8, 2, 12]

unic = []

for i in range(len(my_list_1)):
    if my_list_1.count(my_list_1[i]) < 2:
        unic.append(my_list_1[i])
print(unic)

# решение на разборе ДЗ

numbers = [2, 2, 5, 12, 8, 2, 12]
result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)
print(result)
