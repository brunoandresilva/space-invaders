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
        self.speed = randint(1, 4)

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

    
def writeText(string, coordx, coordy, fontSize, text_color):
    
  	#set the font to write with
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, text_color)
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
        enemy.speed = randint(1, 4)
    ship_x = 335
    ship_y = 800
    score = 0
    enemies_past = 0
    return enemies, ship_x, ship_y, score, enemies_past



# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 900))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
pressed = False

score = 0
enemies_past = 0
running = True
ship_x_pos = 335
ship_y_pos = 800
enemies = []
bullets = []
star_coords = []

for i in range(0, 200):
    star_coords.append((randint(0, 720), randint(0, 900)))

for i in range(0, 5):
    enemies.append(Enemy(randint(25, 695), 25, 25, randint(2, 5)))

# creating image objects
spaceship_img = pygame.image.load("./assets/spaceship.png").convert()
enemy_img = pygame.image.load("./assets/enemy_40.png").convert()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # DRAW BACKGROUND
    for coord in star_coords:
        pygame.draw.circle(screen, "yellow", coord, 2)


    screen.blit(spaceship_img, (ship_x_pos, ship_y_pos))

    # UPDATE SCORE AND ENEMIES PAST
    writeText("SCORE: " + str(score), 50, 20, 20, "white")
    writeText("ENEMIES PAST: " + str(enemies_past), 87, 40, 20, "white")

    # DRAW ENEMIES
    for enemy in enemies:
        if enemy.y > 875:
            enemy.reset()
            enemies_past += 1
        screen.blit(enemy_img, (enemy.getX(), enemy.getY()))
        enemy.y += enemy.getSpeed()
        if abs(enemy.getX() - ship_x_pos) <= 30 and abs(enemy.getY() - ship_y_pos) <= 30:
            screen.fill((235, 119, 110))
            writeText("You Lost!", 350, 400, 50, "black")
            writeText("Score: " + str(score), 350, 450, 50, "black")
            writeText("Press Enter to Go Again!", 350, 500, 30, "black")
            pygame.event.clear()
            r = True
            while r:
                event = pygame.event.wait()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        enemies, ship_x_pos, ship_y_pos, score, enemies_past = restartGame(enemies, ship_x_pos, ship_y_pos)
                        r = False
                if event.type == pygame.QUIT:
                    running = False
                    r = False


    # DRAW BULLETS
    for bullet in bullets:
        pygame.draw.circle(screen, "red", (bullet.getX(), bullet.getY()), bullet.getRadius())
        bullet.y -= bullet.getSpeed()
        for enemy in enemies:
            if abs(bullet.getX() - enemy.getX()) <= 30 and abs(bullet.getY() - enemy.getY()) <= 30: # enemy radius = 25; bullet radius = 5; so it can have an offset of 30
                if bullet in bullets:
                    bullets.remove(bullet)
                enemy.reset()
                score += 10
        if bullet.getY() <= 0 and bullet in bullets:
            bullets.remove(bullet)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and ship_y_pos > 0:
        ship_y_pos -= 15 
    if keys[pygame.K_s] and ship_y_pos < 850:
        ship_y_pos += 15
    if keys[pygame.K_a] and ship_x_pos > 25:
        ship_x_pos -= 15 
    if keys[pygame.K_d] and ship_x_pos < 645:
        ship_x_pos += 15
    if keys[pygame.K_m] and not pressed: # TODO: decrease fire rate
        bullets.append(Bullet(ship_x_pos + 25, ship_y_pos))
        pressed = True
    if not keys[pygame.K_m]:
        pressed = False
    if enemies_past > 3:
        screen.fill((235, 119, 110))
        writeText("You Lost!", 350, 400, 50, "black")
        writeText("Score: " + str(score), 350, 450, 50, "black")
        writeText("Press Enter to Go Again!", 350, 500, 30, "black")
        pygame.event.clear()
        r = True
        while r:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    enemies, ship_x_pos, ship_y_pos, score, enemies_past = restartGame(enemies, ship_x_pos, ship_y_pos)
                    r = False
            if event.type == pygame.QUIT:
                running = False
                r = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()




