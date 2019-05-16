class GameScreen: ## get working then split this up
    #def __init__(self):


    def score_counter(msg, color, x, y): #move to gameScreen
        if(color == GOLD):
            screen_text = font1.render(msg, True, color)
        else:
            screen_text = font.render(msg, True, color)
        gameDisplay.blit(screen_text, [x, y])

    def initalize():  #create initalizer class
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

    def closing(): #define closing class
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
    def manScoreUP(womanScore, manScore): #move to gameScreen
        score_counter("Player 2:   " + str(womanScore), WHITE, 175, 17)
        score_counter("Player 1:   " + str(manScore), GOLD, 785, 13)

    def womanScoreUP(manScore, womanScore): #move to gameScreen
        score_counter("Player 2:   " + str(womanScore), GOLD, 155, 13)
        score_counter("Player 1:   " + str(manScore), WHITE, 785, 17)

    def introMain(): #move to IntroScreen
        score_counter("FOOD RUN", GOLD, 450, 180)
        score_counter("Press i: To View Instructions", BLACK, 400, 257)
        score_counter("Press n: To Select Player Mode", WHITE, 400, 307)
        score_counter("Press w: To Set Winning Points", BLACK, 400, 357)
        score_counter("Press s to Start", BLACK, 450, 457)

    def instructionMenu(): #move to IntroScreen
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

    def winScreen(win):  #push to intro render
        score_counter("Win Limit", GOLD, 455, 17)
        score_counter("Points to Win:  ", BLACK, 430, 110)
        score_counter(str(win), GOLD, 650, 105)
        score_counter("Use the the up and down arrow keys to change the win limit", BLACK, 150, 200)
        score_counter("Press M to return to the menu", BLACK, 375, 517)
