# решение на стриме 07.01.2023


'''
Дан текст. Найдите наибольшее количество идущих подряд цифр
'''

string = 'Div213234ide the 567546line into fragmei8it6785678nts of' \
    'thresdgw456235e in a row of walking symbols. asdege768rg'  \
    'regsdrg r745gterg e4568r 9e9 rgf456747ae457568t45hhx ttwet' \
    'ertyeryt6tert a234523465gergh.'

count = 0
max = 0

for letter in string:
    if letter.isdigit():
        count += 1
    else:
        if count > max:
            max = count
        count = 0

print(max)
