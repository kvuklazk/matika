from random import randint
from tkinter import *
from math import floor


class App:
    def __init__(self):
        self.okno = Tk()
        self.okno.title("Mega dobry okno")
        self.width = self.okno.winfo_screenwidth()
        self.height = self.okno.winfo_screenheight()
        self.okno.geometry("%dx%d" % (self.width, self.height))
        self.okno.attributes('-fullscreen', True)
        self.okno.bind("<Escape>", self.window_close)

        self.velikost_pole = 15  # 100x100
        self.pocet_min = 40

        self.platno = Canvas(height=self.height, width=self.width)
        self.platno.pack()

        self.oznacene_miny = []

        self.okno.bind("<Button-3>", self.napravyklik)
        self.okno.bind("<space>", self.start)

        self.slide_pocet_min = Scale(self.platno,
                                     from_=0, to=self.velikost_pole ** 2,
                                     orient='horizontal',
                                     command=self.set_value_pocet_min)
        self.slide_pocet_min.set(self.pocet_min)
        self.slider_miny_window = self.platno.create_window(10, 10, anchor=NW, window=self.slide_pocet_min)

        self.slide_velikost_pole = Scale(self.platno,
                                         from_=5, to=self.pocet_min+10,
                                         orient='horizontal',
                                         command=self.set_value_velikost_pole)
        self.slide_velikost_pole.set(15)
        self.slider_velikost_pole_window = self.platno.create_window(10, 100,
                                                                     anchor=NW,
                                                                     window=self.slide_velikost_pole)

        self.mrizka = []
        self.cislicka = []

    def start(self, button, text_to_delete=None):
        self.okno.unbind("<space>")
        self.slide_velikost_pole.config(state='disabled')
        self.slide_pocet_min.config(state='disabled')

        for i in self.mrizka:
            self.platno.delete(i)
        self.mrizka = []

        if text_to_delete:
            self.platno.delete(text_to_delete)

        for i in self.oznacene_miny:
            self.platno.delete(i[2][0])
            self.platno.delete(i[2][1])

        self.oznacene_miny = []

        for i in self.cislicka:
            self.platno.delete(i)

        self.pole = []

        for i in range(self.velikost_pole):
            self.pole.append([0] * self.velikost_pole)

        self.velikost_policka = floor(self.height / self.velikost_pole)

        self.top = (self.height - self.velikost_policka * self.velikost_pole) / 2
        self.bottom = self.top + self.velikost_pole * self.velikost_policka
        self.left = self.width / 2 - self.velikost_policka * self.velikost_pole / 2
        self.right = self.width / 2 + self.velikost_policka * self.velikost_pole / 2

        self.mrizka.append(self.platno.create_rectangle(self.left, self.top, self.right, self.bottom))

        for i in range(1, self.velikost_pole):
            self.mrizka.append(self.platno.create_line(self.left + i * self.velikost_policka, self.top,
                                                       self.left + i * self.velikost_policka, self.bottom))
            self.mrizka.append(self.platno.create_line(self.left, self.top + i * self.velikost_policka, self.right,
                                                       self.top + i * self.velikost_policka))
        self.okno.bind("<Button-1>", self.zacatek_vybirani_min)

    def set_value_pocet_min(self, pocet):
        self.pocet_min = int(pocet)

    def set_value_velikost_pole(self, pocet):
        self.velikost_pole = int(pocet)

    def window_close(self, button):
        self.okno.attributes('-fullscreen', False)

    def zacatek_vybirani_min(self, event):
        for i in self.pole:
            for l in i:
                if l == 2:
                    return
        x_klik, y_klik = self.coords_from_event(event)
        if x_klik is None:
            return

        miny = self.pocet_min
        while miny > 0:
            x = randint(0, self.velikost_pole - 1)
            y = randint(0, self.velikost_pole - 1)
            if x_klik == x and y_klik == y:
                continue
            if self.pole[y][x] != 1:
                self.pole[y][x] = 1
                miny -= 1

        self.odkryj(x_klik, y_klik)
        self.okno.bind("<Button-1>", self.nalevyklik)

    def napravyklik(self, event):
        x, y = self.coords_from_event(event)
        if x is None:
            return
        self.nakresli_vlajecku(x, y)
        if self.vyhral_jsi_otazka():
            self.vyhra()
            return

    def coords_from_event(self, event):
        x = floor((event.x - self.left) / self.velikost_policka)
        y = floor((event.y - self.top) / self.velikost_policka)
        if not self.velikost_pole > x >= 0 and self.velikost_pole > y >= 0:
            return None, None
        return x, y

    def nakresli_vlajecku(self, x, y):
        je_oznacena = []
        for i in self.oznacene_miny:
            if i[0] == x and i[1] == y:
                je_oznacena = i
        if self.pole[y][x] == 2:
            return
        if len(je_oznacena) != 0:
            self.platno.delete(je_oznacena[2][0])
            self.platno.delete(je_oznacena[2][1])
            self.oznacene_miny.remove(je_oznacena)
            return

        l, t = self.kresli_vlajku(x, y)

        self.oznacene_miny.append([x, y, [l, t]])

    def kresli_vlajku(self, x, y):
        x = self.preved_souradnice_x(x)
        y = self.preved_souradnice_y(y)
        line = self.platno.create_line(x + self.velikost_policka / 2, y + self.velikost_policka * 9 / 12,
                                       x + self.velikost_policka / 2, y + self.velikost_policka * 2 / 12)
        triangle = self.platno.create_polygon(x + self.velikost_policka / 2,
                                              y + self.velikost_policka * 2 / 12,
                                              x + self.velikost_policka / 2 + self.velikost_policka * 4.5 / 12,
                                              y + self.velikost_policka * 4 / 12,
                                              x + self.velikost_policka / 2,
                                              y + self.velikost_policka * 1 / 2, fill="green")
        return line, triangle

    def vyhral_jsi_otazka(self):
        for y in self.pole:
            for x in y:
                if not (x == 1 or x == 2):
                    return False
        if len(self.oznacene_miny) == self.pocet_min:
            return True
        return False

    def nalevyklik(self, event):
        x, y = self.coords_from_event(event)
        if x is None:
            return

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
                if self.pole[y_1][x_1] == 0:
                    self.odkryj(x_1, y_1)

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
        self.cislicka.append(self.platno.create_text(self.preved_souradnice_x(x) + self.velikost_policka / 2,
                                                     self.preved_souradnice_y(y) + self.velikost_policka / 2,
                                                     text=cislo))
        self.pole[y][x] = 2

    def end(self):
        print("GAME OVER")
        self.platno.create_text(self.width / 2, self.height / 2, text="Game Over")
        self.okno.unbind("<Button-1>")
        self.okno.unbind("<Button-3>")
        self.okno.bind("<space>", self.start)

    def vyhra(self):
        print("vyhral jsi")
        text = self.platno.create_text(self.width / 2, self.height / 2, text="Vyhral jsi")
        self.okno.unbind("<Button-1>")
        self.okno.unbind("<Button-3>")
        self.okno.bind("<space>", lambda x: self.start(text))
        self.slide_pocet_min.config(state='active')
        self.slide_velikost_pole.config(state='active')


a = App()
mainloop()
