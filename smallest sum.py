def solution(a):
    while not all_equal(a):
        i = 0
        k = 0
        while i < len(a) and not all_equal(a):
            while k < len(a):
                if a[i] < a[k]:
                    a[k] -= a[i]
                else:
                    k += 1
            i += 1
            k = 0
    return sum(a)


def all_equal(iterator):
    iterator = iter(iterator)

    try:
        first = next(iterator)
    except StopIteration:
        return True

    return all(first == x for x in iterator)


print(solution([319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865, 319865]))
