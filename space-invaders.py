# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from pygame.locals import *


# class for the enemies (which will be just circles)
class Enemy:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def reset(self):
        self.x = randint(25, 695)
        self.y = 25
        self.speed = randint(3, 6)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getRadius(self):
        return self.radius
    
    def getSpeed(self):
        return self.speed
    
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed = 20

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getRadius(self):
        return self.radius
    
    def getSpeed(self):
        return self.speed

    
def writeText(string, coordx, coordy, fontSize):
    screen.fill((235, 119, 110))
  	#set the font to write with
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    #get the rect of the text
    textRect = text.get_rect()
    #set the position of the text
    textRect.center = (coordx, coordy)
    #add text to window
    screen.blit(text, textRect)
    #update window
    pygame.display.update()

def restartGame(enemies, ship_x, ship_y):
    #writeText("You Lost. Press Enter to Restart.", 350, 400, 20)
    for enemy in enemies:
        enemy.x = randint(25, 695)
        enemy.y = 25
        enemy.radius = 25
        enemy.speed = randint(3, 6)
    ship_x = 335
    ship_y = 800
    return enemies, ship_x, ship_y


# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 900))
clock = pygame.time.Clock()


running = True
ship_x_pos = 335
ship_y_pos = 800
enemies = []
bullets = []
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
    for enemy in enemies:
        if enemy.y > 875:
            enemy.reset()
        pygame.draw.circle(screen, "red", (enemy.getX(), enemy.getY()), enemy.getRadius())
        enemy.y += enemy.getSpeed()

    # DRAW BULLETS
    for bullet in bullets:
        pygame.draw.circle(screen, "yellow", (bullet.getX(), bullet.getY()), bullet.getRadius())
        bullet.y -= bullet.getSpeed()
        for enemy in enemies:
            if abs(bullet.getX() - enemy.getX()) <= 30 and abs(bullet.getY() - enemy.getY()) <= 30: # enemy radius = 25; bullet radius = 5; so it can have an offset of 30
                if bullet in bullets:
                    bullets.remove(bullet)
                enemy.reset()
        if bullet.getY() <= 0 and bullet in bullets:
            bullets.remove(bullet)

    # RENDER YOUR GAME HERE
    ship = pygame.Rect(ship_x_pos, ship_y_pos, 50, 50)
    pygame.draw.rect(screen, (36, 14, 235), ship)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and ship_y_pos > 0:
        ship_y_pos -= 15 
    if keys[pygame.K_s] and ship_y_pos < 850:
        ship_y_pos += 15
    if keys[pygame.K_a] and ship_x_pos > 25:
        ship_x_pos -= 15 
    if keys[pygame.K_d] and ship_x_pos < 645:
        ship_x_pos += 15
    if keys[pygame.K_m]: # TODO: change shoot key for something more intuitive
        bullets.append(Bullet(ship_x_pos + 25, ship_y_pos))
    if keys[pygame.K_x]: # TODO: change game over trigger when adding collisions
        writeText("You Lost! Press Enter to Start Again.", 350, 400, 20)
        pygame.event.clear()
        r = True
        while r:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    enemies, ship_x_pos, ship_y_pos = restartGame(enemies, ship_x_pos, ship_y_pos)
                    r = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()




