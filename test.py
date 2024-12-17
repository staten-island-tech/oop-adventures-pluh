import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text-Based Adventure Game with Background")

# Set the background image
background_image = pygame.image.load('Blackboy.jpg')  # Load the image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # Scale it to fit the screen

# Define button colors
button_color = (255, 0, 0)  # Red
button_hover_color = (200, 0, 0)  # Darker Red
button_font = pygame.font.Font(None, 36)

# Button positions and sizes
button_width = 200
button_height = 50
button1_rect = pygame.Rect(300, 200, button_width, button_height)
button2_rect = pygame.Rect(300, 300, button_width, button_height)

# Text to be rendered on the screen
font = pygame.font.Font(None, 36)
welcome_text = font.render("Welcome to the Village Brother!", True, (255, 255, 255))  # White text

# Function to draw buttons
def draw_button(rect, text):
    pygame.draw.rect(screen, button_color, rect)
    text_surface = button_font.render(text, True, (255, 255, 255))  # White text
    screen.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2,
                               rect.y + (rect.height - text_surface.get_height()) // 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse button click
            mouse_x, mouse_y = event.pos
            if button1_rect.collidepoint(mouse_x, mouse_y):  # If clicked inside button1
                print("Button 1 clicked")
                # You can change the background or do any action here
            elif button2_rect.collidepoint(mouse_x, mouse_y):  # If clicked inside button2
                print("Button 2 clicked")
                # You can change the background or do any action here

    # Draw everything
    screen.fill((255, 255, 255))  # Fill screen with white (or black if needed)
    screen.blit(background_image, (0, 0))  # Draw background image

    # Draw the welcome text at the top of the screen
    screen.blit(welcome_text, (250, 50))  # Position the text on the screen

    # Check for hover effect and draw buttons
    if button1_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(button1_rect, "Start Game")
    else:
        draw_button(button1_rect, "Start Game")

    if button2_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(button2_rect, "Exit")
    else:
        draw_button(button2_rect, "Exit")

    # Update the display
    pygame.display.flip()

# Quit the game when the loop ends
pygame.quit()
sys.exit()
