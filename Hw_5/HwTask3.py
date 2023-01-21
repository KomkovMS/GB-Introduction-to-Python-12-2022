'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaaabbbcccc -> 5a3b4c
5a3b4c -> aaaaabbbcccc

'''

# модуль сжатия

with open('Hw_5/file_1.txt', mode='r', encoding='utf-8') as f:
    my_txt = f.read()


def get_compression(my_txt):
    compression = ''
    letter = ''
    total = 1
    for item in my_txt:
        if item != letter:
            if letter:
                compression += str(total) + letter
            total = 1
            letter = item
        else:
            total += 1
    return compression


compression = get_compression(my_txt)

with open('Hw_5/file_2.txt', mode='w', encoding='utf-8') as f:
    f.write(compression)

# print(compression)

# модуль восстановления данных

with open('Hw_5/file_2.txt', mode='r', encoding='utf-8') as f:
    my_txt = f.read()


def get_recovery(my_txt):
    total = ''
    recovery = ''
    for item in my_txt:
        if item.isdigit():
            total += item
        else:
            recovery += item * int(total)
            total = ''
    return recovery


recovery = get_recovery(my_txt)

# print(recovery)
with open('Hw_5/file_3.txt', mode='w', encoding='utf-8') as f:
    f.write(recovery)
