'''
В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
Найдите это число.

'''

# мое решение

path = 'C:/Python/Python_12.2022/Sem_5/file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos + 1:]
print(numbers)

result = 0

# for i in range(len(numbers)):
#     if i != numbers[i]:
#         result = i - 1

# или так
result = [numbers[x] -
          1 for x in range(1, len(numbers)) if numbers[x] - 1 != numbers[x - 1]]

print(result)
