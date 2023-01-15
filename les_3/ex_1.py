def sum(x):
    return x + 10


def mult(x):
    return x ** 2


print(sum(mult(2)))  # 14


def sum1(x):
    return x + 22


def mult2(x):
    return x ** 3


print(sum1(mult2(2)))  # 30


def sum3(x):
    return x + 242


def mult4(x):
    return x ** 5


print(sum3(mult4(2)))  # 274


def f(x):
    return x ** 2


g = f
print(type(f))  # <class 'function'>
print(f(1))  # 1
print(g(1))  # 1


def func(x):
    return x ** 2


print(func(2))  # 4
print(type(func))  # <class 'function'>


def calc(x):
    return x + 10


print(calc(10))  # 20


def calc1(x):
    return x * 10


print(calc1(10))  # 100


def math(op, x):
    print(op(x))


math(calc1, 10)     # 100
math(calc, 10)      # 20
