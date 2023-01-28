import turtle
import time

delay = 0.1

#ovo je pocetan screen
sg = turtle.Screen()
sg.title("Igra zmi'ce od MENE    (@Ja)")
sg.bgcolor("green")
sg.setup(width=1600, height=1600)
sg.tracer(0)


#zmijina glava

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "up"


#funkcije

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.yorc()
        head.sety(y + 20)

def move():
    if head.direction == "down":
        y = head.yorc()
        head.sety(y - 20)

def move():
    if head.direction == "left":
        x = head.xorc()
        head.sety(x - 20)

def move():
    if head.direction == "right":
        x = head.xorc()
        head.sety(x  + 20)

#kljucevi za mrdanje
sg.listen()
sg.onkeypress(go_up, "w")
sg.onkeypress(go_down, "s")
sg.onkeypress(go_left, "a")
sg.onkeypress(go_right, "d")

#loop glavne igre
while True:
    sg.update()

    move()

    time.sleep(delay)

sg.mainloop()


