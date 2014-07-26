import turtle
class scr:
    def say(text):
        print(text)
    def toInt(num):
        return int(num)
    def toString(thing):
        return str(thing)
    def get(text):
        return input(text)
class tess():
    def __init__(self):
        self.tess = turtle.Turtle()

    def go(self,px):
        self.tess.fd(px)

    def back(self,px):
        self.tess.bk(px)

    def left(self,dg):
        self.tess.lt(dg)

    def right(self,dg):
        self.tess.rt(dg)

    def pen(self):
        self.tess.pendown()

    def noPen(self):
        self.tess.penup()
