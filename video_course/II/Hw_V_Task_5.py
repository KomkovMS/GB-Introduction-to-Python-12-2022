# 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде,
# например: второе ноября 2013 года.
#
# Склонением пренебречь (2000 года, 2010 года)

list_day = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'вщсьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое'
}

list_month = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

date_input = input('Введите дату (в формате dd.mm.yyyy): ')
day = date_input[:2]
month = date_input[3:5]
year = date_input[6:10]

if day in list_day:
    if month in list_month:
        print(f'{list_day[day]} {list_month[month]} {year} года')


# другое решение на разборе ДЗ

date = '02.11.2013'
d, m, y = date.split('.')
print(d, m, y)

months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '11': 'ноября'
}

days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое'
}

result = f'{days[d]} {months[m]} {y} года.'
print(result)
