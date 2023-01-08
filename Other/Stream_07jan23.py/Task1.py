from string import ascii_letters
import random
from random import choice

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

# варинт 2

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet += alphabet.upper()

s = 'Div213234ide the 567546line into fragmei8it6785678nts of' \
    'thresdgw456235e in a row of walking symbols. asdege768rg'  \
    'regsdrg r745gterg e4568r 9e9 rgf456747ae457568t45hhx ttwet' \
    'ertyeryt6tert a234523465gergh.'


def replacer(frag: str) -> str:
    while True:
        lt = choice(alphabet)
        if lt not in frag and len(frag) > 2:
            return frag[0] + lt + frag[2]

        if len(frag) <= 2:
            return frag


print(list(map(replacer, [s[i:i+3] for i in range(0, len(s), 3)])))
