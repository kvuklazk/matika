import tkinter as tk


class App:
    def __init__(self, cells, generations):
        # upravujou se vsechny tyhle listy ne jenom self.cells_temporary
        self.cells = cells
        self.temporary_cells = cells
        self.origin_cells = cells
        self.generations = generations

        self.master = tk.Tk()
        self.master.title("game of life")

        self.width = len(self.cells[0])
        self.height = len(self.cells)
        self.size = 50
        self.padding = 10

        self.canvas = tk.Canvas(self.master,
                                width=self.width * self.size,
                                height=self.height * self.size)
        self.canvas.pack()

        self.shapes = []
        for i in range(self.height):
            self.shapes.append([])
            for x in range(self.width):
                self.shapes[i].append(0)

        self.draw_scene()

        self.button = tk.Button(self.master, text="Next gen", command=lambda: self.life())
        self.button.pack()

        self.beginn_button = tk.Button(self.master, text="Again", command=self.beginn).pack()

        self.directions = [[0, 1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]


    def beginn(self):
        print("a", self.cells, self.origin_cells)
        self.cells = [x for x in self.origin_cells]
        self.draw_scene()

    def draw_scene(self, size=50):
        for y, row in zip(range(self.height), self.cells):
            for x, human in zip(range(self.width), row):
                self.canvas.create_rectangle(x * size, y * size, (x + 1) * size, (y + 1) * size, width=2)
                if human:
                    self.draw_circle(x, y)
                else:
                    self.draw_cross(x, y)

    def draw_circle(self, x, y):
        self.delete_object(x, y)
        self.shapes[y][x] = (self.canvas.create_oval(x * self.size + self.padding,
                                                     y * self.size + self.padding,
                                                     (x + 1) * self.size - self.padding,
                                                     (y + 1) * self.size - self.padding,
                                                     fill="green"))

    def draw_cross(self, x, y):
        self.delete_object(x, y)
        self.shapes[y][x] = [self.canvas.create_line(x * self.size + self.padding,
                                                     y * self.size + self.padding,
                                                     (x + 1) * self.size - self.padding,
                                                     (y + 1) * self.size - self.padding),
                             self.canvas.create_line((x + 1) * self.size - self.padding,
                                                     y * self.size + self.padding,
                                                     x * self.size + self.padding,
                                                     (y + 1) * self.size - self.padding)]

    def delete_object(self, x, y):
        if self.shapes[y][x]:
            if type(self.shapes[y][x]) == int:
                self.canvas.delete(self.shapes[y][x])
            else:
                for i in self.shapes[y][x]:
                    self.canvas.delete(i)

    def life(self):
        """
        Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
        Any live cell with more than three live neighbours dies, as if by overcrowding.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any dead cell with exactly three live neighbours becomes a live cell.
        """
        for i, y in enumerate(self.cells):
            for x, cell in enumerate(y):
                print(x, i, self.cells)
                if cell:
                    print("cell is one")
                    if not 2 <= self.get_neighbours(x, i) <= 3:
                        print("dies")
                        self.temporary_cells[i][x] = 0
                    else:
                        print("lives")
                if not cell:
                    print("cell is zero")
                    if self.get_neighbours(x, i) == 3:
                        self.temporary_cells[i][x] = 1

        self.cells = self.temporary_cells

        self.draw_scene()

    def get_neighbours(self, x, y):
        neighbours = []
        for direction in self.directions:
            if len(self.cells) > y + direction[1] >= 0 and len(self.cells[0]) > x + direction[0] >= 0:
                neighbours.append(self.cells[y + direction[1]][x + direction[0]])
        return sum(neighbours)


a = App([[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]], 1)
a.master.mainloop()
