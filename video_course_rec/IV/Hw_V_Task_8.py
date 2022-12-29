# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую
# наибольшее из них.


def get_max_number(numbers: list) -> int:
    return max(numbers)


numbers = [33, 75, 23]
max_number = get_max_number(numbers)
print(max_number)

# numbers = [33, 75, 23]
# print(lambda numbers: max(numbers))
