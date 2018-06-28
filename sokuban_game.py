import pygame

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Display an image')
penguinImage = pygame.image.load("abc.jpg").convert()

x = 20 # x coordnate of image
y = 30  # y coordinate of image
screen.blit(penguinImage, (x, y))  # paint to screen
pygame.display.flip()  # paint screen one time

running = True
while (running):  # loop listening for end of game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# loop over, quite pygame
pygame.quit()