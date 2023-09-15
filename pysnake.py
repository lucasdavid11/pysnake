import pygame
from pygame.locals import *
from sys import exit
from random import randrange
import os
import time

pygame.init()

def loadIcon():
    imagesdirectory = os.path.join(os.getcwd(), 'images')
    icon = os.path.join(imagesdirectory, 'artsnake.png')
    icon = pygame.image.load(icon).convert()
    pygame.display.set_icon(icon)

#LOAD MENU IMAGES
def loadMenuImages():
    imagesdirectory = os.path.join(os.getcwd(), 'images')
    titlepysnakedirectory = os.path.join(imagesdirectory, 'titlepysnake.png')
    artsnakedirectory = os.path.join(imagesdirectory, 'artsnake.png')
    playbuttondirectory = os.path.join(imagesdirectory, 'playbutton.png')

    artsnakedirectory = pygame.image.load(artsnakedirectory).convert()
    artsnake_rect = artsnakedirectory.get_rect()
    artsnake_rect.midtop = (50, 120)
    window.blit(artsnakedirectory, artsnake_rect)

    titlepysnakedirectory = pygame.image.load(titlepysnakedirectory).convert()
    titlepysnake_rect = titlepysnakedirectory.get_rect()
    titlepysnakedirectory = pygame.transform.scale(titlepysnakedirectory, (640, 480))
    titlepysnake_rect.midtop = (220, -50)
    window.blit(titlepysnakedirectory, titlepysnake_rect)

    playbuttondirectory = pygame.image.load(playbuttondirectory).convert()
    playbuton_rect = titlepysnakedirectory.get_rect()
    playbuton_rect.midtop = (520, 200)
    window.blit(playbuttondirectory, playbuton_rect)


#LOAD GAME IMAGES
def loadGameImages():
    imagesdirectory = os.path.join(os.getcwd(), 'images'
                                   )
    titlepysnakedirectory = os.path.join(imagesdirectory, 'titlepysnake.png')
    titlepysnakedirectory = pygame.image.load(titlepysnakedirectory).convert()
    titlepysnake_rect = titlepysnakedirectory.get_rect()
    titlepysnakedirectory = pygame.transform.scale(titlepysnakedirectory, (480, 360))
    titlepysnake_rect.midtop = (293, -75)
    window.blit(titlepysnakedirectory, titlepysnake_rect)

    pygame.draw.rect(window, secundarywindowcolor, (80, 60, 480, 360))  # 24x18
    pygame.draw.rect(window, (0, 0, 0), (75, 60, 5, 360))
    pygame.draw.rect(window, (0, 0, 0), (560, 60, 5, 360))
    pygame.draw.rect(window, (0, 0, 0), (75, 55, 490, 5))
    pygame.draw.rect(window, (0, 0, 0), (75, 420, 490, 5))

    for j in range(79, 400, 20):
        for i in range(99, 540, 20):
            pygame.draw.rect(window, (132, 124, 172), (i, j, 2, 2))


#PUTS THE TEXTS IN SCREEN
def gameMessagesBlit():
    pointsmessage = f'Points: {points}'
    pointsformatmessage = font.render(pointsmessage, True, (0, 0, 0))

    restartmessage = 'Press "R" to restart'
    restartformatmessage = font1.render(restartmessage, True, (0, 0, 0))

    speedmessage = 'Press "I" or "K" to controll speed'
    speedformatmessage = font1.render(speedmessage, True, (0, 0, 0))

    musicmessage = 'Press "M" to mute'
    musicformatmessage = font1.render(musicmessage, True, (0, 0, 0))

    window.blit(pointsformatmessage, (80, 440))
    if not lose and not win:
        window.blit(musicformatmessage, (280, 430))
        window.blit(restartformatmessage, (280, 445))
        window.blit(speedformatmessage, (280, 460))


#PUT THE EYES IN SCREEN
def loadSnakeEyes():
    if up:
        pygame.draw.circle(window, (255, 0, 0), (xsnake + 5, ysnake + 15), 4)
        pygame.draw.circle(window, (255, 0, 0), (xsnake + 15, ysnake + 15), 4)

    if down:
        pygame.draw.circle(window, (255, 0, 0), (xsnake + 5, ysnake + 5), 4)
        pygame.draw.circle(window, (255, 0, 0), (xsnake + 15, ysnake + 5), 4)

    if right:
        pygame.draw.circle(window, (255, 0, 0), (xsnake + 5, ysnake + 5), 4)
        pygame.draw.circle(window, (255, 0, 0), (xsnake + 5, ysnake + 15), 4)

    if left:
        pygame.draw.circle(window, (255, 0, 0), (xsnake + 15, ysnake + 15), 4)
        pygame.draw.circle(window, (255, 0, 0), (xsnake + 15, ysnake + 5), 4)


#INCREASES THE SIZE OF THE SNAKE
def increasesnake(positions):
    for k in positions:
        pygame.draw.rect(window, snakecolor, (k[0], k[1], bodysize, bodysize))


#WINDOW CONTROL VARIABLES INITIALIZATION
x = 640
y = 480
window = pygame.display.set_mode((x, y))
pygame.display.set_caption('pysnake')
frames = pygame.time.Clock()


#GAME VARIABLES INITIALIZATION
xsnake = (x / 2) - 20
ysnake = (y / 2) - 20
xapple = randrange(80, 540, 20)
yapple = randrange(60, 400, 20)
bg = (40, 63, 21)
snakecolor = (40, 14, 67)
applecolor = (255, 0, 0)
bodysize = 20
secundarywindowcolor = (137, 163, 114)
secundarywindowx = 480
secundarywindowy = 360
lose = 0
win=0


#GAME CONTROL VARIABLES INITIALIZATION
speed = 8
snakesize = 2
positions = []
points = 0


#DIRECTION VARIABLES INITIALIZATION
up = True
down = False
right = False
left = False


#FONT VARIABLES INITIALIZATION
font = pygame.font.SysFont('SF Pixelate', 30, True, False)
font1 = pygame.font.SysFont('SF Pixelate', 14, True, False)
fontmenu = pygame.font.SysFont('SF Pixelate', 24, True, False)
fontlosegame = pygame.font.SysFont('SF Pixelate', 22, True, False)
fontlosegame2 = pygame.font.SysFont('SF Pixelate', 16, True, False)


#MUSIC VARIABLES INITIALIZATION
gamemusic = pygame.mixer.music.load('audios\music.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
winmusic = pygame.mixer.Sound('audios\win.mp3')
losemusic = pygame.mixer.Sound('audios\lose.mp3')
eatapplemusic = pygame.mixer.Sound('audios\eatapple.mp3')
playmusic=True
mute=0


#LOOP VARIABLES INITIALIZATION
menu = True
game = True

finaltime = 0.0

while menu:

    frames.tick(8)
    window.fill(bg)
    mouse = pygame.mouse.get_pos()
    loadIcon()
    loadMenuImages()

    for event in pygame.event.get():
        if event.type == QUIT:
            menu = False
            pygame.quit()
            exit()

        if event.type == KEYUP:
            menu = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (x / 2) - 120 <= mouse[0] <= x / 2 + 240 and y / 2 - 40 <= mouse[1] <= y / 2 + 80:
                menu = False

    playmessage = 'PLAY'
    formatplaymessage = font.render(playmessage, True, (255, 0, 0))

    message = 'Dev by Lucas David Roscziniak'
    formatmessage = fontmenu.render(message, True, (0, 0, 0))

    if (x / 2) - 120 <= mouse[0] <= x / 2 + 240 and y / 2 - 40 <= mouse[1] <= y / 2 + 80:
        pygame.draw.rect(window, (0, 0, 0), [(x / 2) - 120, y / 2 - 40, 240, 80])
        window.blit(formatplaymessage, (x / 2 - 40, y / 2 - 10))

    window.blit(formatmessage, (100, 440))

    pygame.display.flip()

while game:

    if not win:
        if snakesize >= 395:
            win=1
            playmusic=True
            
    loadIcon()
    frames.tick(speed)
    window.fill(bg)
    for event in pygame.event.get():
        if event.type == QUIT:
            game = False
            pygame.quit()
            exit()

        #CONTROL THE KEYBOARD TOUTCH
        if event.type == KEYDOWN:

            starttime = (time.time())

            if finaltime-starttime != 0:

                if event.key == K_s and event.key == K_d:
                    up = True
                    down = False
                    right = False
                    left = False
                if event.key == K_w:
                    if down == False:
                        up = True
                        down = False
                        right = False
                        left = False
                if event.key == K_s:
                    if up == False:
                        up = False
                        down = True
                        right = False
                        left = False
                if event.key == K_d:
                    if left == False:
                        up = False
                        down = False
                        right = True
                        left = False
                if event.key == K_a:
                    if right == False:
                        up = False
                        down = False
                        right = False
                        left = True
                if event.key == K_i:
                    if speed < 20:
                        speed += 1
                if event.key == K_k:
                    if speed > 1:
                        speed -= 1
                if event.key == K_m:
                    if not mute:
                        pygame.mixer.music.set_volume(0)
                        mute=1
                    else:
                        pygame.mixer.music.set_volume(0.2)
                        mute=0


                if event.key == K_r:
                    xsnake = (x / 2) - 20
                    ysnake = (y / 2) - 20
                    xapple = randrange(80, 540, 20)
                    yapple = randrange(60, 400, 20)
                    speed = 8
                    points = 0
                    snakesize = 2
                    positions = []
                    lose = 0
                    win=0
                    winmusic.stop()
                    losemusic.stop()
                    pygame.mixer.music.play(-1)
            finaltime = (time.time())


    #CONTROL SNAKE'S MOVEMENTS
    if up:
        if ysnake <= 60:
            ysnake = secundarywindowy + 60
        ysnake -= bodysize

    if down:
        if ysnake >= secundarywindowy + 40:
            ysnake = 40
        ysnake += bodysize

    if right:
        if xsnake >= secundarywindowx + 60:
            xsnake = 60
        xsnake += bodysize

    if left:
        if xsnake <= 80:
            xsnake = secundarywindowx + 80
        xsnake -= bodysize

    loadGameImages()

    apple = pygame.draw.rect(window, applecolor, (xapple, yapple, bodysize, bodysize), border_radius=10)
    snakehead = pygame.draw.rect(window, snakecolor, (xsnake, ysnake, bodysize, bodysize))


    newposition = []
    newposition.append(xsnake)
    newposition.append(ysnake)
    positions.append(newposition)

    if len(positions) > snakesize:
        del positions[0]

    increasesnake(positions)
    loadSnakeEyes()

    #VERIFY IF SNAKE TOUTCH THE SNAKE
    if not lose and not win:
        if len(positions) > 1:
            for i in range(0, len(positions) - 1):
                if xsnake == positions[i][0] and ysnake == positions[i][1]:
                    lose = 1
                    playmusic=True

    #WHEN YOU LOSE THE GAME
    if not win:
        if lose:
            if playmusic:
                losemusic.play()
                pygame.mixer.music.stop()

            loserect = pygame.draw.rect(window, (132, 124, 172), (80, 60, 480, 360))
            losegaamemessage = "You're horrible. Stop playing NOW"
            losegaameformatmessage = fontlosegame.render(losegaamemessage, True, (0, 0, 0))

            losegaamemessage2 = "Or press R and keep humiliating yourself"
            losegaameformatmessage2 = fontlosegame2.render(losegaamemessage2, True, (0, 0, 0))

            window.blit(losegaameformatmessage, (100, 200))
            window.blit(losegaameformatmessage2, (120, 250))

            playmusic = False
            pygame.display.flip()


    #WHEN YOU WIN THE GAME
    if win:
        if playmusic:
            winmusic.play()
            pygame.mixer.music.stop()

        loserect = pygame.draw.rect(window, (132, 124, 172), (80, 60, 480, 360))
        losegamemessage = "You won. You are the real champ."
        losegameformatmessage = fontlosegame.render(losegamemessage, True, (0, 0, 0))

        losegamemessage2 = "Press R and play again"
        losegameformatmessage2 = fontlosegame2.render(losegamemessage2, True, (0, 0, 0))

        window.blit(losegameformatmessage, (95, 200))
        window.blit(losegameformatmessage2, (200, 250))

        playmusic = False
        pygame.display.flip()

    #WHEN SNAKE EATS AN APPLE
    if snakehead.colliderect(apple):
        eatapplemusic.play()
        points += 1
        xapple = randrange(80, 540, 20)
        yapple = randrange(60, 400, 20)
        applexy = [xapple, yapple]

        if applexy in positions:
            xapple = randrange(80, 540, 20)
            yapple = randrange(60, 400, 20)
            applexy = [xapple, yapple]

        snakesize += 1

    gameMessagesBlit()

    pygame.display.flip()
