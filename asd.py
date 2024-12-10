import pygame 
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text-Based Adventure Game with Background")

# Load your background image (replace with your image file)
background = pygame.image.load("background_image.jpg")  # Ensure your image file is in the same directory or specify the full path
background = pygame.transform.scale(background, (screen_width, screen_height))  # Resize if needed

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image on the screen
    screen.blit(background, (0, 0))

    # Add any game objects or text on top of the background here
    # For example, adding a simple message:
    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to the Adventure Game!", True, (255, 255, 255))
    screen.blit(text, (250, 50))  # Position the text on the screen

    # Update the display
    pygame.display.flip()

# Quit the game when the loop ends
pygame.quit()
sys.exit()
