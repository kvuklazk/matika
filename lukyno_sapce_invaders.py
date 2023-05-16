from tkinter import *

class App:
    def __init__(self):
        self.okno = Tk()
        self.okno.title("Space Invaders")
        self.height = 800
        self.width = 800
        self.platno = Canvas(height=self.height, width=self.width)
        self.platno.pack()

        self.prisery = []
        for y in range(4):
            for x in range(10):
                self.prisery.append(Prisera(self, x*(30+50)+20, y*(30+50)+20))
        self.prisery_smer = 1

        hrac = Hrac(self)

        self.okno.bind("<Left>", hrac.posun_vlevo)
        self.okno.bind("<Right>", hrac.posun_vpravo)

        self.pohyb_vseho()

    def pohyb_vseho(self):
        print(self.prisery[0].x)
        if self.prisery[0].x > 50:
            self.prisery_smer = -1
            for prisera in self.prisery:
                self.platno.move(prisera.obrazek, 0, 5)
                prisera.y += 5
        if self.prisery[0].x < 0:
            self.prisery_smer = 1
            for prisera in self.prisery:
                self.platno.move(prisera.obrazek, 0, 5)
                prisera.y += 5
        for prisera in self.prisery:
            self.platno.move(prisera.obrazek, self.prisery_smer*5, 0)
            prisera.x += self.prisery_smer*5

        self.okno.after(50, self.pohyb_vseho)



class Hrac:
    def __init__(self, a):
        self.a = a
        self.width = 50
        self.height = 20
        # self.obrazek = PhotoImage("")
        self.x = 375
        self.y = 750
        self.obrazek = self.a.platno.create_rectangle(375, 750, 425, 775, fill='green')
        

    def posun_vlevo(self, event):
        if self.x > 0:
            self.x -= 10
            self.a.platno.move(self.obrazek, -10, 0)

    def posun_vpravo(self, event):
        if self.x < 750:
            self.x += 10
            self.a.platno.move(self.obrazek, 10, 0)

class Prisera:
    def __init__(self, a, x, y):
        self.a = a
        self.x = x
        self.y = y

        self.width = 30
        self.heigt = 30

        self.obrazek = self.a.platno.create_rectangle(self.x, self.y, self.x+30, self.y+30, fill='red')

a = App()
mainloop()