import tkinter as tk
from math import floor


class App:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Algorithms")

        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()

        self.dimension = 20
        self.cubes = []

        self.list_cubes = [
            [[[0, 1, 0], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0]]],
            [[[0, 1, 1], [1, 0, 0, 0, 0], [1, 0, 1, 0, 1], [1, 0, 0, 0, 0], [0, 1, 1]]],
            [[[1, 0, 1], [0, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 1, 0], [0, 1, 0]]],
            [[[0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 0, 0, 1], [1, 1, 0]]],
            [[[1, 1, 0], [0, 0, 0, 0, 1], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0], [0, 0, 0]]],
            [[[0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 1]], "R2 D (R' U2 R) D' (R' U2 R')"],
            [[[1, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 0], [1, 0, 0]]]
        ]

        self.buttons = []
        self.solution_text = []

        for a, i in enumerate(self.list_cubes):
            self.make_cube(self.my_func(a)*100+100, floor(a/4)*100+100, i[0])
            self.buttons.append(tk.Button(self.canvas,
                                          width=int(self.dimension/2),
                                          text="Solution",
                                          command=lambda m=a: self.show_solution(m)))
            self.canvas.create_window(self.my_func(a)*100+100, floor(a/4)*100+100+self.dimension*2.5,
                                      window=self.buttons[-1])
            self.solution_text.append([0, 0])

    @staticmethod
    def my_func(x):
        print(x)
        if x % 4 < 3:
            return x % 4
        else:
            return 12 - (x % 4) * 3

    def show_solution(self, num):
        if self.buttons[num]["text"] == "Solution":
            self.buttons[num]["text"] = "Hide sol"
            self.solution_text[num][0] = self.canvas.create_text(self.my_func(num)*100+100, floor(num/4)*100+100,
                                                                 text=str(self.list_cubes[num][-1]))
            self.solution_text[num][1] = self.canvas.create_rectangle(self.canvas.bbox(self.solution_text[num][0]),
                                                                      fill="white")
            self.canvas.tag_lower(self.solution_text[num][1], self.solution_text[num][0])
        else:
            self.buttons[num]["text"] = "Solution"
            for i in self.solution_text[num]:
                self.canvas.delete(i)

    def make_cube(self, x, y, yellow):
        """
        :param x: x coordinate
        :param y: y coordinate
        coord are the center of the cube
        :param yellow: list of yellow tiles on cube
                        [[top], [first row including sides], [second row], [third row], [bottom]]
        :return: None
        """

        self.cubes.append([])

        top_left = (x - self.dimension*1.5, y - self.dimension*1.5)

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_left[0], top_left[1],
                top_left[0] + self.dimension / 4, top_left[1] - self.dimension / 3,
                top_left[0] + self.dimension, top_left[1] - self.dimension / 3,
                top_left[0] + self.dimension, top_left[1],
                fill="grey", width="2", outline="black"))

        if yellow[0][0]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_left[0] + self.dimension, top_left[1],
                top_left[0] + self.dimension, top_left[1] - self.dimension / 3,
                top_left[0] + self.dimension * 2, top_left[1] - self.dimension / 3,
                top_left[0] + self.dimension * 2, top_left[1],
                fill="grey", width="2", outline="black"))

        if yellow[0][1]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_left[0] + self.dimension * 2, top_left[1],
                top_left[0] + self.dimension * 2, top_left[1] - self.dimension / 3,
                top_left[0] + self.dimension * 3 - self.dimension / 4, top_left[1] - self.dimension / 3,
                top_left[0] + self.dimension * 3, top_left[1],
                fill="grey", width="2", outline="black"))

        if yellow[0][2]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        for row in range(1, 4):
            for tile in range(1, 4):
                self.cubes[-1].append(
                    self.canvas.create_rectangle(
                                                top_left[0]+((tile-1)*self.dimension),
                                                top_left[1]+((row-1)*self.dimension),
                                                top_left[0] + (tile * self.dimension),
                                                top_left[1]+(row*self.dimension),
                                                fill="grey", width="2", outline="black")
                )
                if yellow[row][tile]:
                    self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        bottom_left = (x-self.dimension*1.5, y+self.dimension*1.5)

        self.cubes[-1].append(
            self.canvas.create_polygon(
                bottom_left[0], bottom_left[1],
                bottom_left[0] + self.dimension / 4, bottom_left[1] + self.dimension / 3,
                bottom_left[0] + self.dimension, bottom_left[1] + self.dimension / 3,
                bottom_left[0] + self.dimension, bottom_left[1],
                fill="grey", width="2", outline="black"))

        if yellow[-1][0]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                bottom_left[0] + self.dimension, bottom_left[1],
                bottom_left[0] + self.dimension, bottom_left[1] + self.dimension / 3,
                bottom_left[0] + self.dimension * 2, bottom_left[1] + self.dimension / 3,
                bottom_left[0] + self.dimension * 2, bottom_left[1],
                fill="grey", width="2", outline="black"))

        if yellow[-1][1]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                bottom_left[0] + self.dimension * 2, bottom_left[1],
                bottom_left[0] + self.dimension * 2, bottom_left[1] + self.dimension / 3,
                bottom_left[0] + self.dimension * 3 - self.dimension / 4, bottom_left[1] + self.dimension / 3,
                bottom_left[0] + self.dimension * 3, bottom_left[1],
                fill="grey", width="2", outline="black"))

        if yellow[-1][2]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_left[0], top_left[1],
                top_left[0] - self.dimension/3, top_left[1] + self.dimension / 4,
                top_left[0] - self.dimension/3, top_left[1] + self.dimension,
                top_left[0], top_left[1] + self.dimension,
                fill="grey", width="2", outline="black"))

        if yellow[1][0]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_left[0], top_left[1] + self.dimension,
                top_left[0] - self.dimension / 3, top_left[1] + self.dimension,
                top_left[0] - self.dimension / 3, top_left[1] + self.dimension + self.dimension,
                top_left[0], top_left[1] + self.dimension + self.dimension,
                fill="grey", width="2", outline="black"))

        if yellow[2][0]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_left[0], top_left[1] + self.dimension*2,
                top_left[0] - self.dimension / 3, top_left[1] + self.dimension*2,
                top_left[0] - self.dimension / 3, top_left[1] + self.dimension - self.dimension/4 + self.dimension*2,
                top_left[0], top_left[1] + self.dimension + self.dimension*2,
                fill="grey", width="2", outline="black"))

        if yellow[3][0]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        top_right = (x + self.dimension*1.5, top_left[1])

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_right[0], top_right[1],
                top_right[0] + self.dimension / 3, top_right[1] + self.dimension / 4,
                top_right[0] + self.dimension / 3, top_right[1] + self.dimension,
                top_right[0], top_right[1] + self.dimension,
                fill="grey", width="2", outline="black"))

        if yellow[1][-1]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_right[0], top_right[1] + self.dimension,
                top_right[0] + self.dimension / 3, top_right[1] + self.dimension,
                top_right[0] + self.dimension / 3, top_right[1] + self.dimension + self.dimension,
                top_right[0], top_right[1] + self.dimension + self.dimension,
                fill="grey", width="2", outline="black"))

        if yellow[2][-1]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")

        self.cubes[-1].append(
            self.canvas.create_polygon(
                top_right[0], top_right[1] + self.dimension * 2,
                top_right[0] + self.dimension / 3, top_right[1] + self.dimension * 2,

                top_right[0] + self.dimension / 3,
                top_right[1] + self.dimension - self.dimension / 4 + self.dimension * 2,

                top_right[0], top_right[1] + self.dimension + self.dimension * 2,
                fill="grey", width="2", outline="black"))

        if yellow[3][-1]:
            self.canvas.itemconfig(self.cubes[-1][-1], fill="yellow")


app = App()
app.master.mainloop()
