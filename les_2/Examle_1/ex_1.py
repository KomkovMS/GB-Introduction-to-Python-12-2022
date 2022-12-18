colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')  # его не существует он будет создан
data.writelines(colors)  # разделителей не будет
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
