from string import ascii_letters
import random

# решение на стриме 07.01.2023

# """
# Дана строка.
# Разделить строку на фрагменты по три подряд идущих символа.
# В каждом фрагменте средний символ заменить на случайный символ,
# не совпадающий ни с одним из символов этого фрагмента.
# Показать фрагменты, упорядоченные по алфавиту.

# """

string = 'Divide the line into fragments of three in a row of walking symbols. \
     asdegerg regsdrg rgterg er ergfaet45hhx ttwtert agergh.'

new_list = []

while len(string) > 0:
    element = string[:3]
    while True:
        letter = random.choice(ascii_letters)
        if letter != element[0] and letter != element[2]:
            new_element = element[0] + letter + element[2]
            break
    new_list.append(new_element)
    string = string[3:]  # Div...ide... th...e l...ine...

print(new_list)
