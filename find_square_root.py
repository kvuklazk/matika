def find_square_root(n: int = 0, n_square_root: int = 0):
    if (n_square_root+1) * (n_square_root+1) > n:
        if n_square_root * n_square_root == n:
            return n_square_root
        return "≈", n_square_root
    n_square_root += 1
    return find_square_root(n, n_square_root)


def print_tuple(tuple_to_print: tuple = None):
    for i in range(len(tuple_to_print)):
        print(tuple_to_print[i], end='')
    return ""


inp = int(input())
if type(find_square_root(inp)) != int:
    print(print_tuple(find_square_root(inp)))
else:
    print(find_square_root(inp))
