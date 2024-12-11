import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text-Based Adventure Game with Background")

# Set background color to black (RGB value for black is (0, 0, 0))
BLACK = (0, 0, 0)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Add any game objects or text on top of the black background here
    # For example, adding a simple message:
    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to the Adventure Game!", True, (255, 255, 255))  # White text
    screen.blit(text, (250, 50))  # Position the text on the screen

    # Update the display
    pygame.display.flip()

# Quit the game when the loop ends
pygame.quit()
sys.exit()
