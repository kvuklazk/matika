from tkinter import *


def destroy_all(win):
    for widget in win.winfo_children():
        widget.destroy()


class MyWindow:
    def __init__(self, win):
        self.win = win

        # self.row = 0
        # self.column = 0
        self.len = 0
        self.text_widgets = []

        # self.lbl_row = Label(win, text='Number of rows:')
        # self.lbl_column = Label(win, text='Number of columns:')
        self.lbl_len = Label(win, text='Height of matrix:')
        # self.e_row = Entry(win)
        # self.e_column = Entry(win)
        self.e_len = Entry(win)
        self.enter = Button(win, text='Enter', command=self.enter_row_column)

        # self.lbl_row.grid(row=0, column=0)
        # self.lbl_column.grid(row=1, column=0)
        self.lbl_len.grid(row=0, column=0)
        self.enter.grid(row=3, column=1)
        self.e_len.grid(row=0, column=1)

        # self.e_row.grid(row=0, column=1)
        # self.e_column.grid(row=1, column=1)

        lbl_inst = Label(self.win, text='Enter matrix (one entry - one number):')

    def enter_row_column(self):
        # self.row = int(self.e_row.get())
        # self.column = int(self.e_column.get())
        self.len = int(self.e_len.get())
        destroy_all(self.win)

        lbl_inst = Label(self.win, text='Enter matrix (one entry - one number):')
        lbl_inst.grid(row=0, column=0, columnspan=self.len+1)

        self.text_widgets = self.create_e_for_matrix(self.len, self.len)

        self.enter = Button(self.win, text='Enter', command=self.enter_matrix)
        self.enter.grid(row=self.len+1, column=0, columnspan=self.len+1)

    def enter_matrix(self):
        matrix = []
        for row in range(self.len):
            matrix.append([])
            for column in range(self.len):
                matrix[row].append(self.text_widgets[row][column].get())
        print(matrix)

    def create_e_for_matrix(self, row, column):
        text_widgets = []
        for row in range(row):
            text_widgets.append([])
            for column in range(column+1):
                e = Entry(self.win, width=15)
                if column == self.len:
                    e.grid(row=row + 1, column=column, padx=6, pady=2)
                    text_widgets[row].append(e)
                else:
                    e.grid(row=row+1, column=column, padx=2, pady=2)
                    text_widgets[row].append(e)
        return text_widgets


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
