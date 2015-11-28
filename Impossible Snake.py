# Impossible Snake Game 
# Made By JBalisticMC

import pygame
import time
import random

pygame.init()

pygame.mixer.music.load("music_for_pops.wav")

white = (255,255,255)
red = (255,0,0)
green = (0,155,0)
purple = (215,19,196)
black = (0,0,0)
light_blue = (62,221,230)

display_width = 700
display_height = 500

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Impossible Snake (Alpha)')

icon = pygame.image.load('snake_head.png')
pygame.display.set_icon(icon)

bg = pygame.image.load("bg.jpg")

img = pygame.image.load('snake_head.png')
appleimg = pygame.image.load('apple.png')

#3:47 t 31


clock = pygame.time.Clock()

AppleThinkness = 30
block_size = 20
FPS = 15

direction = "right" 

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():

    pygame.mixer.music.pause()
    
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_r:
                   paused = False
                   pygame.mixer.music.unpause()

                   
               elif event.key == pygame.K_q:
                   pygame.quit()
                   quit()
                   
        message_to_screen("Paused",
                          red,
                          -100,
                          size="large")


        message_to_screen("Press R to continue or Q to quit.",
                         red,
                         25)

        pygame.display.update()
        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score), True, red)
    gameDisplay.blit(text, [0,0])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThinkness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThinkness))#/10.0)*10.0


    return randAppleX,randAppleY




def game_intro():

    ######################################################
    
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Impossible Snake",
                          light_blue,
                          -100,
                          size="medium")
        message_to_screen("The objective of the game is to eat red apples",
                          red,
                          -30)

        message_to_screen("The more apples you eat, the longer you get!",
                          red,
                          10)

        message_to_screen("If you run into your self, or the edges, YOU DIE!!",
                          red,
                          50)

        message_to_screen("Press R to play or Q to quit.",
                          green,
                          180)

        pygame.display.update()
        clock.tick(15)
             
        


def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)


        
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width / 2),(display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)
    

def gameLoop():
    global direction
    pygame.mixer.music.play(-1)

    
    direction = 'right'
    gameExit = False
    gameOver = False
    
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()

   

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            pygame.mixer.music.stop()
            message_to_screen("Game over!",
                              red,
                              y_displace=-50,
                              size="large")
            
            message_to_screen("Press R to play again or Q to quit",
                              green,
                              50,
                              size="small")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_d:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_w:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_s:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0

            
        lead_x += lead_x_change
        lead_y += lead_y_change
        

        gameDisplay.fill(white)

        
        #pygame.draw.rect(gameDisplay, red,[randAppleX, randAppleY, AppleThinkness, AppleThinkness])
        
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))


        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList [0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
            
        snake(block_size, snakeList)

        score ( snakeLength-1)

        
        pygame.display.update()

##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThinkness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThinkness:
##                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
##                snakeLength += 3


##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThinkness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThinkness:
##                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
##                snakeLength += 3

        if lead_x > randAppleX and lead_x < randAppleX + AppleThinkness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThinkness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThinkness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 4

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThinkness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 4

            

            
        

        
            
            

        

        clock.tick(FPS)
        
    pygame.quit()
    quit()
game_intro()
gameLoop()

