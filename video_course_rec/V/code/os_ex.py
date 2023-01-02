import os

# Имя операционной системы
print(os.name)  # nt

# текущая рабочая директория
print(os.getcwd())  # C:\Python\Python_12.2022

# создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_f')

# создаем папку по новому пути
os.mkdir(new_path)
