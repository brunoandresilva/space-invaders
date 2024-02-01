# Example file showing a basic pygame "game loop"
import pygame
from random import randint


# class for the enemies (which will be just circles)
class Enemy:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getRadius(self):
        return self.radius
    
    def getSpeed(self):
        return self.speed


# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 900))
clock = pygame.time.Clock()
running = True
x_pos = 335
y_pos = 800
enemies = []

for i in range(0, 5):
    enemies.append(Enemy(randint(25, 695), 25, 25, randint(3, 6)))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # DRAW ENEMIES
    for i in range(0, 5):
        if enemies[i].y > 875:
            enemies[i].y = 25
            enemies[i].x = randint(25, 695)
            enemies[i].speed = randint(3, 6)
        pygame.draw.circle(screen, "red", (enemies[i].getX(), enemies[i].getY()), enemies[i].getRadius())
        enemies[i].y += enemies[i].getSpeed()

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