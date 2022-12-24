# Когда нам может помочь range

winners = ['Max', 'Leo', 'Kate']

# простой перебор
for winner in winners:
    print(winner)

# что делать если нам нужно вывести место победителя?
# использовать while?
# или есть способ лучше?

# вывести нечетные цифры от 1 до 5
numbers = [1, 3, 5]

for number in numbers:
    print(number)

# как это сделать если цифр будет 100? 1000?
# использовать while?
# или есть способ лучше?


numbers = range(10)
print(numbers)  # range(0, 10)
print(type(numbers))    # <class 'range'>

print(list(numbers))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

winners = ['Max', 'Leo', 'Kate']

# простой перебор
for winner in winners:
    print(winner)

# используем range
for i in range(len(winners)):
    # print(i)
    print(f'{i+1} ) {winners[i]}')  # 1 ) Max
    # 2 ) Leo
    # 3 ) Kate

# или

# используем range
for i in range(1, len(winners)+1):
    # print(i)
    print(f'{i} ) {winners[i-1]}')  # 1 ) Max
    # 2 ) Leo
    # 3 ) Kate

# вывести нечетные цифры от 1 до 5
print(list(range(1, 6, 2)))  # [1, 3, 5]

for number in range(1, 6, 2):
    print(number)   # 1
    # 3
    # 5
