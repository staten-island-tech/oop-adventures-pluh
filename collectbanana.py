import os
import turtle
import time
import random

# Initialize score variables
naira = 0  # Changed from score to naira
delay = 0.1

# Setup the screen
window1 = turtle.Screen()
window1.title("Banana Game")
window1.setup(width=600, height=600)
window1.bgcolor("green")  # Changed the background color to green
window1.tracer(0)  # Turns off automatic screen updates for better performance

# Snake setup (one brown circle as snake)
snake = []
segment = turtle.Turtle()
segment.speed(0)
segment.shape("circle")
segment.color("brown")
segment.penup()
segment.goto(0, 0)  # Position the snake initially at the center
snake.append(segment)

# Fruit setup (yellow rectangle)
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")  # Start with a square shape
fruit.color("yellow")
fruit.penup()
fruit.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the square to make a rectangle
fruit.goto(0, 100)  # Position the banana initially

# Obstacles setup
obstacles = []

def create_obstacles():
    global obstacles
    obstacles.clear()  # Clear existing obstacles
    for _ in range(5):  # Create 5 obstacles
        obstacle = turtle.Turtle()
        obstacle.speed(0)
        obstacle.shape("circle")
        obstacle.color("black")
        obstacle.penup()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        obstacle.goto(x, y)
        obstacles.append(obstacle)

# Naira (black circle) setup
naira_circles = []  # This list will hold the black circles representing Naira

# Scoring display setup
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

# Snake movement direction
direction = "stop"
game_over_flag = False  # Flag to track if the game is over

# Define movement functions
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

# Declare start_screen as a global variable so it can be accessed in multiple functions
start_screen = None

# Display the start screen
def display_start_screen():
    global start_screen
    start_screen = turtle.Turtle()
    start_screen.speed(0)
    start_screen.color("white")
    start_screen.penup()
    start_screen.hideturtle()
    start_screen.goto(0, 0)
    start_screen.write("Press 'Enter' to Start", align="center", font=("Courier", 16, "normal"))
    
    window1.update()  # Show the start screen
    window1.listen()
    window1.onkey(start_game, "Return")  # 'Enter' key starts the game

def start_game():
    global naira, direction, start_screen, game_over_flag
    naira = 0  # Reset naira
    direction = "stop"  # Reset direction
    score_display.clear()
    score_display.write("Naira: {}".format(naira), align="center", font=("Courier", 16, "normal"))
    window1.tracer(1)  # Enable game loop

    # Clear the start screen text
    start_screen.clear()  # This clears the "Press Enter to Start" text
    
    # Reset snake position
    snake[0].goto(0, 0)  # Bring the snake back to the center

    # Reset fruit position in front of the snake
    fruit.goto(0, 20)

    # Create obstacles
    create_obstacles()

    # Reset game_over_flag
    game_over_flag = False

    game_loop()  # Start the game loop

# Main game loop after start screen
def game_loop():
    global naira, delay, game_over_flag
    while not game_over_flag:
        window1.update()  # Updates the screen
        
        # Check for collision with the wall
        if abs(snake[0].xcor()) > 290 or abs(snake[0].ycor()) > 290:
            game_over()
            break
        
        # Check for collision with the fruit
        if snake[0].distance(fruit) < 20:
            # Move fruit to a random spot in front of the snake
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            fruit.goto(x, y)
            
            # Increase naira (10 Naira per banana collected)
            naira += 10
            score_display.clear()
            score_display.write("Naira: {}".format(naira), align="center", font=("Courier", 16, "normal"))
            
            # Add a black circle (representing Naira) at the snake's position
            naira_circle = turtle.Turtle()
            naira_circle.speed(0)
            naira_circle.shape("circle")
            naira_circle.color("black")
            naira_circle.penup()
            naira_circle.goto(snake[0].xcor(), snake[0].ycor())
            naira_circles.append(naira_circle)
        
        # Check for collision with the obstacles
        for obstacle in obstacles:
            if snake[0].distance(obstacle) < 20:
                game_over()
                break
        
        # Move the snake (there is only one segment now)
        move()
        
        # Check for collision with the snake's body (although there is only one segment now)
        if len(snake) > 1:
            for segment in snake[1:]:
                if snake[0].distance(segment) < 10:
                    game_over()
                    break
        
        time.sleep(delay)  # Control the speed of the game

# Handle the game over and offer restart option
# Handle the game over and offer restart option
def game_over():
    global naira, game_over_flag
    game_over_flag = True  # Set the flag to stop the snake from moving
    
    # Deduct 30 Naira when the player loses
    naira -= 30
    if naira < 0:
        naira = 0  # Ensure naira doesn't go negative

    # Clear the score display and show the game over message
    score_display.clear()
    score_display.write(f"Game Over! You lost 30 Naira to a tribe man. Press 'Enter' to Restart", align="center", font=("Courier", 16, "normal"))
    
    # Update the screen
    window1.update()

    # Listen for restart key press
    window1.listen()
    window1.onkey(start_game, "Return")  # 'Enter' key restarts the game

    # Hide obstacles and Naira circles after game over
    for obstacle in obstacles:
        obstacle.hideturtle()  # Hide obstacles (without creating more)
    for naira_circle in naira_circles:
        naira_circle.hideturtle()  # Hide Naira circles
  # 'Enter' key restarts the game

    # Clear obstacles and naira_circles after game over
    for obstacle in obstacles:
        obstacle.hideturtle()  # Hide the obstacles (without creating more)
    for naira_circle in naira_circles:
        naira_circle.hideturtle()  # Hide the Naira circles

# Start the game by displaying the start screen
display_start_screen()

# Main game execution
turtle.done()