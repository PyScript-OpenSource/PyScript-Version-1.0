from PyScript import scr,tess
import time
t = tess()
screen = t.tess.getscreen()

screen.bgcolor('red')
t.go(100)
t.left(90)
t.go(100)
t.left(90)
t.go(100)
t.left(90)
t.go(100)
screen.bgcolor('pink')
t.noPen()
t.go(60)
t.pen()
t.go(30)
screen.mainloop()
