def my_function():
    return 10


lambda: 10


def result(): return 10


print(result)


def a(): return 10


print(a)
print(type(a))

print(a())


cities = [('Москва', 1000), ('Лас-Вегас', 500, ('Антверпен', 2000))]

print(cities)

print(sorted(cities, key=lambda city: city[1]))


friend1 = {
    'name': 'Max',
    'age': 25,
    'has_car': True
}


friend2 = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# for item in friend1.items():
#    for item in friend2.items():

print(friend1[1][0])
print(friend2[1][0])
