import os
import turtle
import time
import random

# Initialize score variables
score = 0
high_score = 0
delay = 0.1

# Setup the screen
window1 = turtle.Screen()
window1.title("Banana Game")
window1.setup(width=600, height=600)
window1.bgcolor("black")
window1.tracer(0)  # Turns off automatic screen updates for better performance

# Snake setup (brown circle as snake)
snake = []
for i in range(3):
    segment = turtle.Turtle()
    segment.speed(0)
    segment.shape("circle")
    segment.color("brown")
    segment.penup()
    segment.goto(-20 * i, 0)  # Position the snake segments
    snake.append(segment)

# Fruit setup (yellow rectangle)
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")  # Start with a square shape
fruit.color("yellow")
fruit.penup()
fruit.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the square to make a rectangle
fruit.goto(0, 100)  # Position the banana initially

# Scoring display setup
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Snake movement direction
direction = "stop"

# Define movement functions
def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

# Keyboard bindings
window1.listen()
window1.onkey(go_up, "w")
window1.onkey(go_down, "s")
window1.onkey(go_left, "a")
window1.onkey(go_right, "d")

# Function to move the snake
def move():
    if direction == "up":
        y = snake[0].ycor()
        snake[0].sety(y + 20)
    if direction == "down":
        y = snake[0].ycor()
        snake[0].sety(y - 20)
    if direction == "left":
        x = snake[0].xcor()
        snake[0].setx(x - 20)
    if direction == "right":
        x = snake[0].xcor()
        snake[0].setx(x + 20)

# Main game loop
while True:
    window1.update()  # Updates the screen
    
    # Check for collision with the wall
    if abs(snake[0].xcor()) > 290 or abs(snake[0].ycor()) > 290:
        time.sleep(1)
        # Reset the game
        for segment in snake:
            segment.goto(1000, 1000)  # Move the snake off screen
        snake.clear()
        score = 0
        direction = "stop"
        
        # Recreate the snake
        for i in range(3):
            segment = turtle.Turtle()
            segment.speed(0)
            segment.shape("circle")
            segment.color("brown")
            segment.penup()
            segment.goto(-20 * i, 0)
            snake.append(segment)
            
        score_display.clear()
        score_display.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    # Check for collision with the fruit
    if snake[0].distance(fruit) < 20:
        # Move fruit to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        fruit.goto(x, y)
        
        # Increase score (no snake growth)
        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    # Move the snake's body
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    # Move the head of the snake
    if len(snake) > 0:
        move()

    # Check for collision with the snake's body
    for segment in snake[1:]:
        if snake[0].distance(segment) < 10:
            time.sleep(1)
            # Reset the game
            for segment in snake:
                segment.goto(1000, 1000)  # Move the snake off screen
            snake.clear()
            score = 0
            direction = "stop"
            
            # Recreate the snake
            for i in range(3):
                segment = turtle.Turtle()
                segment.speed(0)
                segment.shape("circle")
                segment.color("brown")
                segment.penup()
                segment.goto(-20 * i, 0)
                snake.append(segment)

            score_display.clear()
            score_display.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    time.sleep(delay)  # Control the speed of the game
