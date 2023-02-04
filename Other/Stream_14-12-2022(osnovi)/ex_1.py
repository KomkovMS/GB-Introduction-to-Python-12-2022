# работа со строками

number = 5
variable = f'Строка выведет значение number = {number}'
my_list = variable.split()
print(variable)     # Строка выведет значение number = 5
print(my_list)      # ['Строка', 'выведет', 'значение', 'number', '=', '5']
print(my_list[2])   # значение

my_list = variable.replace(' ', '-')
print(my_list)      # Строка-выведет-значение-number-=-5
variable = f'Строка      выведет                значение  number = {number}'
my_list = variable.replace(' ', '').replace('е', 'Е')
print(my_list)      # СтрокавывЕдЕтзначЕниЕnumber=5

