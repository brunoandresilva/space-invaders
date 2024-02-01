# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 900))
clock = pygame.time.Clock()
running = True
x_pos = 335
y_pos = 800

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    ship = pygame.Rect(x_pos, y_pos, 50, 50)
    pygame.draw.rect(screen, (36, 14, 235), ship)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y_pos > 0:
        y_pos -= 15 
    if keys[pygame.K_s] and y_pos < 850:
        y_pos += 15
    if keys[pygame.K_a] and x_pos > 25:
        x_pos -= 15 
    if keys[pygame.K_d] and x_pos < 645:
        x_pos += 15

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()