import re


def time_correct(t):
    if not t or not re.search(r"^\d\d:\d\d:\d\d$", t):
        return t

    t = [int(i) for i in t.split(":")]
    while t[2] > 59:
        t[2] -= 60
        t[1] += 1
    while t[1] > 59:
        t[1] -= 60
        t[0] += 1
    while t[0] > 23:
        t[0] -= 24

    return ":".join([str(i).zfill(2) for i in t])


print(time_correct("50:99:99"))
