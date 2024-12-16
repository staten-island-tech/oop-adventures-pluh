import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text-Based Adventure Game with Background")

# Set the background image (replace with the actual file path)
background_image = pygame.image.load('b3916745-37c4-44f1-8a7f-fd2d12a8b3ce.jfif')  # Load the image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # Scale it to fit the screen

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image
    screen.blit(background_image, (0, 0))  # Draw the background at (0, 0)

    # Add any game objects or text on top of the background here
    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to the Adventure Game!", True, (255, 255, 255))  # White text
    screen.blit(text, (250, 50))  # Position the text on the screen

    # Update the display
    pygame.display.flip()

# Quit the game when the loop ends
pygame.quit()
sys.exit()
