def valid_solution(board):
    board_flipped = []
    for i in range(9):
        board_flipped.append([])
        for k in range(9):
            board_flipped[i].append(board[k][i])
    board_cells = []
    for column_square in range(0, 9, 3):
        for row_square in range(0, 9, 3):
            board_cells.append([])
            for row in range(3):
                for column in range(3):
                    board_cells[-1].append(board[row_square+row][column_square+column])
    for i in [board, board_flipped, board_cells]:
        for k in i:
            print(k[:3], end="")
            print(" "*3, end="")
            print(k[3:6], end="")
            print(" "*3, end="")
            print(k[6:9])
            if (i.index(k)) % 3 == 2:
                print(" "*3)
        print("x"*50)
    for b in [board, board_flipped, board_cells]:
        for i in b:
            if len(set(i)) != 9 or sum(i) != 45:
                return False
    return True


print(valid_solution([
  [5, 3, 4,    6, 7, 8,    9, 1, 2],
  [6, 7, 2,    1, 9, 0,    3, 4, 8],
  [1, 0, 0,    3, 4, 2,    5, 6, 0],

  [8, 5, 9,    7, 6, 1,    0, 2, 0],
  [4, 2, 6,    8, 5, 3,    7, 9, 1],
  [7, 1, 3,    9, 2, 4,    8, 5, 6],

  [9, 0, 1,    5, 3, 7,    2, 1, 4],
  [2, 8, 7,    4, 1, 9,    6, 3, 5],
  [3, 0, 0,    4, 8, 1,    1, 7, 9]
]))