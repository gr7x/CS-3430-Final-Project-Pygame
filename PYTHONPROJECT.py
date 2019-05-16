import pygame
import os

from random import randint

pygame.init()


####################################### INITAL VARIABLES###################################
# please migrate this 2014 project to object oriented structure

## SET COLOR VALUES
GRAY = (245, 245, 245)
GOLD = (255, 215, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)

## LOAD BACKGROUND IMAGES
gameDisplay = pygame.display.set_mode((1159,659))
pygame.display.set_caption('Food Run')
background_image = pygame.image.load("resources/imgs/backgrounds/street1.png").convert()
intro_image = pygame.image.load("resources/imgs/backgrounds/intro.png").convert()
map2 = pygame.image.load("resources/imgs/maps/map2.png").convert()
map3 = pygame.image.load("resources/imgs/maps/df.png").convert()
spa = pygame.image.load("resources/imgs/maps/pool.png").convert()

## load male images
manUL = pygame.image.load('resources/imgs/characters/male/pl1UpLeft.png')
manUR = pygame.image.load('resources/imgs/characters/male/pl1UpRight.png')
manDL = pygame.image.load('resources/imgs/characters/male/pl1DownLeft.png')
manDR = pygame.image.load('resources/imgs/characters/male/pl1DownRight.png')

## load woman images
womanUL = pygame.image.load('resources/imgs/characters/female/pl2UL.png')
womanUR = pygame.image.load('resources/imgs/characters/female/pl2UR.png')
womanDL = pygame.image.load('resources/imgs/characters/female/pl2DL.png')
womanDR = pygame.image.load('resources/imgs/characters/female/pl2DR.png')

## load object images
banana = pygame.image.load('resources/imgs/items/banana.png')
bacon = pygame.image.load('resources/imgs/items/bacon.png')
kfc = pygame.image.load("resources/imgs/items/kfc.png")
wand = pygame.image.load("resources/imgs/items/potion.png")
rocks = pygame.image.load("resources/imgs/items/mo.png")

## SETUP FONT
font = pygame.font.SysFont(None, 45)
font1 = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()

## SETUP TIME
minutes = 0
seconds = 0
milliseconds = 0

##PLAYER MODE SETUP
character = "Two Player"

## INITALOZE BACKGROUND VARIABLE
background = background_image

## INITALIZE MAN VALUES
manX = 50
manY = 50
manChangeX = 0
manChangeY = 0
manDirY = "down"
manDirX = "right"
manSpeed = 11
manScore = 00
mScoreLabel = "GOLD"


## INITALIZE WOMAN VALUES
womanX =200
womanY =200
womanChangeY = 0
womanChangeX = 0
womanDirY = "down"
womanDirX = "left"
womanSpeed = 11
womanScore = 00
wScoreLabel = "GOLD"


## INITALIZE GAME VALUES
gameExit= False
level = 1
round1 = True
round2 = False
round3 = False


## INITALIZE ITEMS
bananaPick = False
bX = 610
bY = 475

baconPick = False
baX = 1035
baY = 250

kfcX = randint(75, 775)
kfcY = randint(75, 500)
kfcPick = False
chicken = True

wX = randint(75, 775)
wY = randint(75, 470)
wPick = False

wFrog = False
mFrog = False

bob = False
moX = randint(75, 775)
moY = randint(75, 480)
moPick = False
whoIsMoses = "none"
mLevel = 0

select = 1
prevSelect = 1
Intro = True


### SET WIN SCORE
win = 500
winChange = 0

##########################END INITAL VARIABLES################

#### METHODS####


## METHOD TO DISPLAY TEXT TO THE SCREEN
def score_counter(msg, color, x, y):
    if(color == GOLD):
        screen_text = font1.render(msg, True, color)
    else:
        screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x, y])

def initalize():
    score_counter("Initalizing.", WHITE, 400, 257)
    pygame.time.delay(400)
    score_counter("Initalizing.", WHITE, 400, 257)
    pygame.display.update()
    pygame.time.delay(250)
    gameDisplay.fill(BLACK)
    score_counter("Initalizing..", WHITE, 400, 257)
    pygame.display.update()
    pygame.time.delay(250)
    score_counter("Initalizing...", WHITE, 400, 257)
    pygame.display.update()
    pygame.time.delay(300)

def closing():
            gameDisplay.fill(BLACK)
            score_counter("Closing....", WHITE, 400, 257)
            pygame.time.delay(350)
            score_counter("Closing...", WHITE, 400, 257)
            pygame.display.update()
            pygame.time.delay(250)
            gameDisplay.fill(BLACK)
            score_counter("Closing..", WHITE, 400, 257)
            pygame.display.update()
            pygame.time.delay(250)
            score_counter("Closing.", WHITE, 400, 257)
            pygame.display.update()
            pygame.time.delay(250)
            gameDisplay.blit(intro_image,(0,0))
            score_counter("Game Over", GOLD, 455, 210)

def music():
    x = randint (1,7)
    if(x == 1):
        pygame.mixer.music.load("resources/audio/soundtrack/tec.mp3")
    elif(x==2):
        pygame.mixer.music.load("resources/audio/soundtrack/fl.wav")
    elif(x==3):
        pygame.mixer.music.load("resources/audio/soundtrack/BEAST1.wav")
    elif(x==4):
        pygame.mixer.music.load("resources/audio/soundtrack/46.wav")
        background = spa
    elif(x==5):
        pygame.mixer.music.load("resources/audio/soundtrack/A.wav")
    elif(x==6):
        pygame.mixer.music.load("resources/audio/soundtrack/WT2.wav")
    elif(x==7):
        pygame.mixer.music.load("resources/audio/soundtrack/PS2.wav")

    gameDisplay.fill(BLACK)
    pygame.mixer.music.play(-1,0)

def manScoreUP(womanScore, manScore):
    score_counter("Player 2:   " + str(womanScore), WHITE, 175, 17)
    score_counter("Player 1:   " + str(manScore), GOLD, 785, 13)

def womanScoreUP(manScore, womanScore):
    score_counter("Player 2:   " + str(womanScore), GOLD, 155, 13)
    score_counter("Player 1:   " + str(manScore), WHITE, 785, 17)

def introMain():
    score_counter("FOOD RUN", GOLD, 450, 180)
    score_counter("Press i: To View Instructions", BLACK, 400, 257)
    score_counter("Press n: To Select Player Mode", WHITE, 400, 307)
    score_counter("Press w: To Set Winning Points", BLACK, 400, 357)
    score_counter("Press s to Start", BLACK, 450, 457)

def instructionMenu():
    score_counter("Instructions", GOLD, 455, 17)
    score_counter("Use the arrow keys to move the character(s) to collect", BLACK, 180, 80)
    score_counter("food items scattered throughout the maps to earn points. If two", BLACK, 180, 120)
    score_counter("player mode is enabled the second player uses the keys (a)" , BLACK, 180, 160)
    score_counter("to go left, (d) up, (w) right, and (x) to move down. ", BLACK, 180, 200)
    score_counter("Press M to return to the main menu", BLACK, 375, 517)

def playerScreen(character, womanDL, manDR):
    score_counter("Players Select", GOLD, 455, 17)
    score_counter("Player mode:  "+ character.upper(), BLACK, 400, 110)
    score_counter("Press up for two player left for single woman or right single player man", BLACK, 50, 415)
    score_counter("Press M to return to the menu", BLACK, 375, 517)
    if(character == "Two Player"):
       gameDisplay.blit(womanDL,(600,150))
       gameDisplay.blit(manDR,(400,150))
    elif(character == "woman"):
        gameDisplay.blit(womanDL,(530,180))
    elif(character == "man"):
        gameDisplay.blit(manDR,(420,150))

def winScreen(win):
    score_counter("Win Limit", GOLD, 455, 17)
    score_counter("Points to Win:  ", BLACK, 430, 110)
    score_counter(str(win), GOLD, 650, 105)
    score_counter("Use the the up and down arrow keys to change the win limit", BLACK, 150, 200)
    score_counter("Press M to return to the menu", BLACK, 375, 517)


def checkForWin(manScore, womanScore, character):
    if((manScore + womanScore) >= win):
        gameDisplay.blit(intro_image,(0,0))
        score_counter("SCORE ACHIEVED!", GOLD, 375, 210)
        if(character == "Two Player"):
            pygame.display.update()
            if(manScore > womanScore):
                score_counter("Player One Lead", BLACK, 440, 280)

            else:
                score_counter("Player Two Lead", BLACK, 440, 280)

        score_counter("Final Score:  " + str(womanScore + manScore), BLACK, 455, 340)
        pygame.display.update()
        pygame.time.delay(2500)
        gameExit = True
        pygame.quit()
        quit()
        return gameExit


## VARIABLES FOR INTRO SCREEN
instructionScreen = False
pScreen = False
pointS = False


########INTRO SCREEN LOOP#########
while Intro:
        gameDisplay.blit(intro_image,(0,0))
        pygame.mixer.music.get_busy()

        ### CHECKS TO CHOOSE WHICH SCREEN TO DISPLAY ### PULL BASED ON BOOL VALUES
        if not (pScreen or instructionScreen or pointS):
            introMain()
        elif(instructionScreen):
            instructionMenu()
        elif(pScreen):
            playerScreen(character, womanDL, manDR)
        elif(pointS):
            winScreen(win)


        ### Intro EVENTS  ####################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    if(instructionScreen):
                        instructionScreen = False
                    else:
                        instructionScreen = True
                if event.key == pygame.K_n:
                    if(pScreen):
                        pScreen = False
                    else:
                        pScreen = True
                if event.key == pygame.K_m:
                    pScreen = False
                    instructionScreen = False
                    pointS = False
                if event.key == pygame.K_w:
                    if(pointS):
                        pointS = False
                    else:
                        pointS = True
                if event.key == pygame.K_UP:
                    if(pointS):
                        winChange += 50

                    elif(pScreen):
                        character = "Two Player"
                if event.key == pygame.K_DOWN:
                    if(pointS):
                        winChange -= 50

                if event.key == pygame.K_LEFT:
                    if(pScreen):
                        character = "man"
                if event.key == pygame.K_RIGHT:
                    if(pScreen):
                        character = "woman"
                if event.key == pygame.K_s:
                    Intro = False
                if event.key == pygame.K_g:
                    if(pointS):
                        x = 7
                        womanSpeed = 20
                        manSpeed = 20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if(pointS):
                        winChange = 0

                    elif(pScreen):
                        character = "Two Player"
                if event.key == pygame.K_DOWN:
                    if(pointS):
                        winChange = 0
        ## update points to win

        win += winChange
        if(pointS):
            pygame.time.delay(175)
        if(win < 50):
            win = 10500

        elif(win > 10500):
            win = 50

        pygame.display.update()
        clock.tick(60)

### INITALIZE MUSIC SELECTION FOR GAME PLAY


music()

initalize()




## ## ## MAIN GAME LOOP ## ## ##

while not gameExit:
    pygame.mixer.music.get_busy()

    #######EVENTS########
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ## CLOSING DISPLAY ## POSSIBLY PULL TO A METHOD
            pygame.mixer.music.play(-1,0)
            closing()
            if(character == "Two Player"):
                pygame.display.update()
                if(manScore > womanScore):
                    score_counter("Player One Lead", BLACK, 440, 280)

                else:
                    score_counter("Player Two Lead", BLACK, 440, 280)

            score_counter("Final Score:  " + str(womanScore + manScore), BLACK, 460, 340)
            pygame.display.update()
            pygame.time.delay(2500)
            gameExit = True
            ## END CLOSING DISPLAY

         ## CHECK GAME KEY EVENTS ##
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                manChangeX += manSpeed
                manDirX = "right"
                #print("Right Key Pressed")
            if event.key == pygame.K_LEFT:
                #print("Left Key Pressed")
                manChangeX -= manSpeed
                manDirX = "left"
            if event.key == pygame.K_UP:
                #print("Up Key Pressed")
                manChangeY -= manSpeed
                manDirY = "up"
            if event.key == pygame.K_DOWN:
                #print("Down key Pressed")
                manChangeY += manSpeed
                manDirY = "down"
            if event.key == pygame.K_a:
                #print("A Key Pressed")
                womanChangeX -= womanSpeed
                womanDirX = "left"
            if event.key == pygame.K_d:
                #print("D Key Pressed")
                womanChangeX += womanSpeed
                womanDirX = "right"
            if event.key == pygame.K_w:
                #print("W Key Pressed")
                womanChangeY -= womanSpeed
                womanDirY = "up"
            if event.key == pygame.K_x:
                #print("Z Key Pressed")
                womanChangeY += womanSpeed
                womanDirY = "down"
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
                sys.exit(0)
        ## CHECK KEYUP EVENTS
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                manChangeX = 0
                manDirX = "right"
                #print("Right Key Pressed")
            if event.key == pygame.K_LEFT:
                #print("Left Key Pressed")
                manChangeX = 0
                manDirX = "left"
            if event.key == pygame.K_UP:
                #print("Up Key Pressed")
                manChangeY = 0
                manDirY = "up"
            if event.key == pygame.K_DOWN:
                #print("Down key Pressed")
                manChangeY = 0
                manDirY = "down"
            if event.key == pygame.K_a:
                womanChangeX = 0
                #print("A Key Pressed")
                #womanChangeX = 0
                womanDirX = "left"
            if event.key == pygame.K_d:
                #print("D Key Pressed")
                womanChangeX = 0
                womanDirX = "right"
            if event.key == pygame.K_w:
                #print("W Key Pressed")
                womanChangeY = 0
                womanDirY = "up"
            if event.key == pygame.K_x:
                #print("Z Key Pressed")
                womanChangeY = 0
                womanDirY = "down"

    ####update movment POSSIBLY PULL TO A METHOD
    manX += manChangeX
    manY += manChangeY
    womanX += womanChangeX
    womanY += womanChangeY

    ## CHECK IF WIN EXTRACT TO METHOD
    checkForWin(manScore, womanScore, character)
    ## END CHECK IF WIN METHOD

    #### render background
    gameDisplay.blit(background, (0,0))


    ### RAISE LEVEL METHOD
    if(baconPick == True and bananaPick == True and kfcPick):
        score_counter("NEXT LEVEL", GOLD, 440, 210)
        pygame.display.update()
        pygame.time.delay(550)
        level += 1
        bob = False
        manX = randint(2 ,1047)
        manY = randint(5, 400)
        manDirY = "down"
        womanX = randint(2,1047)
        womanY = randint(5, 400)
        womanDirY = "down"

        if(randint(0,14) == randint(0,14)):
           bob = True

        select = randint(0,5)
        while select == prevSelect:
            select = randint(0,5)

        ## Randomly place objects within contstraints ##
        if(select == 1):
            background = background_image
        elif(select == 2):
            background = map3
            bx = randint(-40, 1000)
            bY = randint(26, 500)
            baX = randint(-40, 1000)
            baY = randint(26, 500)
            kfcX = randint(-40, 1000)
            kfcY = randint(26, 500)
        elif(select == 3):
            background = map2
            bx = randint(155, 750)
            bY = randint(100, 450)
            baX = randint(155, 750)
            baY = randint(100, 450)
            kfcX = randint(155, 750)
            kfcY = randint(100, 450)
        elif(select == 4):
            background = spa
            bx = randint(-40, 1000)
            bY = randint(26, 500)
            baX = randint(-40, 1000)
            baY = randint(26, 500)
            kfcX = randint(-40, 1000)
            kfcY = randint(26, 500)

        prevSelect = select
        baconPick = False
        bananaPick = False
        kfcPick = False
        kfcX = randint(75, 775)
        kfcY = randint(75, 500)




## blit objects


## check boundaries PULL TO METHOD?

    if(background == map2):
        ## make a get and set to modify these values
        if(manX > 800):
            manX = 800
        elif(manX < 26):
            manX = 26
        if(manY < 80):
            manY = 80
        elif(manY > 450):
            manY = 450

        if(womanX > 790):
            womanX = 790
        elif(womanX <= 146):
            womanX = 146
        if(womanY <= 40):
            womanY = 40
        elif(womanY >= 450):
            womanY = 450
    else:
        if(manX > 1049):
            manX = -175
        elif(manX <= -185):
            manX = 1049
        if(manY <= -170):
            manY = 540
        elif(manY >= 572):
            manY = -160

        if(womanX > 1130):
            womanX = -79
        elif(womanX <= -73):
            womanX = 1130
        if(womanY <= -170):
            womanY = 560
        elif(womanY >= 630):
            womanY = -104




## blit players
## blit man image ## VARIABLES CHARACTER AND DIRECTION X AND Y COORDONATES
    if(character == "Two Player" or character == "man"):
        if(manDirY == "down" and manDirX == "left"):
            gameDisplay.blit(manDL,(manX,manY))
        elif(manDirY == "down" and manDirX == "right"):
            gameDisplay.blit(manDR,(manX,manY))
        elif(manDirY == "up" and manDirX == "left"):
            gameDisplay.blit(manDL,(manX,manY))
        elif(manDirY == "up" and manDirX == "right"):
            gameDisplay.blit(manDR,(manX,manY))
    if (character == "woman"):
        if(manDirY == "down" and manDirX == "left"):
            gameDisplay.blit(womanDL,(manX,manY))
        elif(manDirY == "down" and manDirX == "right"):
            gameDisplay.blit(womanDR,(manX,manY))
        elif(manDirY == "up" and manDirX == "left"):
            gameDisplay.blit(womanDL,(manX,manY))
        elif(manDirY == "up" and manDirX == "right"):
            gameDisplay.blit(womanDR,(manX,manY))
    if(mFrog and randint(0,100) == 24):
        score_counter("**Croak*", GOLD, manX, manY)
        pygame.time.delay(200)

## blit woman image
    if(character == "Two Player"):
        if(womanDirY == "down" and womanDirX == "left"):
            gameDisplay.blit(womanDL,(womanX,womanY))
        elif(womanDirY == "down" and womanDirX == "right"):
            gameDisplay.blit(womanDR,(womanX,womanY))
        elif(womanDirY == "up" and womanDirX == "left"):
            gameDisplay.blit(womanDL,(womanX,womanY))
        elif(womanDirY == "up" and womanDirX == "right"):
            gameDisplay.blit(womanDR,(womanX,womanY))

    if(wFrog and randint(0,100) == 24):
        score_counter("**ribbit*", GOLD, womanX, womanY)
        pygame.time.delay(200)


    ###check if items remain
        ## CHECK BANANA STATUS
    if(bananaPick == False):
        if(randint(0, 100) == randint(0,100)):
             bX = randint(-40, 1000)
             bY = randint(26, 500)
        gameDisplay.blit(banana,(bX,bY))
        if manX> bX and manX < bX + 70 or manX + 70 > bX and manX + 70 < bX:
                if manY >bY and manY < bY + 70 or manY + 70 > bY and manY + 70 < bY:
                    bananaPick = True
                    manScore += 3

                    score_counter("+3", GOLD, bX, bY)


        if(character == "Two Player"):
            if womanX> bX and womanX < bX + 70 or womanX + 70 > bX and womanX + 70 < bX:

                    if womanY >bY and womanY < bY + 70 or womanY + 70 > bY and womanY + 70 < bY:

                        womanScore += 3
                        bananaPick = True
                        score_counter("+3", GOLD, bX, bY)


    ## CHECK BACON STATUS
    if(baconPick == False):
        gameDisplay.blit(bacon,(baX,baY))
        if(randint(0, 80) == randint(0,80)):
             baX = randint(-40, 1000)
             baY = randint(26, 500)
        if manX> baX and manX < baX + 100 or manX + 100 > baX and manX + 100 < baX:
                if manY >baY and manY < baY + 150 or manY + 150 > baY and manY + 150 < baY:
                    baconPick = True
                    manScore += 5

                    score_counter("+5", GOLD, baX, baY)

        if(character == "Two Player"):
            if womanX> baX and womanX < baX + 100 or womanX + 100 > baX and womanX +100 < baX:
                    if womanY >baY and womanY < baY + 150 or womanY + 150 > baY and womanY + 150 < baY:
                        womanScore += 5
                        baconPick = True
                        score_counter("+5", GOLD, baX, baY)


    ## CHECK KFC STATUS ##
    if(kfcPick == False):
        if(randint(0, 80) == randint(0,80)):
             kfcX = randint(-40, 1000)
             kfcY = randint(26, 500)
        gameDisplay.blit(kfc,(kfcX,kfcY))
        if manX> kfcX and manX < kfcX + 70 or manX + 70 > kfcX and manX + 70 < kfcX:
                if manY >kfcY and manY < kfcY + 70 or manY + 70 > kfcY and manY + 70 < kfcY:
                    kfcPick = True
                    manScore += 25

                    score_counter("YUM +25", GOLD, kfcX, kfcY)

        if(character == "Two Player"):
            if womanX> kfcX and womanX < kfcX + 70 or womanX + 70 > kfcX and womanX + 70 < kfcX:
                    if womanY >kfcY and womanY < kfcY + 70 or womanY + 70 > kfcY and womanY + 70 < kfcY:
                        womanScore += 25
                        kfcPick = True
                        score_counter("YUM +25", GOLD, kfcX, kfcY)

    ## CHECK POTION STATUS
    if(level == 5 or level == 10 or level == 15):
        if(wPick == False):
            if(randint(0, 40) == randint(0,40)):
                wX = randint(-40, 1000)
                wY = randint(26, 500)
            gameDisplay.blit(wand,(wX,wY))
            if manX> wX and manX < wX + 70 or manX + 70 > wX and manX + 70 < wX:
                    if manY >wY and manY < wY + 70 or manY + 70 > wY and manY + 70 < wY:
                        wPick = True

                        score_counter("*Croak*", GOLD, wX, wY)
                        manUL = pygame.image.load('resources/imgs/characters/frog/frogL.png')
                        manUR = pygame.image.load('resources/imgs/characters/frog/frog.png')
                        manDL = pygame.image.load('resources/imgs/characters/frog/frogL.png')
                        manDR = pygame.image.load('resources/imgs/characters/frog/frog.png')
                        manChangeY = 4
                        mFrog = True

            if(character == "Two Player"):
                if womanX> wX and womanX < wX + 70 or womanX + 70 > wX and womanX + 70 < wX:
                        if womanY >wY and womanY < wY + 70 or womanY + 70 > wY and womanY + 70 < wY:
                            wPick = True
                            score_counter("**ribbit*", GOLD, wX, wY)
                            womanUL = pygame.image.load('resources/imgs/characters/frog/frogL.png')
                            womanUR = pygame.image.load('resources/imgs/characters/frog/frog.png')
                            womanDL = pygame.image.load('resources/imgs/characters/frog/frogL.png')
                            womanDR = pygame.image.load('resources/imgs/characters/frog/frog.png')
                            womanChangeY = 4
                            wFrog = True
    ## CHANGE BACK FROM FROG
    elif(level == 8 or level == 13 or level == 18):

        if (wPick == True):
            ## return
            wPick = False
            manUL = pygame.image.load('resources/imgs/characters/male/pl1UpLeft.png.png')
            manUR = pygame.image.load('resources/imgs/characters/male/pl1UpRight.png')
            manDL = pygame.image.load('resources/imgs/characters/male/pl1DownLeft.png')
            manDR = pygame.image.load('resources/imgs/characters/male/pl1DownRight.png')
            manChangeY = 0
            mFrog = False

            ## load woman images
            womanUL = pygame.image.load('resources/imgs/characters/female/pl2UL.png')
            womanUR = pygame.image.load('resources/imgs/characters/female/pl2UR.png')
            womanDL = pygame.image.load('resources/imgs/characters/female/pl2DL.png')
            womanDR = pygame.image.load('resources/imgs/characters/female/pl2DR.png')
            womanChangeY = 0
            wFrog = False

    ## MAKE PLAYER MOSES
    if(bob):
        if(moPick == False):
            if(randint(0, 40) == randint(0,40)):
                moX = randint(-40, 1000)
                moY = randint(26, 500)
            gameDisplay.blit(rocks,(moX, moY))
            if manX> moX and manX < moX + 70 or manX + 70 > moX and manX + 70 < moX:
                    if manY >moY and manY < moY + 70 or manY + 70 > moY and manY + 70 < moY:
                        moPick = True
                        manUL = pygame.image.load('resources/imgs/characters/moL.png')
                        manUR = pygame.image.load(resources/imgs/characters/'moR.png')
                        manDL = pygame.image.load('resources/imgs/characters/moL.png')
                        manDR = pygame.image.load('resources/imgs/characters/moR.png')
                        score_counter("HOLY MOSES!!", GOLD, 440, 210)
                        pygame.display.update()
                        #pygame.time.delay(450)
                        manSpeed = 25
                        whoISMoses = "man"
                        mLevel = level


            if(character == "Two Player"):
                if womanX> moX and womanX < moX + 70 or womanX + 70 > moX and womanX + 70 < moX:
                        print("THIS ONE WORKED")
                        if womanY >moY and womanY < moY + 70 or womanY + 70 > wY and womanY + 70 < moY:
                            #print("SECOND")
                            moPick = True
                            score_counter("HOLY MOSES!!", GOLD, 440, 210)
                            pygame.display.update()
                            pygame.time.delay(450)
                            #print("woman got banana")
                            womanUL = pygame.image.load('resources/imgs/characters/moL.png')
                            womanUR = pygame.image.load('resources/imgs/characters/moR.png')
                            womanDL = pygame.image.load('resources/imgs/characters/moL.png')
                            womanDR = pygame.image.load('resources/imgs/characters/moR.png')
                            womanSpeed = 25
                            whoIsMoses ="woman"
                            pygame.display.update()
                            mLevel = level

    ## RETURN PLAYER FROM MOSES
    elif((moPick == True and (level - mLevel) == randint(4,8)) or (level - mLevel) > randint(8,11)):

        if (moPick == True):
            manUL = pygame.image.load('resources/imgs/characters/male/pl1UpLeft.png')
            manUR = pygame.image.load('resources/imgs/characters/male/pl1UpRight.png')
            manDL = pygame.image.load('resources/imgs/characters/male/pl1DownLeft.png')
            manDR = pygame.image.load('resources/imgs/characters/male/pl1DownRight.png')
            moPick = False
            manSpeed = 11

            ## load woman images
            womanUL = pygame.image.load('resources/imgs/characters/female/pl2UL.png')
            womanUR = pygame.image.load('resources/imgs/characters/female/pl2UR.png')
            womanDL = pygame.image.load('resources/imgs/characters/female/pl2DL.png')
            womanDR = pygame.image.load('resources/imgs/characters/female/pl2DR.png')
            moPick = False
            womanSpeed = 11

    x = "GOLD"
    if(character == "Two Player"):
        if(manScore > womanScore):
            manScoreUP(manScore, womanScore)
        else:
            womanScoreUP(manScore,womanScore)

    ## PRINT SCORES - DISPLAY
    score_counter("Team Score:  " + str(womanScore + manScore), GOLD, 425, 610)
    score_counter("Level:  " + str(level), GRAY, 40, 610)
    score_counter("Score to Win:  " + str(win), GRAY, 860, 610)


    ##DISPLAY CLOCK
    if milliseconds > 500:
        seconds += 1
        milliseconds -= 500
    if seconds > 60:
        minutes += 1
        seconds -= 60
    score_counter("  "+str(minutes)+ " min: " +str(seconds)+" sec", GRAY, 485, 35)
    milliseconds += clock.tick_busy_loop(60)
    pygame.display.update()
    clock.tick(60)

    ## ## ## END GAME LOOP ## ## ##




## END GAME AFTER WHILE LOOP
pygame.quit()
quit()
