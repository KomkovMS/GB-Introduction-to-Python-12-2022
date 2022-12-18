# Напишите программу, которая на вход принимает число и проверяет, кратно ли
# оно 5 и 10 или 15, но не 30

# Мое решение:

number = int(input('Enter a number: '))

if number % 5 and number % 10 or number % 15 and not number % 30 == 0:
    print('кратно')
else:
    print('НЕ кратно')

# Решение на семинаре (преподаватель):

number = int(input('Enter a number: '))

if number % 10 or number % 15 and not number % 30 == 0:
    print('Условие выполнено')
else:
    print('Условие НЕ выполнено')
