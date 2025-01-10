import os
import turtle
import time
import random

banana = 0
delay = 0.1

window1 = turtle.Screen()
window1.title("Banana Game")
window1.setup(width=600, height=600)
window1.bgcolor("green")
window1.tracer(0)

# Initialize snake
snake = []
segment = turtle.Turtle()
segment.speed(0)
segment.shape("circle")
segment.color("brown")
segment.penup()
segment.goto(0, 0)
snake.append(segment)

# Initialize fruit
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("yellow")
fruit.penup()
fruit.shapesize(stretch_wid=1, stretch_len=2)
fruit.goto(0, 100)

# Initialize obstacles
obstacles = []

def create_obstacles():
    global obstacles
    obstacles.clear()
    for _ in range(5):
        obstacle = turtle.Turtle()
        obstacle.speed(0)
        obstacle.shape("circle")
        obstacle.color("black")
        obstacle.penup()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        obstacle.goto(x, y)
        obstacles.append(obstacle)

banana_circles = []

# Initialize score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

direction = "stop"
game_over_flag = False

def go_up():
    global direction
    if direction != "down" and not game_over_flag:
        direction = "up"

def go_down():
    global direction
    if direction != "up" and not game_over_flag:
        direction = "down"

def go_left():
    global direction
    if direction != "right" and not game_over_flag:
        direction = "left"

def go_right():
    global direction
    if direction != "left" and not game_over_flag:
        direction = "right"

window1.listen()
window1.onkey(go_up, "w")
window1.onkey(go_down, "s")
window1.onkey(go_left, "a")
window1.onkey(go_right, "d")

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

start_screen = None

def display_start_screen():
    global start_screen
    start_screen = turtle.Turtle()
    start_screen.speed(0)
    start_screen.color("white")
    start_screen.penup()
    start_screen.hideturtle()
    start_screen.goto(0, 0)
    start_screen.write("Press 'Enter' to Start", align="center", font=("Courier", 16, "normal"))
    
    window1.update()
    window1.listen()
    window1.onkey(start_game, "Return")

def start_game():
    global banana, direction, start_screen, game_over_flag
    banana = 0
    direction = "stop"
    score_display.clear()
    score_display.write("Naira: {}".format(banana), align="center", font=("Courier", 16, "normal"))
    window1.tracer(1)
    start_screen.clear()
    snake[0].goto(0, 0)
    fruit.goto(0, 20)

    create_obstacles()
    game_over_flag = False

    game_loop()

def game_loop():
    global banana, delay, game_over_flag
    while not game_over_flag:
        window1.update()
        if abs(snake[0].xcor()) > 290 or abs(snake[0].ycor()) > 290:
            game_over()
            break

        if snake[0].distance(fruit) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            fruit.goto(x, y)

            banana += 10
            score_display.clear()
            score_display.write("Naira: {}".format(banana), align="center", font=("Courier", 16, "normal"))

            banana_circle = turtle.Turtle()
            banana_circle.speed(0)
            banana_circle.shape("circle")
            banana_circle.color("black")
            banana_circle.penup()
            banana_circle.goto(snake[0].xcor(), snake[0].ycor())
            banana_circles.append(banana_circle)

        for obstacle in obstacles:
            if snake[0].distance(obstacle) < 20:
                game_over()
                break

        move()

        if len(snake) > 1:
            for segment in snake[1:]:
                if snake[0].distance(segment) < 10:
                    game_over()
                    break

        time.sleep(delay)

def game_over():
    global banana, game_over_flag
    game_over_flag = True

    banana -= 100000000000
    if banana < 0:
        banana = 0

    score_display.clear()
    score_display.write(f"Game Over! You got robbed. Press 'Enter' to Restart", align="center", font=("Courier", 16, "normal"))

    window1.update()
    window1.listen()
    window1.onkey(start_game, "Return")

    for obstacle in obstacles:
        obstacle.hideturtle()
    for banana_circle in banana_circles:
        banana_circle.hideturtle()

display_start_screen()

turtle.done()