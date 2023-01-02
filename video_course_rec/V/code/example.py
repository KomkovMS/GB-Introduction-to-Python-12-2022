'''
В зависимости от параметра вызывать различные функции скрипта
Параметр ping -> функция выводит pong
2 параметра name <Имя> ->  функция приветствия пользователя
параметр list показать содержимое текущей директории

'''
import sys
import os


def ping():  # Параметр ping -> функция выводит pong
    print('pong')   # pong


# ping()


def hello(name):  # 2 параметра name <Имя> -> функция приветствия пользователя
    print('hello', name)    # hello Maxim


# hello('Maxim')


def get_info():  # параметр list показать содержимое текущей директории
    print(os.listdir())
# ['.git', 'Hw_1', 'Hw_2', 'Hw_3', 'Hw_4', 'lec_1', 'les_2', 'new_f',
# 'polynomial_1.txt', 'polynomial_2.txt', 'Sem_1', 'Sem_2', 'Sem_3', 'Sem_4',
# 'str_final.txt', 'video_course_rec', 'win32_1', 'win32_2', 'win32_3',
# 'win32_4', 'win32_5']


# get_info()


command = sys.argv[1]
if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)
