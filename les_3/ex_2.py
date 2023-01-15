# def sum(x, y):
#     return x + y

# тоже самое, что и:
def sum(x, y): return x + y


def mult(x, y):
    return x * y


def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)


calc(sum, 4, 5)  # 9

calc(lambda x, y: x + y, 6, 7)  # 13
calc(lambda x, y: x + y, 9, 8)  # 13
