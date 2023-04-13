matrix = [[1, -1, 2], [2, 0, 3], [0, 1, -1]]
matrix1 = []
for row in range(len(matrix)):
    matrix1.append([])
    for column in range(len(matrix)):
        if row == column:
            matrix1[row].append(1)
        else:
            matrix1[row].append(0)

def log_matrix(matrix_to_print: list = None):
    gap = 0
    # get length of biggest number
    for p in matrix_to_print:
        for x in p:
            if len(str(x)) > gap:
                gap = len(str(x))
    gap += 1
    line_length = gap * (len(matrix_to_print[0]) + 1) + 4 + 3

    print("-" * 3, " " * (line_length - 6), "-" * 3)
    for rowe in range(len(matrix_to_print)):
        print("|", end="")
        for columne in range(len(matrix_to_print[0])-3):
            print(" " * (gap-len(str(matrix_to_print[rowe][columne]))), matrix_to_print[rowe][columne], end="")
        print("  |", end="")
        for columne in range(-3, 0):
            print(" " * (gap-len(str(matrix_to_print[rowe][columne]))), matrix_to_print[rowe][columne], end="")
        print(" |")
    print("-" * 3, " " * (line_length - 6), "-" * 3)


for row in range(len(matrix1)):
    for column in range(len(matrix1[row])):
        matrix[row].append(matrix1[row][column])


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

print("diagonal")

# make the diagonal all ones
for row in range(0, len(matrix)):
    multiplier = 1 / matrix[row][row]
    for column in range(len(matrix[row])):
        matrix[row][column] = matrix[row][column] * multiplier
        if matrix[row][column] == round(matrix[row][column]):
            matrix[row][column] = int(matrix[row][column])

log_matrix(matrix)

print("top triangle")
# top triangle
for i in range(-4, -len(matrix[0]), -1):
    for row in range(i+2, -len(matrix)- 1, -1):
        if matrix[row][i] == 0:
            continue

        multiplier = matrix[row][i] / -matrix[i+3][i]
        for column in range(len(matrix[0])):
            matrix[row][column] = (multiplier * matrix[i+3][column]) + matrix[row][column]

            if matrix[row][column] == round(matrix[row][column]):
                matrix[row][column] = int(matrix[row][column])

        log_matrix(matrix)


