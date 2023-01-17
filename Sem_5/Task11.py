'''
Напишите программу, удаляющую из текста все слова, содержащие "абв".
'''
my_str = 'Питон - пожабвлуй лучший из хуабвдших языков вабв миабвре'
new_list = []

# my_str = my_str.split()
# for word in my_str:
#     if 'абв' in word:
#         pass
#     else:
#         new_list.append(word)

# или
# for word in my_str:
#     if not 'абв' in word:
#         new_list.append(word)
# print(' '.join(new_list))   # Питон - лучший из языков

# или
new_list = list(filter(lambda word: not 'абв' in word, my_str.split()))
print(' '.join(new_list))  # Питон - лучший из языков
