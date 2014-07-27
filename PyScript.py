import turtle
import webbrowser
from time import *
from random import randint
import os
class scr:
    def say(text):
        print(text)
    def toInt(num):
        return int(num)
    def toString(thing):
        return str(thing)
    def get(text):
        return input(text)
    def webpage(message,file):
        f = open(file,'w')
        f.write(message)
        f.close()
        webbrowser.open(file)
    def makePage(message,file):
        f = open(file,'w')
        f.write(message)
        f.close()
    def host(file):
        webbrowser.open(file)
    def delay(s):
        time.sleep(s)
    def play(wav):
        winsound.PlaySound(wav, winsound.SND_FILENAME)
    def printF(message,file):
        f = open(file,'w')
        f.write(message)
        f.close()
    def exe(location):
        os.startfile("C:\Users\Simon\Desktop\test\helloWorld.exe")
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
