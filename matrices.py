from tkinter import *

# matrix = [[1, -2, 1, 0], [2, 1, -3, 5], [4, -7, 1, -1]]


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
        for columne in range(len(matrix_to_print[0])-1):
            print(" " * (gap-len(str(matrix_to_print[rowe][columne]))), matrix_to_print[rowe][columne], end="")
        print(" " * 2,
              "|",
              " " * (gap-len(str(matrix_to_print[rowe][-1]))),
              matrix_to_print[rowe][-1],
              " ",
              "|")
    print("-" * 3, " " * (line_length - 6), "-" * 3)


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
    for i in range(-1, -len(matrix)-1, -1):
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


def destroy_all(win):
    for widget in win.winfo_children():
        widget.destroy()


def validate_int(action, index, value_if_allowed,
             prior_value, text, validation_type, trigger_type, widget_name):
    if value_if_allowed:
        if len(value_if_allowed) == 1 and value_if_allowed == "-":
            return True
        else:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
    else:
        return False


def validate_float(action, index, value_if_allowed,
             prior_value, text, validation_type, trigger_type, widget_name):
    if value_if_allowed:
        if len(value_if_allowed) == 0:
            return True
        if len(value_if_allowed) == 1 and value_if_allowed == "-":
            return True
        else:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
    else:
        return False


class MatCalc:
    def __init__(self, win):
        self.win = win

        self.column = 0
        self.grid_size = 30

        # self.row = 0
        # self.column = 0
        self.len = 0
        self.text_widgets = []
        self.matrix = []
        self.mode = 'Menu'

        self.start()

        self.e_len = Entry(self.win)

    def start(self, action=None):
        destroy_all(self.win)
        lbl = Label(self.win, text='Choose option')
        lbl.grid(row=0, column=0, columnspan=2)

        gaus_btn = Button(self.win, text="Gaussian elimination - g", command=lambda: self.entered_choise('g'))
        gaus_btn.grid(row=1, column=0)

        inverse_btn = Button(self.win, text="Inverse matrix - i", command=lambda: self.entered_choise('i'))
        inverse_btn.grid(row=1, column=1)

        self.win.bind('<g>', self.entered_choise) and self.win.bind('<i>', self.entered_choise)

    def entered_choise(self, action=None):
        if action.char == 'i' or action == 'i':
            self.mode = 'Inverse'
            self.row_col()
        elif action.char == 'g' or action == 'g':
            self.mode = 'Gaus'
            self.row_col()

    def row_col(self, action=None):
        destroy_all(self.win)
        # self.lbl_row = Label(win, text='Number of rows:')
        # self.lbl_column = Label(win, text='Number of columns:')
        lbl_len = Label(self.win, text='Height of matrix:')
        # self.e_row = Entry(win)
        # self.e_column = Entry(win)
        vcmd = (self.win.register(validate_int),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.e_len = Entry(self.win, validate='key', validatecommand=vcmd)
        enter = Button(self.win, text='Enter', command=self.entered_row_column)

        # self.lbl_row.grid(row=0, column=0)
        # self.lbl_column.grid(row=1, column=0)
        lbl_len.grid(row=0, column=0)
        enter.grid(row=3, column=1)
        self.e_len.grid(row=0, column=1)
        self.e_len.focus_set()

        # self.e_row.grid(row=0, column=1)
        # self.e_column.grid(row=1, column=1)
        self.win.bind('<Return>', self.entered_row_column)

    def entered_row_column(self, action):
        # self.row = int(self.e_row.get())
        # self.column = int(self.e_column.get())
        self.len = int(self.e_len.get())
        destroy_all(self.win)

        lbl_inst = Label(self.win, text='Enter matrix (one entry - one number):')
        lbl_inst.grid(row=0, column=0, columnspan=self.len+1)

        self.text_widgets = self.create_e_for_matrix(self.len, self.len)

        e = Button(self.win, text='Enter', command=self.entered_matrix)
        e.grid(row=self.len+1, column=0, columnspan=self.len+1)
        self.win.bind('<Return>', lambda event: self.entered_matrix())

    def entered_matrix(self):
        self.win.bind('<m>', self.start)
        self.matrix = []
        for row in range(self.len):
            self.matrix.append([])
            for column in range(self.len+1):
                try:
                    self.matrix[row].append(int(self.text_widgets[row][column].get()))
                except ValueError:
                    self.matrix[row].append(float(self.text_widgets[row][column].get()))
        destroy_all(self.win)
        self.text_widgets = []
        self.column = 0
        if self.mode == 'Gaus':
            self.win.bind('<g>', self.entered_choise)
            self.matrix = self.solve_matrix(self.matrix)
            solution = ""
            for i in range(len(self.matrix)):
                solution += str(self.matrix[i][-1])
                if i < len(self.matrix)-1:
                    solution += ', '
            labl = Label(self.win, text='K = {[ %s ]}' % solution)
            labl.place(x=self.grid_size, y=self.grid_size*(4+len(self.matrix)))
        elif self.mode == 'Inverse':
            self.matrix = self.inverse_matrix()
            self.print_matrix_add(self.matrix)

        gaussian_again = Button(self.win, text='Gaussian again - g', command=lambda: self.entered_choise('g'))
        gaussian_again.place(x=self.grid_size, y=self.grid_size*(5+len(self.matrix)))

        return_to_start = Button(self.win, text='Menu - m', command=self.start)
        return_to_start.place(x=self.grid_size, y=self.grid_size*(6+len(self.matrix)))

    def print_matrix_add(self, matrix):
        lbl = Label(self.win, text='----')
        lbl.place(x=self.column*self.grid_size, y=0)
        lbl = Label(self.win, text='----')
        lbl.place(x=(self.column+len(matrix[0])+1)*self.grid_size-len('----')*4, y=0)

        for row in range(1, len(matrix)+1):
            lbl = Label(self.win, text='|')
            lbl.place(x=self.column*self.grid_size, y=row*self.grid_size)

            lbl = Label(self.win, text='|')
            lbl.place(x=(self.column+len(matrix[0])+1)*self.grid_size, y=row*self.grid_size+1)

        lbl = Label(self.win, text='----')
        lbl.place(x=self.column * self.grid_size, y=(len(matrix)+2)*self.grid_size)
        lbl = Label(self.win, text='----')
        lbl.place(x=(self.column + len(matrix[0])+1) * self.grid_size-len('----')*4, y=(len(matrix)+2)*self.grid_size)

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                lbl = Label(self.win, text=matrix[row][column])
                lbl.place(x=(self.column+1+column)*self.grid_size, y=(1+row)*self.grid_size)

        self.column = self.column + len(matrix[0]) + 2

    def create_e_for_matrix(self, row, column):
        text_widgets = []
        for row in range(row):
            text_widgets.append([])
            for column in range(column+1):
                vcmd = (self.win.register(validate_float),
                        '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
                e = Entry(self.win, width=15, validate='key', validatecommand=vcmd)
                if column == self.len:
                    e.grid(row=row + 1, column=column, padx=6, pady=2)
                    text_widgets[row].append(e)
                else:
                    e.grid(row=row+1, column=column, padx=2, pady=2)
                    text_widgets[row].append(e)
        text_widgets[0][0].focus_set()
        return text_widgets

    def solve_matrix(self, matrix):

        self.print_matrix_add(matrix)

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
                self.print_matrix_add(matrix)
                if row != len(matrix)-1:
                    number_0s = 0
                    for i in matrix[row][:len(matrix)+1]:
                        print(type(row), type(len(matrix)+1))
                        if matrix[row][i] == 0:
                            number_0s += 1
                    number_0s2 = 0
                    for i in matrix[row+1][:len(matrix)]:
                        if matrix[row+1][i] == 0:
                            number_0s += 1
                    if number_0s>number_0s2:
                        change_rows_matrix(matrix, row, row+1)

        # make the diagonal all ones
        for row in range(0, len(matrix)):
            multiplier = 1 / matrix[row][row]
            for column in range(len(matrix[row])):
                matrix[row][column] = matrix[row][column] * multiplier
                if matrix[row][column] == round(matrix[row][column]):
                    matrix[row][column] = int(matrix[row][column])

        self.print_matrix_add(matrix)

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
                self.print_matrix_add(matrix)

        return matrix

    def inverse_matrix(self, matrix):
        return matrix


window = Tk()
my_win = MatCalc(window)
window.title('Matrix Calculator')
window.iconbitmap('C:\dev\Pycharm\matika\drawing.ico')
window.geometry("700x700")
window.mainloop()
