# как добавлять значения переменных в лист

# append - добавляет в конец списка

my_list = []

for i in range(5):
    numbers = int(input(f'Введите {i+1} число: '))
    my_list.append(numbers)

print(my_list)
