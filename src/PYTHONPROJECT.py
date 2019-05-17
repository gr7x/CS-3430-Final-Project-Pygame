import pygame
import os
import GameScreen
import Game
import FontG
import Player
from random import randint
f = FontG.Fonts()
G = Game.G()
gs = GameScreen.GameScreen()

pygame.init()


####################################### INITAL VARIABLES###################################
# please migrate this 2014 project to object oriented structure

## LOAD BACKGROUND IMAGES ... LEave til last find better method if exists
gameDisplay = pygame.display.set_mode((1159,659))
pygame.display.set_caption('Food Run')
background_image = pygame.image.load("../resources/imgs/maps/street1.png").convert()
intro_image = pygame.image.load("../resources/imgs/backgrounds/intro.png").convert()
map2 = pygame.image.load("../resources/imgs/maps/map2.png").convert()
map3 = pygame.image.load("../resources/imgs/maps/df.png").convert()
spa = pygame.image.load("../resources/imgs/maps/pool.png").convert()



## fix later maybe? or leav for speed
clock = pygame.time.Clock()

## SETUP TIME  ... maybe make time class
minutes = 0
seconds = 0
milliseconds = 0

##PLAYER MODE SETUP ... game mode class??
character = "Two Player"

## INITALOZE BACKGROUND VARIABLE ... game mode class
background = background_image

## INITALIZE MAN VALUES ~> PORTING TO PLAYER CLASS
p1=Player.Player(50,50,"right")

mScoreLabel = "GOLD" ## not put in class

#use these somehow in class
manUL = pygame.image.load('../resources/imgs/characters/male/pl1UpLeft.png')
manUR = pygame.image.load('../resources/imgs/characters/male/pl1UpRight.png')
manDL = pygame.image.load('../resources/imgs/characters/male/pl1DownLeft.png')
manDR = pygame.image.load('../resources/imgs/characters/male/pl1DownRight.png')


## INITALIZE WOMAN VALUES ~> PORTING TO PLAYER CLASS
p2=Player.Player(200,200, "left")
p2.dirY = "down" ## not put in class
p2.dirX = "left" ## not put in class
wScoreLabel = "GOLD" ## not put in class

#use these in class somehow LEAVE til later find a good way to do this

womanUL = pygame.image.load('../resources/imgs/characters/female/pl2UL.png')
womanUR = pygame.image.load('../resources/imgs/characters/female/pl2UR.png')
womanDL = pygame.image.load('../resources/imgs/characters/female/pl2DL.png')
womanDR = pygame.image.load('../resources/imgs/characters/female/pl2DR.png')


## INITALIZE GAME VALUES ... move to gameMode class??
gameExit= False
level = 1
round1 = True
round2 = False
round3 = False


## INITALIZE ITEMS ~> making Item class
#banana = Item(610, 475) -- change to this
bananaPick = False
bX = 610
bY = 475

#put in class somehow
banana = pygame.image.load('../resources/imgs/items/banana.png')

#bacon = Item(1035, 250) -- change to this
baconPick = False
baX = 1035
baY = 250
#put in class somehow
bacon = pygame.image.load('../resources/imgs/items/bacon.png')

#kfc = Item(randint(75, 775), randint(75, 500)) -- change to this
kfcX = randint(75, 775)
kfcY = randint(75, 500)
kfcPick = False
#put in class somehow
kfc = pygame.image.load("../resources/imgs/items/kfc.png")

#chicken = Item(1035, 250) -- change to this
chicken = True ## What is this???????

## load object images



wand = pygame.image.load("../resources/imgs/items/potion.png") # change wand to potion in other places
rocks = pygame.image.load("../resources/imgs/items/mo.png")
## ^^ what is this??? is it the ten commandments>>>

# w = Item(randint(75, 775), randint(75, 470)) ~> change to this
wX = randint(75, 775)
wY = randint(75, 470)
wPick = False

wFrog = False # what are these?
mFrog = False # what are these?



## figure out this section below
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

def music(): # move to audio class ... leave here for now then fix
    x = randint (1,7)
    if(x == 1):
        pygame.mixer.music.load("../resources/audio/soundtrack/tec.mp3")
    elif(x==2):
        pygame.mixer.music.load("../resources/audio/soundtrack/fl.wav")
    elif(x==3):
        pygame.mixer.music.load("../resources/audio/soundtrack/BEAST1.wav")
    elif(x==4):
        pygame.mixer.music.load("../resources/audio/soundtrack/46.wav")
        background = spa
    elif(x==5):
        pygame.mixer.music.load("../resources/audio/soundtrack/A.wav")
    elif(x==6):
        pygame.mixer.music.load("../resources/audio/soundtrack/WT2.wav")
    elif(x==7):
        pygame.mixer.music.load("../resources/audio/soundtrack/PS2.wav")

    gameDisplay.fill(f.BLACK)
    pygame.mixer.music.play(-1,0)

def checkForWin(p1Score, p2Score, character): #moveto Game Logic then clean up

    if((p1Score + p2Score) >= win):
        gameDisplay.blit(intro_image,(0,0))
        gs.score_counter("SCORE ACHIEVED!", f.GOLD, 375, 210)
        if(character == "Two Player"):
            pygame.display.update()
            if(p1.score > p2Score):
                gs.score_counter("Player One Lead", f.BLACK, 440, 280)

            else:
                gs.score_counter("Player Two Lead", f.BLACK, 440, 280)

        gs.score_counter("Final Score:  " + str(p1Score + p2Score), f.BLACK, 455, 340)
        pygame.display.update()
        pygame.time.delay(2500)
        gameExit = True
        pygame.quit()
        quit()
        return gameExit


## VARIABLES FOR INTRO SCREEN -- put in intro screen class
instructionScreen = False
pScreen = False
pointS = False


########INTRO SCREEN LOOP#########
while Intro:
        gameDisplay.blit(intro_image,(0,0))
        pygame.mixer.music.get_busy()

        ### CHECKS TO CHOOSE WHICH SCREEN TO DISPLAY ### PULL BASED ON BOOL VALUES
        if not (pScreen or instructionScreen or pointS):
            gs.introMain()
        elif(instructionScreen):
            gs.instructionMenu()
        elif(pScreen):
            gs.playerScreen(character, womanDL, manDR)
        elif(pointS):
            gs.winScreen(win)


        ### Intro EVENTS  #################### FIX LAST besides using classes to change data
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
                        p2.speed = 20 #use classes
                        p1.speed = 20 #use classes
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

gs.initalize()




## ## ## MAIN GAME LOOP ## ## ##

while not gameExit: ## leave here but use classes to chnage data
    pygame.mixer.music.get_busy()

    #######EVENTS########
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ## CLOSING DISPLAY ## POSSIBLY PULL TO A METHOD
            pygame.mixer.music.play(-1,0)
            gs.closing()
            if(character == "Two Player"):
                pygame.display.update()
                if(p1.score > p2.score):
                    gs.score_counter("Player One Lead", f.BLACK, 440, 280)

                else:
                    gs.score_counter("Player Two Lead", f.BLACK, 440, 280)

            gs.score_counter("Final Score:  " + str(p2.score + p1.score), f.BLACK, 460, 340) ## use get functions for score
            pygame.display.update()
            pygame.time.delay(2500)
            gameExit = True
            ## END CLOSING DISPLAY

         ## CHECK GAME KEY EVENTS ##
        if event.type == pygame.KEYDOWN: #FIX LAST besides using classes to change data
            if event.key == pygame.K_RIGHT:
                p1.deltaX += p1.speed
                p1.dirX = "right"
            if event.key == pygame.K_LEFT:
                p1.deltaX -= p1.speed
                p1.dirX = "left"
            if event.key == pygame.K_UP:
                p1.deltaY -= p1.speed
                p1.dirY = "up"
            if event.key == pygame.K_DOWN:
                p1.deltaY += p1.speed
                p1.dirY = "down"
            if event.key == pygame.K_a:
                p2.deltaX -= p2.speed
                p2.dirX = "left"
            if event.key == pygame.K_d:
                p2.deltaX += p2.speed
                p2.dirX = "right"
            if event.key == pygame.K_w:
                p2.deltaY -= p2.speed
                p2.dirY = "up"
            if event.key == pygame.K_s:
                p2.deltaY += p2.speed
                p2.dirY = "down"
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
                sys.exit(0)

        ## CHECK KEYUP EVENTS
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                p1.deltaX = 0
                p1.dirX = "right"
            if event.key == pygame.K_LEFT:
                p1.deltaX = 0
                p1.dirX = "left"
            if event.key == pygame.K_UP:
                p1.deltaY = 0
                p1.dirY = "up"
            if event.key == pygame.K_DOWN:
                p1.deltaY = 0
                p1.dirY = "down"
            if event.key == pygame.K_a:
                p2.deltaX = 0
                p2.deltaX = 0
                p2.dirX = "left"
            if event.key == pygame.K_d:
                p2.deltaX = 0
                p2.dirX = "right"
            if event.key == pygame.K_w:
                p2.deltaY = 0
                p2.dirY = "up"
            if event.key == pygame.K_s:
                p2.deltaY = 0
                p2.dirY = "down"

    ####update movment POSSIBLY PULL TO A METHOD

    #update the following in respective player classes
    p1.x += p1.deltaX
    p1.y += p1.deltaY

    p2.x += p2.deltaX
    p2.y += p2.deltaY
    ## CHECK IF WIN EXTRACT TO METHOD # leave as is just access inside class
    checkForWin(p1.score, p2.score, character)
    ## END CHECK IF WIN METHOD

    #### render background  leave til later to figure out how to setup
    gameDisplay.blit(background, (0,0))


    ### RAISE LEVEL METHOD move to game logic do later, pass Player object to this??
    if(baconPick == True and bananaPick == True and kfcPick):
        gs.score_counter("NEXT LEVEL", f.GOLD, 440, 210)
        pygame.display.update()
        pygame.time.delay(550)
        level += 1
        bob = False
        p1.x = randint(2 ,1047)
        p1.y = randint(5, 400)
        p1.dirY = "down"
        p2.x= randint(2,1047)
        p2.y = randint(5, 400)
        p2.dirY = "down"

        if(randint(0,14) == randint(0,14)):
           bob = True

        select = randint(0,5)
        while select == prevSelect:
            select = randint(0,5)

        ## Randomly place objects within contstraints ##
        ## make a class that does this / seriously clean up
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


## check cross map boundaries PULL TO METHOD?
## leave here for now, but make more precise
    if(background == map2):
        ## make a get and set to modify these values <-- listen to past me
        #(do in getters and setters for respective classes)
        if(p1.x > 800):
            p1.x = 800
        elif(p1.x < 26):
            p1.x = 26
        if(p1.y < 80):
            p1.y = 80
        elif(p1.y > 450):
            p1.y = 450

        if(p2.x > 790):
            p2.x = 790
        elif(p2.x <= 146):
            p2.x = 146
        if(p2.y <= 40):
            p2.y = 40
        elif(p2.y >= 450):
            p2.y = 450
    else:
        if(p1.x > 1049):
            p1.x = -175
        elif(p1.x <= -185):
            p1.x = 1049
        if(p1.y <= -170):
            p1.y = 540
        elif(p1.y >= 572):
            p1.y = -160

        if(p2.x > 1130):
            p2.x = -79
        elif(p2.x <= -73):
            p2.x = 1130
        if(p2.y <= -170):
            p2.y = 560
        elif(p2.y >= 630):
            p2.y = -104




## blit players
## blit man image ## VARIABLES CHARACTER AND DIRECTION X AND Y COORDONATES

## leave til later use classes, maybe make a player renderer class???
    if(character == "Two Player" or character == "man"):
        if(p1.dirY == "down" and p1.dirX == "left"):
            gameDisplay.blit(manDL,(p1.x,p1.y))
        elif(p1.dirY == "down" and p1.dirX == "right"):
            gameDisplay.blit(manDR,(p1.x, p1.y))
        elif(p1.dirY == "up" and p1.dirX == "left"):
            gameDisplay.blit(manDL,(p1.x,p1.y))
        elif(p1.dirY == "up" and p1.dirX == "right"):
            gameDisplay.blit(manDR,(p1.x,p1.y))
    if (character == "woman"):
        if(p1.dirY == "down" and p1.dirX == "left"):
            gameDisplay.blit(womanDL,(p1.x,p1.y))
        elif(p1.dirY == "down" and p1.dirX == "right"):
            gameDisplay.blit(womanDR,(p1.x,p1.y))
        elif(p1.dirY == "up" and p1.dirX == "left"):
            gameDisplay.blit(womanDL,(p1.x,p1.y))
        elif(p1.dirY == "up" and p1.dirX == "right"):
            gameDisplay.blit(womanDR,(p1.x,p1.y))
    if(mFrog and randint(0,100) == 24):
        gs.score_counter("**Croak*", f.GOLD, p1.x, p1.y)
        pygame.time.delay(200) # see if this make lag

## blit woman image
    if(character == "Two Player"):
        if(p2.dirY == "down" and p2.dirX == "left"):
            gameDisplay.blit(womanDL,(p2.x,p2.y))
        elif(p2.dirY == "down" and p2.dirX == "right"):
            gameDisplay.blit(womanDR,(p2.x,p2.y))
        elif(p2.dirY == "up" and p2.dirX == "left"):
            gameDisplay.blit(womanDL,(p2.x,p2.y))
        elif(p2.dirY == "up" and p2.dirX == "right"):
            gameDisplay.blit(womanDR,(p2.x,p2.y))

    if(wFrog and randint(0,100) == 24):
        gs.score_counter("**ribbit*", f.GOLD, p2.x, p2.y)
        pygame.time.delay(200)


    ###check if items remain .. make collision engine
        ## CHECK BANANA STATUS ## move to Game Logic / make it's own class
    if(bananaPick == False):
        if(randint(0, 100) == randint(0,100)):
             bX = randint(-40, 1000)
             bY = randint(26, 500)
        gameDisplay.blit(banana,(bX,bY))
        if p1.x> bX and p1.x < bX + 70 or p1.x + 70 > bX and p1.x + 70 < bX:
                if p1.y >bY and p1.y < bY + 70 or p1.y + 70 > bY and p1.y + 70 < bY:
                    bananaPick = True
                    p1.score += 3

                    gs.score_counter("+3", f.GOLD, bX, bY)


        if(character == "Two Player"):
            if p2.x> bX and p2.x < bX + 70 or p2.x + 70 > bX and p2.x + 70 < bX:

                    if p2.y >bY and p2.y < bY + 70 or p2.y + 70 > bY and p2.y + 70 < bY:

                        p2.score += 3
                        bananaPick = True
                        gs.score_counter("+3", f.GOLD, bX, bY)


    ## CHECK BACON STATUS
    if(baconPick == False):
        gameDisplay.blit(bacon,(baX,baY))
        if(randint(0, 80) == randint(0,80)):
             baX = randint(-40, 1000)
             baY = randint(26, 500)
        if p1.x> baX and p1.x < baX + 100 or p1.x + 100 > baX and p1.x + 100 < baX:
                if p1.y >baY and p1.y < baY + 150 or p1.y + 150 > baY and p1.y + 150 < baY:
                    baconPick = True
                    p1.score += 5

                    gs.score_counter("+5", f.GOLD, baX, baY)

        if(character == "Two Player"):
            if p2.x> baX and p2.x < baX + 100 or p2.x + 100 > baX and p2.x +100 < baX:
                    if p2.y >baY and p2.y < baY + 150 or p2.y + 150 > baY and p2.y + 150 < baY:
                        p2.score += 5
                        baconPick = True
                        gs.score_counter("+5", f.GOLD, baX, baY)


    ## CHECK KFC STATUS ##
    if(kfcPick == False):
        if(randint(0, 80) == randint(0,80)):
             kfcX = randint(-40, 1000)
             kfcY = randint(26, 500)
        gameDisplay.blit(kfc,(kfcX,kfcY))
        if p1.x> kfcX and p1.x < kfcX + 70 or p1.x + 70 > kfcX and p1.x + 70 < kfcX:
                if p1.y >kfcY and p1.y < kfcY + 70 or p1.y + 70 > kfcY and p1.y + 70 < kfcY:
                    kfcPick = True
                    p1.score += 25

                    gs.score_counter("YUM +25", f.GOLD, kfcX, kfcY)

        if(character == "Two Player"):
            if p2.x> kfcX and p2.x < kfcX + 70 or p2.x + 70 > kfcX and p2.x + 70 < kfcX:
                    if p2.y >kfcY and p2.y < kfcY + 70 or p2.y + 70 > kfcY and p2.y + 70 < kfcY:
                        p2.score += 25
                        kfcPick = True
                        gs.score_counter("YUM +25", f.GOLD, kfcX, kfcY)

    ## CHECK POTION STATUS
    if(level == 5 or level == 10 or level == 15):
        if(wPick == False):
            if(randint(0, 40) == randint(0,40)):
                wX = randint(-40, 1000)
                wY = randint(26, 500)
            gameDisplay.blit(wand,(wX,wY))
            if p1.x> wX and p1.x < wX + 70 or p1.x + 70 > wX and p1.x + 70 < wX:
                    if p1.y >wY and p1.y < wY + 70 or p1.y + 70 > wY and p1.y + 70 < wY:
                        wPick = True

                        gs.score_counter("*Croak*", f.GOLD, wX, wY)
                        manUL = pygame.image.load('../resources/imgs/characters/frog/frogL.png')
                        manUR = pygame.image.load('../resources/imgs/characters/frog/frog.png')
                        manDL = pygame.image.load('../resources/imgs/characters/frog/frogL.png')
                        manDR = pygame.image.load('../resources/imgs/characters/frog/frog.png')
                        p1.deltaY = 4
                        mFrog = True

            if(character == "Two Player"):
                if p2.x> wX and p2.x < wX + 70 or p2.x + 70 > wX and p2.x + 70 < wX:
                        if p2.y >wY and p2.y < wY + 70 or p2.y + 70 > wY and p2.y + 70 < wY:
                            wPick = True
                            gs.score_counter("**ribbit*", f.GOLD, wX, wY)
                            womanUL = pygame.image.load('../resources/imgs/characters/frog/frogL.png')
                            womanUR = pygame.image.load('../resources/imgs/characters/frog/frog.png')
                            womanDL = pygame.image.load('../resources/imgs/characters/frog/frogL.png')
                            womanDR = pygame.image.load('../resources/imgs/characters/frog/frog.png')
                            p2.deltaY = 4
                            wFrog = True
    ## CHANGE BACK FROM FROG  ... leave til last
    elif(level == 8 or level == 13 or level == 18):

        if (wPick == True):
            ## return
            wPick = False
            manUL = pygame.image.load('../resources/imgs/characters/male/pl1UpLeft.png')
            manUR = pygame.image.load('../resources/imgs/characters/male/pl1UpRight.png')
            manDL = pygame.image.load('../resources/imgs/characters/male/pl1DownLeft.png')
            manDR = pygame.image.load('../resources/imgs/characters/male/pl1DownRight.png')
            p1.deltaY = 0
            mFrog = False

            ## load woman images
            womanUL = pygame.image.load('../resources/imgs/characters/female/pl2UL.png')
            womanUR = pygame.image.load('../resources/imgs/characters/female/pl2UR.png')
            womanDL = pygame.image.load('../resources/imgs/characters/female/pl2DL.png')
            womanDR = pygame.image.load('../resources/imgs/characters/female/pl2DR.png')
            p2.deltaY = 0
            wFrog = False

    ## MAKE PLAYER MOSES
    if(bob):
        if(moPick == False):
            if(randint(0, 40) == randint(0,40)):
                moX = randint(-40, 1000)
                moY = randint(26, 500)
            gameDisplay.blit(rocks,(moX, moY))
            if p1.x> moX and p1.x < moX + 70 or p1.x + 70 > moX and p1.x + 70 < moX:
                    if p1.y >moY and p1.y < moY + 70 or p1.y + 70 > moY and p1.y + 70 < moY:
                        moPick = True
                        manUL = pygame.image.load('../resources/imgs/characters/mo/moL.png')
                        manUR = pygame.image.load('../resources/imgs/characters/mo/moR.png')
                        manDL = pygame.image.load('../resources/imgs/characters/mo/moL.png')
                        manDR = pygame.image.load('../resources/imgs/characters/mo/moR.png')
                        gs.score_counter("HOLY MOSES!!", f.GOLD, 440, 210)
                        pygame.display.update()
                        #pygame.time.delay(450)
                        p1.speed = 25
                        whoISMoses = "man"
                        mLevel = level


            if(character == "Two Player"):
                if p2.x> moX and p2.x < moX + 70 or p2.x + 70 > moX and p2.x + 70 < moX:
                        print("THIS ONE WORKED")
                        if p2.y >moY and p2.y < moY + 70 or p2.y + 70 > wY and p2.y + 70 < moY:
                            #print("SECOND")
                            moPick = True
                            gs.score_counter("HOLY MOSES!!", f.GOLD, 440, 210)
                            pygame.display.update()
                            pygame.time.delay(450)
                            #print("woman got banana")
                            womanUL = pygame.image.load('../resources/imgs/characters/mo/moL.png')
                            womanUR = pygame.image.load('../resources/imgs/characters/mo/moR.png')
                            womanDL = pygame.image.load('../resources/imgs/characters/mo/moL.png')
                            womanDR = pygame.image.load('../resources/imgs/characters/mo/moR.png')
                            p2.speed = 25
                            whoIsMoses ="woman"
                            pygame.display.update()
                            mLevel = level

    ## RETURN PLAYER FROM MOSES
    elif((moPick == True and (level - mLevel) == randint(4,8)) or (level - mLevel) > randint(8,11)):

        if (moPick == True):
            manUL = pygame.image.load('../resources/imgs/characters/male/pl1UpLeft.png')
            manUR = pygame.image.load('../resources/imgs/characters/male/pl1UpRight.png')
            manDL = pygame.image.load('../resources/imgs/characters/male/pl1DownLeft.png')
            manDR = pygame.image.load('../resources/imgs/characters/male/pl1DownRight.png')
            moPick = False
            p1.speed = 11

            ## load woman images
            womanUL = pygame.image.load('../resources/imgs/characters/female/pl2UL.png')
            womanUR = pygame.image.load('../resources/imgs/characters/female/pl2UR.png')
            womanDL = pygame.image.load('../resources/imgs/characters/female/pl2DL.png')
            womanDR = pygame.image.load('../resources/imgs/characters/female/pl2DR.png')
            moPick = False
            p2.speed = 11

    x = "GOLD"
    #combine scores to render method
    if(character == "Two Player"):
        if(p2.score > p2.score):
            gs.manScoreUP(p2.score, p1.score)
        else:
            gs.womanScoreUP(p1.score,p2.score)

    ## PRINT SCORES - DISPLAY  .... move to gameScreen (put these in one method together?)
    gs.score_counter("Team Score:  " + str(p2.score + p2.score), f.GOLD, 425, 610)
    gs.score_counter("Level:  " + str(level), f.GRAY, 40, 610)
    gs.score_counter("Score to Win:  " + str(win), f.GRAY, 860, 610)


    ##DISPLAY CLOCK   .. move to method in gameScreen
    if milliseconds > 500:
        seconds += 1
        milliseconds -= 500
    if seconds > 60:
        minutes += 1
        seconds -= 60
    gs.score_counter("  "+str(minutes)+ " min: " +str(seconds)+" sec", f.GRAY, 485, 35)
    milliseconds += clock.tick_busy_loop(60)
    pygame.display.update()
    clock.tick(60)

    ## ## ## END GAME LOOP ## ## ##




## END GAME AFTER WHILE LOOP (Good as is)
pygame.quit()
quit()
