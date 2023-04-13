from random import randint
from tkinter import *
from math import floor


class App:
    def __init__(self):
        self.okno = Tk()
        self.okno.title("Mega dobry okno")
        self.width = self.okno.winfo_screenwidth() - 100
        self.height = self.okno.winfo_screenheight() - 100
        self.okno.geometry("%dx%d" % (self.width, self.height))

        self.platno = Canvas(height=self.height, width=self.width)
        self.platno.pack()

        self.velikost_pole = 25  # 100x100
        self.pocet_min = 2

        self.pole = []
        for i in range(self.velikost_pole):
            self.pole.append([0] * self.velikost_pole)

        print(self.pole)

        miny = self.pocet_min
        while miny > 0:
            x = randint(0, self.velikost_pole - 1)
            y = randint(0, self.velikost_pole - 1)
            if self.pole[y][x] != 1:
                self.pole[y][x] = 1
                miny -= 1

        self.velikost_policka = floor(self.height / self.velikost_pole)
        self.top = (self.height - self.velikost_policka * self.velikost_pole) / 2
        self.bottom = self.top + self.velikost_pole * self.velikost_policka
        self.left = self.width / 2 - self.velikost_policka * self.velikost_pole / 2
        self.right = self.width / 2 + self.velikost_policka * self.velikost_pole / 2

        self.platno.create_rectangle(self.left, self.top, self.right, self.bottom)

        for i in range(1, self.velikost_pole):
            self.platno.create_line(self.left + i * self.velikost_policka, self.top,
                                    self.left + i * self.velikost_policka, self.bottom)
            self.platno.create_line(self.left, self.top + i * self.velikost_policka, self.right,
                                    self.top + i * self.velikost_policka)

        self.pocet_oznacenych_min = 0

        self.okno.bind("<Button-1>", self.napravyklik)
        self.okno.bind("<Button-3>", self.nalevyklik)

    def nalevyklik(self, event):
        x = floor((event.x - self.left) / self.velikost_policka)
        y = floor((event.y - self.top) / self.velikost_policka)
        if not self.velikost_pole > x >= 0 and self.velikost_pole > y >= 0:
            return
        self.nakresli_vlajecku(x, y)
        if self.vyhral_jsi_otazka():
            self.vyhra()
            return

    def nakresli_vlajecku(self, x, y):
        x = self.preved_souradnice_x(x)
        y = self.preved_souradnice_y(y)

        self.platno.create_line(x+self.velikost_policka/2, y + self.velikost_policka * 9/12,
                                x+self.velikost_policka/2, y + self.velikost_policka * 2/12)
        self.platno.create_polygon(x+self.velikost_policka/2, y + self.velikost_policka * 2/12,
                                   x+self.velikost_policka/2 + self.velikost_policka * 4.5/12, y + self.velikost_policka * 4/12,
                                   x+self.velikost_policka/2, y + self.velikost_policka * 1/2, fill="green")
        self.pocet_oznacenych_min += 1

    def vyhral_jsi_otazka(self):
        for y in self.pole:
            for x in y:
                if not (x == 1 or x == 2):
                    return False
        if self.pocet_oznacenych_min == self.pocet_min:
            return True
        return False

    def napravyklik(self, event):
        x = floor((event.x - self.left) / self.velikost_policka)
        y = floor((event.y - self.top) / self.velikost_policka)
        if not self.velikost_pole > x >= 0 and self.velikost_pole > y >= 0:
            return


        self.nakresli_veshny_miny()
        if self.pole[y][x] == 1:
            self.end()
            return
        self.odkryj(x, y)
        if self.vyhral_jsi_otazka():
            self.vyhra()
            return

    def preved_souradnice_x(self, x):
        return self.left + self.velikost_policka * x

    def preved_souradnice_y(self, y):
        return self.top + self.velikost_policka * y

    def odkryj(self, x, y):
        self.nakresli_cislo(x, y, self.pocet_min_okolo_policka(x, y))
        if self.pocet_min_okolo_policka(x, y) == 0:
            kontrola = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
            to_be_removed = []
            if x == 0:
                to_be_removed.append([-1, -1])
                kontrola.remove([-1, 0])
                to_be_removed.append([-1, 1])
            if x == self.velikost_pole - 1:
                to_be_removed.append([1, -1])
                to_be_removed.append([1, 0])
                to_be_removed.append([1, 1])
            if y == 0:
                to_be_removed.append([-1, -1])
                to_be_removed.append([0, -1])
                to_be_removed.append([1, -1])
            if y == self.velikost_pole - 1:
                to_be_removed.append([-1, 1])
                to_be_removed.append([0, 1])
                to_be_removed.append([1, 1])

            for i in to_be_removed:
                if i in kontrola:
                    kontrola.remove(i)

            for i in kontrola:
                x_1 = x + i[0]
                y_1 = y + i[1]
                if not self.pole[y_1][x_1] == 2:
                    if self.pocet_min_okolo_policka(x_1, y_1) == 0:
                        self.odkryj(x_1, y_1)
                    else:
                        if not self.pole[y_1][x_1] == 1:
                            self.nakresli_cislo(x_1, y_1, self.pocet_min_okolo_policka(x_1, y_1))

    def pocet_min_okolo_policka(self, x, y):
        pocet = 0
        kontrola = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
        to_be_removed = []
        if x == 0:
            to_be_removed.append([-1, -1])
            kontrola.remove([-1, 0])
            to_be_removed.append([-1, 1])
        if x == self.velikost_pole-1:
            to_be_removed.append([1, -1])
            to_be_removed.append([1, 0])
            to_be_removed.append([1, 1])
        if y == 0:
            to_be_removed.append([-1, -1])
            to_be_removed.append([0, -1])
            to_be_removed.append([1, -1])
        if y == self.velikost_pole-1:
            to_be_removed.append([-1, 1])
            to_be_removed.append([0, 1])
            to_be_removed.append([1, 1])

        for i in to_be_removed:
            if i in kontrola:
                kontrola.remove(i)

        for i in kontrola:
            if self.pole[y+i[1]][x+i[0]] == 1:
                pocet += 1
        return pocet

    def nakresli_veshny_miny(self):
        for y in range(self.velikost_pole):
            for x in range(self.velikost_pole):
                if self.pole[y][x] == 1:
                    self.platno.create_oval(
                        self.left + x * self.velikost_policka + self.velikost_policka / 2 - self.velikost_policka / 4,
                        self.top + y * self.velikost_policka + self.velikost_policka / 2 - self.velikost_policka / 4,
                        self.left + x * self.velikost_policka + self.velikost_policka / 2 + self.velikost_policka / 4,
                        self.top + y * self.velikost_policka + self.velikost_policka / 2 + self.velikost_policka / 4)

    def nakresli_cislo(self, x, y, cislo):
        self.platno.create_text(self.preved_souradnice_x(x) + self.velikost_policka / 2,
                                self.preved_souradnice_y(y) + self.velikost_policka / 2, text=cislo)
        self.pole[y][x] = 2

    def end(self):
        print("GAME OVER")
        self.platno.create_text(self.width / 2, self.height / 2, text="Game Over")
        self.okno.unbind("<Button-1>")
        self.okno.unbind("<Button-3>")

    def vyhra(self):
        print("vyhral jsi")
        self.platno.create_text(self.width / 2, self.height / 2, text="Vyhral jsi")
        self.okno.unbind("<Button-1>")
        self.okno.unbind("<Button-3>")

a = App()
mainloop()
