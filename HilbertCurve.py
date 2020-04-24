#15.33 Hilbert Curve
from tkinter import *

class HilbertCurve:
    def __init__(self):
        window = Tk()
        window.title("Hilbert Curve")

        self.width = 200
        self.height = 200
        self.canvas = Canvas(window, width = self.width,
                             height = self.height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack(side = LEFT)

        Label(frame, text = "Enter an order").pack(side = LEFT)
        self.order = StringVar()
        Entry(frame, textvariable = self.order,
              justify = RIGHT).pack(side = LEFT)
        Button(frame, text = "Display",
               command = self.display).pack(side = LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")
        self.pattern = []
        self.path = []
        order = int(self.order.get())
        self.drawCurve(order, 'r')
        #self.getPath()
        print(self.pattern)
        point = [10, 10]
        size = (self.width - 20) / ((2 ** order) - 1)
        self.draw(point, size)

    def drawCurve(self, order, s):
        if order == 0:
            self.pattern.append(s)
        else:
            if s == 'd':
                self.drawCurve(order - 1, 'r')
                self.drawCurve(order - 1, 'd')
                self.drawCurve(order - 1, 'd')
                self.drawCurve(order - 1, 'l')
            elif s == 'u':
                self.drawCurve(order - 1, 'l')
                self.drawCurve(order - 1, 'u')
                self.drawCurve(order - 1, 'u')
                self.drawCurve(order - 1, 'r')
            elif s == 'l':
                self.drawCurve(order - 1, 'u')
                self.drawCurve(order - 1, 'l')
                self.drawCurve(order - 1, 'l')
                self.drawCurve(order - 1, 'd')
            elif s == 'r':
                self.drawCurve(order - 1, 'd')
                self.drawCurve(order - 1, 'r')
                self.drawCurve(order - 1, 'r')
                self.drawCurve(order - 1, 'u')

    def getPath(self):
        for i in range(len(self.pattern)):
            if i % 16 == 3 or i % 16 == 7:
                self.pattern[i] = self.pattern[i - 2]
            elif i % 16 == 11 or i % 16 == 15:
                self.pattern[i - 1] = self.pattern[i]
                
    def draw(self, point, size):
        p = point
        for d in self.pattern:
            if d == 'r':
                self.canvas.create_line(p[0], p[1],
                                        p[0] + size, p[1], tags = "line")
                p[0] += size         
            elif d == 'l':
                self.canvas.create_line(p[0], p[1],
                                        p[0] - size, p[1], tags = "line")
                p[0] -= size
            elif d == 'u':
                self.canvas.create_line(p[0], p[1],
                                        p[0], p[1] - size, tags = "line")
                p[1] -= size
            elif d == 'd':
                self.canvas.create_line(p[0], p[1],
                                        p[0], p[1] + size, tags = "line")
                p[1] += size


HilbertCurve()
