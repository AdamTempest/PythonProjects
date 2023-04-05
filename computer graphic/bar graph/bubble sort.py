import turtle
import random
import time

def draw_bar_graph(data):
    scr = turtle.Screen()
    scr.bgcolor("white")
    scr.tracer(0)
    t=turtle.Turtle()
    t.color("black")
    t.shape("circle")
    t.pensize(3)
    t.penup()
    t.setpos(50-1*(scr._window_size()[0]/2),50-(scr._window_size()[1]/2))
    t.pendown()
    for i in range(len(data)):
        t.left(90)
        t.forward(data[i])
        t.right(90)
        t.forward(scr._window_size()[0]/100)
        t.right(90)
        t.forward(data[i])
        t.left(90)
        scr.update()

def bubble_sort(l):
    scr = turtle.Screen()
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                t=l[j+1]
                l[j+1]=l[j]
                l[j]=t
            scr.clear()
            draw_bar_graph(l)
            time.sleep(0.1)

data=[random.randint(1,800) for i in range(50)]
bubble_sort(data)