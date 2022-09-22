from tkinter import N
import turtle
import colorsys

t=turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(0)
n=100
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n 
    t.color(c)
    for j in range(2):
        t.left(250)
        t.forward(i*3)
        for k in range(3):
            t.left(20)
            t.forward(22)

turtle.done()