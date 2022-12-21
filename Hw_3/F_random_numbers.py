import random

# генерирует список случайных вещественных чисел


def list_random_material_numbers(my_list: list,
                                 size_items: int,
                                 zeros_after_min: int,
                                 zeros_after_max: int,
                                 size_min_list: int,
                                 size_max_list: int
                                 ) -> list:
    for _ in range(size_items):
        amount = random.randint(zeros_after_min, zeros_after_max)
        number = round(random.uniform(size_min_list, size_max_list), amount)
        if number == int(number):
            my_list.append(int(number))
        else:
            my_list.append(number)

    return my_list
