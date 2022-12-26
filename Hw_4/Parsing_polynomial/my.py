path = 'polynomial_1.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


def encode(equation: str) -> dict:
    equation = equation.replace(' + ', ' ').replace(' - ', ' -')\
        .replace(' -x', ' -1*x').replace(' x', ' 1*x')\
        .replace('*x ', '*x**1 ').split()[:-2]
    dict_equation = {}
    for item in equation:
        i = item.split('*x**')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        else:
            dict_equation[int(0)] = int(i[0])

    return dict_equation
