import pygame
import os
import GameScreen
import Game
import FontG
import Player
import Item
import GameLogic
from random import randint
f = FontG.Fonts()
G = Game.G()
gs = GameScreen.GameScreen()
gl = GameLogic.Logic()



def music(): # move to audio class ... figure out why turning screen black.. here
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

if __name__ == '__main__':
    pygame.init()

    gameDisplay = pygame.display.set_mode((1159,659))
    pygame.display.set_caption('Memory Quest')

    ## LOAD BACKGROUND IMAGES ... Find a better way to store these

    background_image = pygame.image.load("../resources/imgs/maps/street1.png").convert()
    intro_image = pygame.image.load("../resources/imgs/backgrounds/intro.png").convert()
    map2 = pygame.image.load("../resources/imgs/maps/map2.png").convert()
    map3 = pygame.image.load("../resources/imgs/maps/df.png").convert()
    spa = pygame.image.load("../resources/imgs/maps/pool.png").convert()

    manUL = pygame.image.load('../resources/imgs/characters/male/pl1UpLeft.png')
    manUR = pygame.image.load('../resources/imgs/characters/male/pl1UpRight.png')
    manDL = pygame.image.load('../resources/imgs/characters/male/pl1DownLeft.png')
    manDR = pygame.image.load('../resources/imgs/characters/male/pl1DownRight.png')

    womanUL = pygame.image.load('../resources/imgs/characters/female/pl2UL.png')
    womanUR = pygame.image.load('../resources/imgs/characters/female/pl2UR.png')
    womanDL = pygame.image.load('../resources/imgs/characters/female/pl2DL.png')
    womanDR = pygame.image.load('../resources/imgs/characters/female/pl2DR.png')

    ## load object images
    kfc = pygame.image.load("../resources/imgs/items/kfc.png")
    banana = pygame.image.load('../resources/imgs/items/banana.png')
    bacon = pygame.image.load('../resources/imgs/items/bacon.png')
    wand = pygame.image.load("../resources/imgs/items/potion.png")
    rocks = pygame.image.load("../resources/imgs/items/mo.png")

    ## INITALOZE BACKGROUND VARIABLE ... game mode class
    background = background_image


## SETUP TIME  ... maybe make time class
    clock = pygame.time.Clock()
    minutes = 0
    seconds = 0
    milliseconds = 0

## create Both Players
    p1=Player.Player(50,50,"right")
    p2=Player.Player(200,200, "left")


    ## create and destroy these during game play
    bananaItem = Item.Item(610, 475)
    baconItem = Item.Item(1035, 250)
    kfcItem = Item.Item(randint(75, 775), randint(75, 500))
    rocksItem = Item.Item(randint(75, 775),randint(75, 480))
    wandItem =Item.Item(randint(75, 775), randint(75, 470))


    # Get rid of this
    round1 = True
    round2 = False
    round3 = False





### CLEAN UP AND GET RID OF THESE
    # move to seperate class its cariable if man and woman are frogs
    wFrog = False
    mFrog = False

    ## figure out this section below
    bob = False
    whoIsMoses = "none"


    ## don't do this
    mLevel = 0

    select = 1
    prevSelect = 1
    Intro = True

    ### Get rid of this

    ##########################################


    ## VARIABLES FOR INTRO SCREEN -- put in intro screen class
    instructionScreen = False
    pScreen = False
    pointS = False
    winChange = 0
    ########INTRO SCREEN LOOP######### THS STAYS HERE
    while Intro:
            gameDisplay.blit(intro_image,(0,0))
            pygame.mixer.music.get_busy()

            ### CHECKS TO CHOOSE WHICH SCREEN TO DISPLAY ### PULL BASED ON BOOL VALUES
            if not (pScreen or instructionScreen or pointS):
                gs.introMain()
            elif(instructionScreen):
                gs.instructionMenu()
            elif(pScreen):
                gs.playerScreen(gl.character, womanDL, manDR)
            elif(pointS):
                gs.winScreen(gl.win)


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
                            gl.character = "Two Player"
                    if event.key == pygame.K_DOWN:
                        if(pointS):
                            winChange -= 50

                    if event.key == pygame.K_LEFT:
                        if(pScreen):
                            gl.character = "man"
                    if event.key == pygame.K_RIGHT:
                        if(pScreen):
                            gl.character = "woman"
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
                            gl.character = "Two Player"
                    if event.key == pygame.K_DOWN:
                        if(pointS):
                            winChange = 0
            ## update points to win

            gl.win += winChange
            if(pointS):
                pygame.time.delay(175)
            if(gl.win < 50):
                gl.win = 10500

            elif(gl.win > 10500):
                gl.win = 50

            pygame.display.update()
            clock.tick(60)

    ### INITALIZE MUSIC SELECTION FOR GAME PLAY


    music()

    gs.initalize()




    ## ## ## MAIN GAME LOOP ## ## ##

    while not gl.gameExit: ## leave here but use classes to chnage data
        pygame.mixer.music.get_busy()

        #######EVENTS########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ## CLOSING DISPLAY ## POSSIBLY PULL TO A METHOD
                pygame.mixer.music.play(-1,0)
                gs.closing()
                if(gl.character == "Two Player"):
                    pygame.display.update()
                    if(p1.score > p2.score):
                        gs.render_to_screen("Player One Lead", f.BLACK, 440, 280)

                    else:
                        gs.render_to_screen("Player Two Lead", f.BLACK, 440, 280)

                gs.render_to_screen("Final Score:  " + str(p2.score + p1.score), f.BLACK, 460, 340) ## use get functions for score
                pygame.display.update()
                pygame.time.delay(2500)
                gl.gameExit = True
                ## END CLOSING DISPLAY

             ## CHECK GAME KEY EVENTS ## These probably stay here
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

            ## CHECK KEYUP EVENTS These probably stay here
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

        ####update movment
        p1.x += p1.deltaX
        p1.y += p1.deltaY

        p2.x += p2.deltaX
        p2.y += p2.deltaY

        gl.checkForWin(p1.score, p2.score, gl.character)


        #### render background  leave til later to figure out how to setup
        gameDisplay.blit(background, (0,0))


        ### RAISE LEVEL METHOD move to game logic do later, pass Player object to this??
        if(baconItem.pick == True and bananaItem.pick == True and kfcItem.pick):
            gs.render_to_screen("NEXT LEVEL", f.GOLD, 440, 210)
            pygame.display.update()
            pygame.time.delay(550)
            gl.level += 1
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
            ##MAKE RAISE LEVEL METHOD CREATE AND DELET OBJECTS INTEAD...
            if(select == 1):
                background = background_image
            elif(select == 2):
                background = map3
                bananaItem.locX = randint(-40, 1000)
                bananaItem.locY = randint(26, 500)
                baconItem.locX = randint(-40, 1000)
                baconItem.locY = randint(26, 500)
                kfcItem.locX = randint(-40, 1000)
                kfcItem.locY = randint(26, 500)
            elif(select == 3):
                background = map2
                bananaItem.locX = randint(155, 750)
                bananaItem.locY = randint(100, 450)
                baconItem.locX = randint(155, 750)
                baconItem.locY = randint(100, 450)
                kfcItem.locX = randint(155, 750)
                kfcItem.locY = randint(100, 450)
            elif(select == 4):
                background = spa
                bananaItem.locX = randint(-40, 1000)
                bananaItem.locY = randint(26, 500)
                baconItem.locX = randint(-40, 1000)
                baconItem.locY = randint(26, 500)
                kfcItem.locX = randint(-40, 1000)
                kfcItem.locY = randint(26, 500)

            prevSelect = select
            ## once class is created this is done by default
            baconItem.pick = False
            bananaItem.pick = False
            kfcItem.pick = False
            kfcItem.locX = randint(75, 775)
            kfcItem.locY = randint(75, 500)


    ## blit objects


    ## check cross map boundaries PULL TO METHOD?

        if(background == map2):

            #PuLL TO BOUNDARY CHECK METHOD / get data without hardcoding

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
        if(gl.character == "Two Player" or gl.character == "man"):
            if(p1.dirY == "down" and p1.dirX == "left"):
                gameDisplay.blit(manDL,(p1.x,p1.y))
            elif(p1.dirY == "down" and p1.dirX == "right"):
                gameDisplay.blit(manDR,(p1.x, p1.y))
            elif(p1.dirY == "up" and p1.dirX == "left"):
                gameDisplay.blit(manDL,(p1.x,p1.y))
            elif(p1.dirY == "up" and p1.dirX == "right"):
                gameDisplay.blit(manDR,(p1.x,p1.y))
        if (gl.character == "woman"):
            if(p1.dirY == "down" and p1.dirX == "left"):
                gameDisplay.blit(womanDL,(p1.x,p1.y))
            elif(p1.dirY == "down" and p1.dirX == "right"):
                gameDisplay.blit(womanDR,(p1.x,p1.y))
            elif(p1.dirY == "up" and p1.dirX == "left"):
                gameDisplay.blit(womanDL,(p1.x,p1.y))
            elif(p1.dirY == "up" and p1.dirX == "right"):
                gameDisplay.blit(womanDR,(p1.x,p1.y))
        if(mFrog and randint(0,100) == 24):
            gs.render_to_screen("**Croak*", f.GOLD, p1.x, p1.y)
            pygame.time.delay(200) # see if this make lag

    ## blit woman image
        if(gl.character == "Two Player"):
            if(p2.dirY == "down" and p2.dirX == "left"):
                gameDisplay.blit(womanDL,(p2.x,p2.y))
            elif(p2.dirY == "down" and p2.dirX == "right"):
                gameDisplay.blit(womanDR,(p2.x,p2.y))
            elif(p2.dirY == "up" and p2.dirX == "left"):
                gameDisplay.blit(womanDL,(p2.x,p2.y))
            elif(p2.dirY == "up" and p2.dirX == "right"):
                gameDisplay.blit(womanDR,(p2.x,p2.y))

        if(wFrog and randint(0,100) == 24):
            gs.render_to_screen("**ribbit*", f.GOLD, p2.x, p2.y)
            pygame.time.delay(200)


        ###check if items remain .. make collision engine
            ## CHECK BANANA STATUS ## move to Game Logic / make it's own class
        if(bananaItem.pick == False):
            if(randint(0, 100) == randint(0,100)):
                 bananaItem.locX = randint(-40, 1000)
                 bananaItem.locY = randint(26, 500)
            gameDisplay.blit(banana,(bananaItem.locX,bananaItem.locY))
            if p1.x> bananaItem.locX and p1.x < bananaItem.locX + 70 or p1.x + 70 > bananaItem.locX and p1.x + 70 < bananaItem.locX:
                    if p1.y >bananaItem.locY and p1.y < bananaItem.locY + 70 or p1.y + 70 > bananaItem.locY and p1.y + 70 < bananaItem.locY:
                        bananaItem.pick = True
                        p1.score += 3

                        gs.render_to_screen("+3", f.GOLD, bananaItem.locX, bananaItem.locY)


            if(gl.character == "Two Player"):
                if p2.x> bananaItem.locX and p2.x < bananaItem.locX + 70 or p2.x + 70 > bananaItem.locX and p2.x + 70 < bananaItem.locX:

                        if p2.y >bananaItem.locY and p2.y < bananaItem.locY + 70 or p2.y + 70 > bananaItem.locY and p2.y + 70 < bananaItem.locY:

                            p2.score += 3
                            bananaItem.pick = True
                            gs.render_to_screen("+3", f.GOLD, bananaItem.locX, bananaItem.locY)


        ## CHECK BACON STATUS
        if(baconItem.pick == False):
            gameDisplay.blit(bacon,(baconItem.locX,baconItem.locY))
            if(randint(0, 80) == randint(0,80)):
                 baconItem.locX = randint(-40, 1000)
                 baconItem.locY = randint(26, 500)
            if p1.x> baconItem.locX and p1.x < baconItem.locX + 100 or p1.x + 100 > baconItem.locX and p1.x + 100 < baconItem.locX:
                    if p1.y >baconItem.locY and p1.y < baconItem.locY + 150 or p1.y + 150 > baconItem.locY and p1.y + 150 < baconItem.locY:
                        baconItem.pick = True
                        p1.score += 5

                        gs.render_to_screen("+5", f.GOLD, baconItem.locX, baconItem.locY)

            if(gl.character == "Two Player"):
                if p2.x> baconItem.locX and p2.x < baconItem.locX + 100 or p2.x + 100 > baconItem.locX and p2.x +100 < baconItem.locX:
                        if p2.y >baconItem.locY and p2.y < baconItem.locY + 150 or p2.y + 150 > baconItem.locY and p2.y + 150 < baconItem.locY:
                            p2.score += 5
                            baconItem.pick = True
                            gs.render_to_screen("+5", f.GOLD, baconItem.locX, baconItem.locY)


        ## CHECK KFC STATUS ##
        if(kfcItem.pick == False):
            if(randint(0, 80) == randint(0,80)):
                 kfcItem.locX = randint(-40, 1000)
                 kfcItem.locY = randint(26, 500)
            gameDisplay.blit(kfc,(kfcItem.locX,kfcItem.locY))
            if p1.x> kfcItem.locX and p1.x < kfcItem.locX + 70 or p1.x + 70 > kfcItem.locX and p1.x + 70 < kfcItem.locX:
                    if p1.y >kfcItem.locY and p1.y < kfcItem.locY + 70 or p1.y + 70 > kfcItem.locY and p1.y + 70 < kfcItem.locY:
                        kfcItem.pick = True
                        p1.score += 25

                        gs.render_to_screen("YUM +25", f.GOLD, kfcItem.locX, kfcItem.locY)

            if(gl.character == "Two Player"):
                if p2.x> kfcItem.locX and p2.x < kfcItem.locX + 70 or p2.x + 70 > kfcItem.locX and p2.x + 70 < kfcItem.locX:
                        if p2.y >kfcItem.locY and p2.y < kfcItem.locY + 70 or p2.y + 70 > kfcItem.locY and p2.y + 70 < kfcItem.locY:
                            p2.score += 25
                            kfcItem.pick = True
                            gs.render_to_screen("YUM +25", f.GOLD, kfcItem.locX, kfcItem.locY)

        ## CHECK POTION STATUS
        if(gl.level == 5 or gl.level == 10 or gl.level == 15):
            if(wandItem.pick == False):
                if(randint(0, 40) == randint(0,40)):
                    wandItem.locX = randint(-40, 1000)
                    wandItem.locY = randint(26, 500)
                gameDisplay.blit(wand,(wandItem.locX,wandItem.locY))
                if p1.x> wandItem.locX and p1.x < wandItem.locX + 70 or p1.x + 70 > wandItem.locX and p1.x + 70 < wandItem.locX:
                        if p1.y >wandItem.locY and p1.y < wandItem.locY + 70 or p1.y + 70 > wandItem.locY and p1.y + 70 < wandItem.locY:
                            wandItem.pick = True

                            gs.render_to_screen("*Croak*", f.GOLD, wandItem.locX, wandItem.locY)
                            manUL = pygame.image.load('../resources/imgs/characters/frog/frogL.png')
                            manUR = pygame.image.load('../resources/imgs/characters/frog/frog.png')
                            manDL = pygame.image.load('../resources/imgs/characters/frog/frogL.png')
                            manDR = pygame.image.load('../resources/imgs/characters/frog/frog.png')
                            p1.deltaY = 4
                            mFrog = True

                if(gl.character == "Two Player"):
                    if p2.x> wandItem.locX and p2.x < wandItem.locX + 70 or p2.x + 70 > wandItem.locX and p2.x + 70 < wandItem.locX:
                            if p2.y >wandItem.locY and p2.y < wandItem.locY + 70 or p2.y + 70 > wandItem.locY and p2.y + 70 < wandItem.locY:
                                wandItem.pick = True
                                gs.render_to_screen("**ribbit*", f.GOLD, wandItem.locX, wandItem.locY)
                                womanUL = pygame.image.load('../resources/imgs/characters/frog/frogL.png')
                                womanUR = pygame.image.load('../resources/imgs/characters/frog/frog.png')
                                womanDL = pygame.image.load('../resources/imgs/characters/frog/frogL.png')
                                womanDR = pygame.image.load('../resources/imgs/characters/frog/frog.png')
                                p2.deltaY = 4
                                wFrog = True
        ## CHANGE BACK FROM FROG  ... leave til last
        elif(gl.level == 8 or gl.level == 13 or gl.level == 18):

            if (wandItem.pick == True):
                ## return
                wandItem.pick = False
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
            if(rocksItem.pick == False):
                if(randint(0, 40) == randint(0,40)):
                    rocksItem.locX = randint(-40, 1000)
                    rocksItem.locY = randint(26, 500)
                gameDisplay.blit(rocks,(rocksItem.locX, rocksItem.locY))
                if p1.x> rocksItem.locX and p1.x < rocksItem.locX + 70 or p1.x + 70 > rocksItem.locX and p1.x + 70 < rocksItem.locX:
                        if p1.y >rocksItem.locY and p1.y < rocksItem.locY + 70 or p1.y + 70 > rocksItem.locY and p1.y + 70 < rocksItem.locY:
                            rocksItem.pick = True
                            manUL = pygame.image.load('../resources/imgs/characters/mo/moL.png')
                            manUR = pygame.image.load('../resources/imgs/characters/mo/moR.png')
                            manDL = pygame.image.load('../resources/imgs/characters/mo/moL.png')
                            manDR = pygame.image.load('../resources/imgs/characters/mo/moR.png')
                            gs.render_to_screen("HOLY MOSES!!", f.GOLD, 440, 210)
                            pygame.display.update()
                            #pygame.time.delay(450)
                            p1.speed = 25
                            whoISMoses = "man"
                            mLevel = gl.level


                if(gl.character == "Two Player"):
                    if p2.x> rocksItem.locX and p2.x < rocksItem.locX + 70 or p2.x + 70 > rocksItem.locX and p2.x + 70 < rocksItem.locX:
                            if p2.y >rocksItem.locY and p2.y < rocksItem.locY + 70 or p2.y + 70 > wandItem.locY and p2.y + 70 < rocksItem.locY:
                                #print("SECOND")
                                rocksItem.pick = True
                                gs.render_to_screen("HOLY MOSES!!", f.GOLD, 440, 210)
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
                                mLevel = gl.level

        ## RETURN PLAYER FROM MOSES
        elif((rocksItem.pick == True and (gl.level - mLevel) == randint(4,8)) or (gl.level - mLevel) > randint(8,11)):

            if (rocksItem.pick == True):
                manUL = pygame.image.load('../resources/imgs/characters/male/pl1UpLeft.png')
                manUR = pygame.image.load('../resources/imgs/characters/male/pl1UpRight.png')
                manDL = pygame.image.load('../resources/imgs/characters/male/pl1DownLeft.png')
                manDR = pygame.image.load('../resources/imgs/characters/male/pl1DownRight.png')
                rocksItem.pick = False
                p1.speed = 11

                ## load woman images
                womanUL = pygame.image.load('../resources/imgs/characters/female/pl2UL.png')
                womanUR = pygame.image.load('../resources/imgs/characters/female/pl2UR.png')
                womanDL = pygame.image.load('../resources/imgs/characters/female/pl2DL.png')
                womanDR = pygame.image.load('../resources/imgs/characters/female/pl2DR.png')
                rocksItem.pick = False
                p2.speed = 11

        x = "GOLD"


        #Game Scree Frame Pass to Renderer
        if(gl.character == "Two Player"):
                gs.score_mode(p2.score, p1.score)
        ## PRINT SCORES - DISPLAY  .... move to gameScreen (put these in one method together?)
        gs.render_to_screen("Team Score:  " + str(p2.score + p2.score), f.GOLD, 425, 610)
        gs.render_to_screen("Level:  " + str(gl.level), f.GRAY, 40, 610)
        gs.render_to_screen("Score to Win:  " + str(gl.win), f.GRAY, 860, 610)


        ##DISPLAY CLOCK   .. move to method in gameScreen
        if milliseconds > 500:
            seconds += 1
            milliseconds -= 500
        if seconds > 60:
            minutes += 1
            seconds -= 60
        gs.render_to_screen("  "+str(minutes)+ " min: " +str(seconds)+" sec", f.GRAY, 485, 35)
        milliseconds += clock.tick_busy_loop(60)
        pygame.display.update()
        clock.tick(60)

        ## ## ## END GAME LOOP ## ## ##




    ## END GAME AFTER WHILE LOOP (Good as is)
    pygame.quit()
    quit()
