'''
В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
Найдите это число.

'''
# решение одногрупников на семинаре

path = 'Sem_5/file.txt'  # или r'Sem_5\file.txt'
with open(path, 'r') as data:
    text = data.read().split()
    print(text)
    text = list(map(int, text))
    print(text)

res = [text[x] - 1 for x in range(1, len(text)) if text[x] - 1 != text[x - 1]]
print(res[0])

# вариант решение через zip
true_text = [x for x in range(1, len(text))]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(true_text)

new_list = list(zip(text, true_text))
print(new_list)

for item in new_list:
    if item[0] != item[1]:
        print(item[1])
        break
