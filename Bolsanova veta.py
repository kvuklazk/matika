from math import pi, cos, sin, log, log10, e, tan

accuracy = 0.000000001


def line_from_two_points(a, b, func):
    result = a + (b-a) / (abs(func(a))+abs(func(b))) * abs(func(a))
    return result


def approx(a, b, func, n=1):
    fa = func(a)
    fb = func(b)

    if abs(fa)-abs(fb) > 9999999999999:
        return f"function doesn't have a root between {a} and {b}, it's not defined"

    if fa * fb > 0:
        return "Invalid approx Input; f(a) * f(b) > 0)"

    if fa < fb:
        fa, fb = fb, fa
        a, b = b, a

    # print(f"a = {a}, f(a) = {fa}, b = {b}, f(b) = {fb}, n = {n}")

    middle = line_from_two_points(a, b, func)
    # middle = (a + b) / 2
    # print(f"middle = {middle}")

    if type(func(middle)) is str:
        return f"function is not defined in {middle}, approx"

    if abs(func(middle)) < accuracy:
        return middle, n

    if func(middle) > 0:
        a = middle
    else:
        b = middle

    return approx(a, b, func, n+1)


def parse_func(eq: str):
    eq.replace(" ", "")
    print(eq)
    eq = eq[eq.find("=")+1:]

    def f(x):
        try:
            return eval(eq)
        except ValueError:
            return f"function not defined in {x}"
        except ZeroDivisionError:
            return f"function not defined in {x}"

    return f


def find_root(eq: str = None, start=-10.0, end=10, step=0.75):
    if not eq:
        return "Invalid input"

    f = parse_func(eq)

    x = start
    y_now = 0

    roots = []
    while x < end:
        x = round(x, 2)
        y_last = y_now
        if type(f(x)) is str:
            print(f(x))
            x += step
            continue
        if type(f(x-step)) is str:
            print(f(x-step))
            x += step
            continue
        y_now = f(x)
        print(f"y_last = {y_last}, y_now = {y_now}, x = {x}")
        if y_now == 0:
            roots.append(x)
            x += step
            continue
        if y_now * y_last < 0:
            approximation = approx(x, x-step, f)
            if type(approximation) is str:
                print(approximation)
            else:
                roots.append(approximation[0])
        x += step

    for i in roots:
        yield i


print("Enter function as following: y= ... or f(x)= ...")

gen = find_root("f(x)=tan(x) * log(10,x * x) * x", step=0.1)
first = gen.__next__()
print()
print(f"roots: {first}", end="")
for value in gen:
    print(value, end=", ")
print

