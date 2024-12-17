import turtle

# Set up the screen for Turtle
# turtle_bg_image_01.py
#
# It works!
#
 
import turtle
import time
 
screen = turtle.Screen()
screen.setup(600,400)
screen.bgpic('D:/programmation related/Butterfly_01.png')
screen.update()
time.sleep(2)
screen.bgpic('D:/programmation related/complex_quotations_02.PNG')

# Create a turtle object for drawing
my_turtle = turtle.Turtle()
my_turtle.color("white")
my_turtle.penup()

# Function to handle mouse clicks
def on_click(x, y):
    my_turtle.clear()  # Clear any previous text
    my_turtle.goto(x, y)  # Move the turtle to where the user clicked
    my_turtle.write("You clicked here!", align="center", font=("Arial", 16, "normal"))

# Set up click listener
screen.onclick(on_click)

# Instructions
my_turtle.goto(0, 250)
my_turtle.write("Click anywhere on the screen!", align="center", font=("Arial", 16, "normal"))

# Keep the Turtle window open until clicked
turtle.mainloop()