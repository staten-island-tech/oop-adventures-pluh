import turtle
import pygame
import sys
import time

def run_turtle_graphics():
    screen = turtle.Screen()
    screen.setup(600, 400)
    screen.bgpic('D:/programmation related/Butterfly_01.png')
    screen.update()
    time.sleep(2)
    screen.bgpic('D:/programmation related/complex_quotations_02.PNG')

    my_turtle = turtle.Turtle()
    my_turtle.color("white")
    my_turtle.penup()

    def on_click(x, y):
        my_turtle.clear()
        my_turtle.goto(x, y)
        my_turtle.write("You clicked here!", align="center", font=("Arial", 16, "normal"))

    screen.onclick(on_click)

    my_turtle.goto(0, 250)
    my_turtle.write("Click anywhere on the screen!", align="center", font=("Arial", 16, "normal"))

    turtle.mainloop()