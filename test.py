import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Define the font globally
font = pygame.font.Font(None, 36)  # Define the font globally (or use a different font if needed)

# Set up the screen dimensions
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text-Based Adventure Game with Background")

# Set the background images for the main menu, game screen, village, war, jungle, and the new phase
background_image_menu = pygame.image.load('Blackboy.jpg')  # Main menu background
background_image_game = pygame.image.load('Olukunle.jpg')  # Game screen background
background_image_village = pygame.image.load('market.jpg')  # Market background for Village
background_image_war = pygame.image.load('Ready.jpg')  # War background after purchase
background_image_jungle = pygame.image.load('redopp.png')  # Jungle background
background_image_new = pygame.image.load('new.jpg')  # New background after collectbanana.py

# Scale the background images to fit the screen
background_image_menu = pygame.transform.scale(background_image_menu, (screen_width, screen_height))
background_image_game = pygame.transform.scale(background_image_game, (screen_width, screen_height))
background_image_village = pygame.transform.scale(background_image_village, (screen_width, screen_height))
background_image_war = pygame.transform.scale(background_image_war, (screen_width, screen_height))
background_image_jungle = pygame.transform.scale(background_image_jungle, (screen_width, screen_height))
background_image_new = pygame.transform.scale(background_image_new, (screen_width, screen_height))

# Define button colors
button_color = (255, 0, 0)  # Red
button_hover_color = (200, 0, 0)  # Darker Red

# Button positions and sizes
button_width = 200
button_height = 50
button1_rect = pygame.Rect(300, 200, button_width, button_height)
button2_rect = pygame.Rect(300, 300, button_width, button_height)
button3_rect = pygame.Rect(300, 350, button_width, button_height)  # For Village option
button4_rect = pygame.Rect(300, 400, button_width, button_height)  # For Jungle option

# Continue button for Jungle screen
continue_button_rect = pygame.Rect(300, 500, button_width, button_height)  # Continue button at the bottom

# Advance button for after Collect Banana game
advance_button_rect = pygame.Rect(300, 500, button_width, button_height)  # Advance button

# Eat and Sell buttons for bananas
eat_button_rect = pygame.Rect(200, 500, button_width, button_height)  # Eat button
sell_button_rect = pygame.Rect(500, 500, button_width, button_height)  # Sell button

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
    text_surface = font.render(text, True, (255, 255, 255))  # White text
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

# Function to display rewards at the top of the 'new.jpg' background
def display_rewards():
    reward_text = "You won 5 Bananas! "

    # Add more rewards based on purchases
    if "Warrior Monkey" in inventory:
        reward_text += " + 3 for Warrior Monkey"
    if "Machete" in inventory:
        reward_text += " + 2 for Machete"
    if "Banana" in inventory:
        reward_text += " + 1 for Banana"

    # Draw the text box
    message_box_rect = pygame.Rect(50, 20, screen_width - 100, 100)
    pygame.draw.rect(screen, (0, 0, 0), message_box_rect)  # Draw background for the text box
    draw_text_in_box(reward_text, message_box_rect, font, (255, 255, 255))  # Draw the text

# Function to run the collect banana game and wait until it's closed
def run_collect_banana():
    subprocess.run(['python', 'collectbanana.py'])

# Main game loop
running = True
current_screen = "menu"  # Start at the main menu screen
user_input = ""
collect_banana_completed = False  # Flag to track if collect banana game is done
advance_to_next_phase = False  # Flag for when the player advances to next phase
banana_eaten = False  # Flag to track if banana is eaten
banana_sold = False  # Flag to track if banana is sold

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
                current_screen = "jungle"  # Change to the jungle screen

            # Check if Continue button is clicked
            if current_screen == "jungle" and continue_button_rect.collidepoint(mouse_x, mouse_y):
                print("Continue clicked")
                run_collect_banana()  # Run collectbanana.py when clicked
                collect_banana_completed = True  # Mark that collect banana game is completed

            # Check if Advance button is clicked after banana collection
            if collect_banana_completed and advance_button_rect.collidepoint(mouse_x, mouse_y):
                print("Advance clicked")
                current_screen = "new_background"  # Change to new background (new.jpg)

            # Handle item purchases in village
            if current_screen == "village":
                if warrior_monkey.rect.collidepoint(mouse_x, mouse_y) and not warrior_monkey.purchased:
                    warrior_monkey.purchase()
                    print(f"Purchased {warrior_monkey.name}")
                    current_screen = "jungle"  # Switch to jungle screen after purchase

                elif banana.rect.collidepoint(mouse_x, mouse_y) and not banana.purchased:
                    banana.purchase()
                    print(f"Purchased {banana.name}")
                    current_screen = "jungle"  # Switch to jungle screen after purchase

                elif machete.rect.collidepoint(mouse_x, mouse_y) and not machete.purchased:
                    machete.purchase()
                    print(f"Purchased {machete.name}")
                    current_screen = "jungle"  # Switch to jungle screen after purchase

            # Handle banana eating and selling
            if current_screen == "new_background":
                if eat_button_rect.collidepoint(mouse_x, mouse_y) and not banana_eaten:
                    banana_eaten = True
                    print("Banana eaten")
                elif sell_button_rect.collidepoint(mouse_x, mouse_y) and not banana_sold:
                    banana_sold = True
                    money += 50  # Add 50 Naira to the player's money
                    print("Banana sold")

    # Draw everything
    if current_screen == "menu":
        # Main menu screen
        screen.fill((255, 255, 255))  # White background
        screen.blit(background_image_menu, (0, 0))  # Draw main menu background

        # Draw buttons
        draw_button(button1_rect, "Start Game")
        draw_button(button2_rect, "Exit")

    elif current_screen == "game":
        # Game screen
        screen.fill((255, 255, 255))  # White background
        screen.blit(background_image_game, (0, 0))  # Draw the game screen background

        # Show the options: Village or Jungle
        draw_button(button3_rect, "Go to Village")
        draw_button(button4_rect, "Go to Jungle")

    elif current_screen == "village":
        # Village screen
        screen.fill((255, 255, 255))  # White background
        screen.blit(background_image_village, (0, 0))  # Draw market background for village

        # Display items to purchase
        if not warrior_monkey.purchased:
            draw_button(warrior_monkey.rect, f"Warrior Monkey: {warrior_monkey.cost} Naira")
        if not banana.purchased:
            draw_button(banana.rect, f"Banana: {banana.cost} Naira")
        if not machete.purchased:
            draw_button(machete.rect, f"Machete: {machete.cost} Naira")

    elif current_screen == "jungle":
        # Jungle screen
        screen.fill((255, 255, 255))  # White background
        screen.blit(background_image_jungle, (0, 0))  # Draw jungle background

        # Draw message box
        message_text = "Collect 5 bananas to survive here! I'll use your item if you have any to help you along"
        message_box_rect = pygame.Rect(50, 20, screen_width - 100, 100)
        pygame.draw.rect(screen, (0, 0, 0), message_box_rect)
        draw_text_in_box(message_text, message_box_rect, font, (255, 255, 255))

        # Continue Button
        draw_button(continue_button_rect, "Continue")

    elif current_screen == "new_background":
        # After advancing, change to new background
        screen.fill((255, 255, 255))
        screen.blit(background_image_new, (0, 0))  # Draw new.jpg background

        # Display rewards at the top
        display_rewards()  # Call the function to show the rewards

        # Draw Eat and Sell buttons
        draw_button(eat_button_rect, "Eat Banana")
        draw_button(sell_button_rect, "Sell Banana")

        # Display banana status
        if banana_eaten:
            banana_status_text = "Banana eaten"
        elif banana_sold:
            banana_status_text = "Banana sold"
        else:
            banana_status_text = "Banana available"

        banana_status_surface = font.render(banana_status_text, True, (255, 255, 255))  # White text
        screen.blit(banana_status_surface, (10, 150))  # Display banana status

    # Draw the money counter in the top-left corner
    draw_money_counter()

    # Display inventory in bottom-right corner
    display_inventory()

    # Update the display
    pygame.display.flip()

# Quit the game when the loop ends
pygame.quit()
sys.exit()
