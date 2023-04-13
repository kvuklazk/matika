matrix = [[1, -2, 1, 0], [2, 1, -3, 5], [4, -7, 1, -1]]


def log_matrix(matrix_to_print: list = None):
    gap = 0
    # get length of biggest number
    for p in matrix_to_print:
        for x in p:
            if len(str(x)) > gap:
                gap = len(str(x))
    gap += 1
    line_length = gap * (len(matrix_to_print[0]) + 1) + 4 + 3

    print("-" * 3, " " * (line_length - 4), "-" * 3)
    for rowe in range(len(matrix_to_print)):
        print("|", end="")
        for columne in range(len(matrix_to_print[0]) - 1):
            print(" " * (gap - len(str(matrix_to_print[rowe][columne]))), matrix_to_print[rowe][columne], end="")
        print(" " * 2,
              "|",
              " " * (gap - len(str(matrix_to_print[rowe][-1]))),
              matrix_to_print[rowe][-1],
              " ",
              "|")
    print("-" * 3, " " * (line_length - 4), "-" * 3)


def change_rows_matrix(matrix_to_change_rows: list = None, row1: int = 0, row2: int = 0):
    change = matrix_to_change_rows[row1]
    matrix_to_change_rows[row1] = matrix_to_change_rows[row2]
    matrix_to_change_rows[row2] = change
    return matrix_to_change_rows


def log_solution_matrix(matrix):
    print("K = {[ ", end="")
    for i in range(len(matrix)):
        print(matrix[i][-1], end="")
        if i < len(matrix) - 1:
            print(", ", end="")
    print(" ]}")

    letters = ["q", "w", "z", "y", "x"]

    print("( ", end="")
    for i in range(-1, -len(matrix) - 1, -1):
        print(letters[i], end="")
        if i > -len(matrix):
            print(", ", end="")
    print(" ) = ", end="")
    print("( ", end="")
    for i in range(len(matrix)):
        print(matrix[i][-1], end="")
        if i < len(matrix) - 1:
            print(", ", end="")
    print(" )")


log_matrix(matrix)

# bottom triangle
# i - column that wants to be 0
for i in range(0, len(matrix) - 1):
    for row in range(i + 1, len(matrix)):
        if matrix[row][i] == 0:
            continue

        multiplier = matrix[row][i] / -matrix[i][i]

        for column in range(len(matrix[0])):
            matrix[row][column] = (multiplier * matrix[i][column]) + matrix[row][column]

            if matrix[row][column] == round(matrix[row][column]):
                matrix[row][column] = int(matrix[row][column])
        log_matrix(matrix)

# make the diagonal all ones
for row in range(-1, -len(matrix) - 1, -1):
    multiplier = 1 / matrix[row][row - 1]
    for column in range(len(matrix[row])):
        matrix[row][column] = matrix[row][column] * multiplier
        if matrix[row][column] == round(matrix[row][column]):
            matrix[row][column] = int(matrix[row][column])

log_matrix(matrix)

# top triangle
for i in range(-2, -len(matrix) - 1, -1):
    for row in range(i, -len(matrix) - 1, -1):
        if matrix[row][i] == 0:
            continue

        multiplier = matrix[row][i] / -matrix[i + 1][i]

        for column in range(len(matrix[0])):
            matrix[row][column] = (multiplier * matrix[i + 1][column]) + matrix[row][column]

            if matrix[row][column] == round(matrix[row][column]):
                matrix[row][column] = int(matrix[row][column])
        log_matrix(matrix)

log_solution_matrix(matrix)
