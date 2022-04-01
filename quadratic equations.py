from math import sqrt


def quadratic_root(equation: str = ""):
    equation = equation.replace(" ", "")
    equal_index = equation.index("=")
    for i in range(equal_index, len(equation)):
        if equation[i] == "0":
            equation = equation[0: i:] + equation[i + 1::]
    equation = equation.replace("=", "")
    equation = equation.replace("²", "^2")
    a = 1
    b = 1
    c = 1
    if equation == "":
        pass
    k = 0
    if equation[k] == "-":
        a = -1
        k += 1
    if equation[k].isnumeric():
        if equation[k+1].isnumeric():
            a = a * int(equation[k] + equation[k+1])
            k += 2
        else:
            a = a * int(equation[k])
            k += 1
    k += 3
    if equation[k] == "-":
        b = -1

    k += 1
    if equation[k].isnumeric():
        if equation[k + 1].isnumeric():
            b = b * int(equation[k] + equation[k+1])
            k += 3
        else:
            b = b * int(equation[k])
            k += 2
    else:
        k += 1

    if equation[k] == "-":
        c = -1
    k += 1
    if k != len(equation)-1:
        c = c * int(equation[k] + equation[k+1])
    else:
        c = c * int(equation[k])
    discriminant = b*b-(4*a*c)

    if b*b-4*a*c > 0:
        if 2*a != 0:
            x1 = ((b*-1)+sqrt(discriminant))/(2*a)
            x2 = ((b*-1)-sqrt(discriminant))/(2*a)
            return x1, x2
        else:
            return "2*a is 0"
    else:
        return "Discriminant is negative"


print(quadratic_root(input("Enter equation: ")))
# print(quadratic_root("x² -x -89 = 0"))
