# Пользователь вводит 3 числа. Найти минимальное из них, максимальное из них,
# их сумму и вывести результат на экран


def get_dig_list() -> list:
    my_list = []
    input_number = input('Введите три числа через пробел: ')
    for item in input_number.split():
        if item.isdigit():
            my_list.append(int(item))

    return my_list


dig_list = get_dig_list()


print(dig_list)

max_number = max(dig_list)
min_number = min(dig_list)
sum_number = sum(dig_list)
print(max_number)
print(min_number)
print(sum_number)


# или

numbers = []

for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(numbers)

max_number = max(numbers)
min_number = min(numbers)
sum_number = sum(numbers)
print(max_number)
print(min_number)
print(sum_number)
