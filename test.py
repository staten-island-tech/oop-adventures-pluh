import pygame # type: ignore
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text-Based Adventure Game with Background")

background_image = pygame.image.load('b3916745-37c4-44f1-8a7f-fd2d12a8b3ce.jfif')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to the Adventure Game!", True, (255, 255, 255))
    screen.blit(text, (250, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()