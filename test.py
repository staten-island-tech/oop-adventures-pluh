import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text-Based Adventure Game with Background")

# Set the background images for the main menu, game screen, village, and war
background_image_menu = pygame.image.load('Blackboy.jpg')  # Main menu background
background_image_game = pygame.image.load('Olukunle.jpg')  # Game screen background
background_image_village = pygame.image.load('market.jpg')  # Market background for Village
background_image_war = pygame.image.load('Ready.jpg')  # War background after purchase
background_image_menu = pygame.transform.scale(background_image_menu, (screen_width, screen_height))  # Scale to fit
background_image_game = pygame.transform.scale(background_image_game, (screen_width, screen_height))  # Scale to fit
background_image_village = pygame.transform.scale(background_image_village, (screen_width, screen_height))  # Scale to fit
background_image_war = pygame.transform.scale(background_image_war, (screen_width, screen_height))  # Scale to fit

# Define button colors
button_color = (255, 0, 0)  # Red
button_hover_color = (200, 0, 0)  # Darker Red
button_font = pygame.font.Font(None, 36)

# Button positions and sizes
button_width = 200
button_height = 50
button1_rect = pygame.Rect(300, 200, button_width, button_height)
button2_rect = pygame.Rect(300, 300, button_width, button_height)
button3_rect = pygame.Rect(300, 350, button_width, button_height)  # For Village option
button4_rect = pygame.Rect(300, 400, button_width, button_height)  # For Jungle option

# Text to be rendered on the screen
font = pygame.font.Font(None, 36)
welcome_text = font.render("Welcome to the Village Brother!", True, (255, 255, 255))  # White text
fufu_text = "Do you want to go to the village or the jungle?"  # White text for "You want fufu?"

# Money variable (starts with 100 Naira)
money = 100

# Player's inventory (for storing purchased items)
inventory = []

# Item class for handling items in the village
class Item:
    def __init__(self, name, cost, rect):
        self.name = name
        self.cost = cost
        self.rect = rect  # Position for the item in the shop
        self.purchased = False  # Track if the item is purchased

    def can_afford(self, player_money):
        return player_money >= self.cost

    def purchase(self):
        global money
        if self.can_afford(money):
            money -= self.cost
            inventory.append(self.name)  # Add item to the player's inventory
            self.purchased = True  # Mark the item as purchased
            return True
        return False

# Create items
warrior_monkey = Item("Warrior Monkey", 80, pygame.Rect(50, 200, button_width, button_height))
banana = Item("Banana", 50, pygame.Rect(50, 300, button_width, button_height))
machete = Item("Machete", 60, pygame.Rect(50, 400, button_width, button_height))

# Function to draw buttons
def draw_button(rect, text):
    pygame.draw.rect(screen, button_color, rect)
    text_surface = button_font.render(text, True, (255, 255, 255))  # White text
    screen.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2,
                               rect.y + (rect.height - text_surface.get_height()) // 2))

# Function to handle text input
def handle_text_input():
    user_input = ''
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False  # End input when Enter is pressed
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]  # Remove the last character
                else:
                    user_input += event.unicode  # Add the character typed to the input
        return user_input

# Function to draw text that automatically fits into a box
def draw_text_in_box(text, rect, font, color):
    words = text.split(" ")
    lines = []
    current_line = ""
    
    # Loop through each word to check if it fits in the box
    for word in words:
        test_line = current_line + " " + word if current_line else word
        test_surface = font.render(test_line, True, color)
        if test_surface.get_width() <= rect.width:  # Check if the text fits
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word  # Start a new line with the current word

    lines.append(current_line)  # Add the last line
    
    # Render each line in the box
    y_offset = rect.top + (rect.height - len(lines) * font.get_height()) // 2  # Center vertically
    for line in lines:
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (rect.left + (rect.width - text_surface.get_width()) // 2, y_offset))
        y_offset += font.get_height()

# Function to draw the money counter in the top-left corner
def draw_money_counter():
    money_text = f"Money: {money} Naira"
    money_surface = font.render(money_text, True, (255, 255, 255))  # White text
    screen.blit(money_surface, (10, 10))  # Top-left corner

# Function to display inventory in the bottom-right corner
def display_inventory():
    inventory_text = "Inventory: " + ", ".join(inventory)
    inventory_surface = font.render(inventory_text, True, (255, 255, 255))  # White text
    text_width, text_height = inventory_surface.get_size()
    screen.blit(inventory_surface, (screen_width - text_width - 10, screen_height - text_height - 10))  # Bottom-right corner

# Main game loop
running = True
current_screen = "menu"  # Start at the main menu screen
user_input = ""
purchase_complete = False  # Flag to track if purchase is complete

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse button click
            mouse_x, mouse_y = event.pos
            if button1_rect.collidepoint(mouse_x, mouse_y):  # If clicked inside button1
                current_screen = "game"  # Switch to the game screen
                print("Button 1 clicked")
            elif button2_rect.collidepoint(mouse_x, mouse_y):  # If clicked inside button2
                print("Button 2 clicked")
                running = False  # Exit the game

            # Check for Village and Jungle choices
            if button3_rect.collidepoint(mouse_x, mouse_y):  # If clicked inside button3
                print("Village chosen")
                current_screen = "village"  # Change to the village background
            elif button4_rect.collidepoint(mouse_x, mouse_y):  # If clicked inside button4
                print("Jungle chosen")
                # Add actions to go to the jungle here

            # Check for item purchases in the village
            if current_screen == "village":
                if warrior_monkey.rect.collidepoint(mouse_x, mouse_y) and not warrior_monkey.purchased:
                    if warrior_monkey.purchase():
                        print("Warrior Monkey purchased! Added to inventory.")
                        # Change the background to Ready.jpg after purchase
                        background_image_village = background_image_war
                        purchase_complete = True
                    else:
                        print("Not enough money for Warrior Monkey.")
                elif banana.rect.collidepoint(mouse_x, mouse_y) and not banana.purchased:
                    if banana.purchase():
                        print("Banana purchased! Added to inventory.")
                        # Change the background to Ready.jpg after purchase
                        background_image_village = background_image_war
                        purchase_complete = True
                    else:
                        print("Not enough money for Banana.")
                elif machete.rect.collidepoint(mouse_x, mouse_y) and not machete.purchased:
                    if machete.purchase():
                        print("Machete purchased! Added to inventory.")
                        # Change the background to Ready.jpg after purchase
                        background_image_village = background_image_war
                        purchase_complete = True
                    else:
                        print("Not enough money for Machete.")

                # Disable other items after one purchase
                if warrior_monkey.purchased or banana.purchased or machete.purchased:
                    warrior_monkey.rect = pygame.Rect(0, 0, 0, 0)
                    banana.rect = pygame.Rect(0, 0, 0, 0)
                    machete.rect = pygame.Rect(0, 0, 0, 0)

    # Draw everything
    if current_screen == "menu":
        # Main menu screen
        screen.fill((255, 255, 255))  # White background
        screen.blit(background_image_menu, (0, 0))  # Draw main menu background
        screen.blit(welcome_text, (250, 50))  # Position the welcome text on the screen

        # Draw buttons
        if button1_rect.collidepoint(pygame.mouse.get_pos()):
            draw_button(button1_rect, "Start Game")
        else:
            draw_button(button1_rect, "Start Game")

        if button2_rect.collidepoint(pygame.mouse.get_pos()):
            draw_button(button2_rect, "Exit")
        else:
            draw_button(button2_rect, "Exit")

    elif current_screen == "game":
        # Game screen
        screen.fill((255, 255, 255))  # White background
        screen.blit(background_image_game, (0, 0))  # Draw the game screen background (Olukunle.jpg)

        # Display text box with fufu text
        pygame.draw.rect(screen, (0, 0, 0), (150, 450, 500, 100))  # Black box for text
        draw_text_in_box(fufu_text, pygame.Rect(150, 450, 500, 100), font, (255, 255, 255))  # Draw text inside box

        # Show the options: Village or Jungle
        if button3_rect.collidepoint(pygame.mouse.get_pos()):
            draw_button(button3_rect, "Go to Village")
        else:
            draw_button(button3_rect, "Go to Village")

        if button4_rect.collidepoint(pygame.mouse.get_pos()):
            draw_button(button4_rect, "Go to Jungle")
        else:
            draw_button(button4_rect, "Go to Jungle")

    elif current_screen == "village":
        # Village screen
        screen.fill((255, 255, 255))  # White background
        screen.blit(background_image_village, (0, 0))  # Draw market background for village

        # If purchase is complete, show "Alright, you're done, let's get battling"
        if purchase_complete:
            battle_text = font.render("Alright, you're done, let's get battling!", True, (150, 100, 7))
            screen.blit(battle_text, (200, 30))  # Display at the top

        # Remove "You are in the village market!" text after purchase
        if not purchase_complete:
            village_text = font.render("You are in the village market!", True, (255, 255, 255))
            screen.blit(village_text, (250, 50))  # Display village market text

        # Draw items for purchase (only if not purchased)
        if not warrior_monkey.purchased:
            draw_button(warrior_monkey.rect, f"Warrior Monkey: {warrior_monkey.cost} Naira")
        if not banana.purchased:
            draw_button(banana.rect, f"Banana: {banana.cost} Naira")
        if not machete.purchased:
            draw_button(machete.rect, f"Machete: {machete.cost} Naira")

    # Draw the money counter in the top-left corner
    draw_money_counter()

    # Display inventory in bottom-right corner
    display_inventory()

    # Update the display
    pygame.display.flip()

# Quit the game when the loop ends
pygame.quit()
sys.exit()
