#clean up GOLD BLACK AND WHITE somehow ,, make fonts class
import pygame
import os
pygame.init()
import FontG
import Game
f = FontG.Fonts()
G = Game.G()
class GameScreen(): # get working then split this up
    #def __init__(self, G):
    #    super().__init__()

    ## this is the render text method migrate somewhere else
    def render_to_screen(self, msg, color, x, y): #move to gameScreen
        GOLD = (255, 215, 0)
        if(color == f.GOLD):
            screen_text = f.font1.render(msg, True, color)
        else:
            screen_text = f.font.render(msg, True, color)
        G.gameDisplay.blit(screen_text, [x, y])

    def initalize(self):  #create initalizer class
        self.render_to_screen("Initalizing.", f.WHITE, 400, 257)
        pygame.time.delay(400)
        self.render_to_screen("Initalizing.", f.WHITE, 400, 257)
        pygame.display.update()
        pygame.time.delay(250)
        G.gameDisplay.fill(f.BLACK)
        self.render_to_screen("Initalizing..", f.WHITE, 400, 257)
        pygame.display.update()
        pygame.time.delay(250)
        self.render_to_screen("Initalizing...", f.WHITE, 400, 257)
        pygame.display.update()
        pygame.time.delay(300)

    def closing(self): #define closing class
                G.gameDisplay.fill(f.BLACK)
                self.render_to_screen("Closing....", f.WHITE, 400, 257)
                pygame.time.delay(350)
                self.render_to_screen("Closing...", f.WHITE, 400, 257)
                pygame.display.update()
                pygame.time.delay(250)
                G.gameDisplay.fill(BLACK)
                self.render_to_screen("Closing..", f.WHITE, 400, 257)
                pygame.display.update()
                pygame.time.delay(250)
                self.render_to_screen("Closing.", f.WHITE, 400, 257)
                pygame.display.update()
                pygame.time.delay(250)
                G.gameDisplay.blit(intro_image,(0,0))
                self.render_to_screen("Game Over", f.GOLD, 455, 210)

    #combine the two below to render scores method
    def score_mode(self, womanScore, manScore): #move to gameScreen
        if(manScore > womanScore):
            self.render_to_screen("Player 2:   " + str(womanScore), f.WHITE, 175, 17)
            self.render_to_screen("Player 1:   " + str(manScore), f.GOLD, 785, 13)
        else:
            self.render_to_screen("Player 2:   " + str(womanScore), f.GOLD, 155, 13)
            self.render_to_screen("Player 1:   " + str(manScore), f.WHITE, 785, 17)

    def womanScoreUP(self, manScore, womanScore): #move to gameScreen
        self.render_to_screen("Player 2:   " + str(womanScore), f.GOLD, 155, 13)
        self.render_to_screen("Player 1:   " + str(manScore), f.WHITE, 785, 17)

    def introMain(self): #move to IntroScreen
        self.render_to_screen("FOOD RUN", f.GOLD, 450, 180)
        self.render_to_screen("Press i: To View Instructions", f.BLACK, 400, 257)
        self.render_to_screen("Press n: To Select Player Mode", f.WHITE, 400, 307)
        self.render_to_screen("Press w: To Set Winning Points", f.BLACK, 400, 357)
        self.render_to_screen("Press s to Start", f.BLACK, 450, 457)

    def instructionMenu(self): #move to IntroScreen
        self.render_to_screen("Instructions", f.GOLD, 455, 17)
        self.render_to_screen("Use the arrow keys to move the character(s) to collect", f.BLACK, 180, 80)
        self.render_to_screen("food items scattered throughout the maps to earn points. If two", f.BLACK, 180, 120)
        self.render_to_screen("player mode is enabled the second player uses the keys (a)" , f.BLACK, 180, 160)
        self.render_to_screen("to go left, (d) up, (w) right, and (x) to move down. ", f.BLACK, 180, 200)
        self.render_to_screen("Press M to return to the main menu", f.BLACK, 375, 517)

    def playerScreen(self, character, womanDL, manDR):
        self.render_to_screen("Players Select", f.GOLD, 455, 17)
        self.render_to_screen("Player mode:  "+ character.upper(), f.BLACK, 400, 110)
        self.render_to_screen("Press up for two player left for single woman or right single player man", f.BLACK, 50, 415)
        self.render_to_screen("Press M to return to the menu", f.BLACK, 375, 517)
        if(character == "Two Player"):
           G.gameDisplay.blit(womanDL,(600,150))
           G.gameDisplay.blit(manDR,(400,150))
        elif(character == "woman"):
            G.gameDisplay.blit(womanDL,(530,180))
        elif(character == "man"):
            G.gameDisplay.blit(manDR,(420,150))

    def winScreen(self, win):  #push to intro render
        self.render_to_screen("Win Limit", f.GOLD, 455, 17)
        self.render_to_screen("Points to Win:  ", f.BLACK, 430, 110)
        self.render_to_screen(str(win), f.GOLD, 650, 105)
        self.render_to_screen("Use the the up and down arrow keys to change the win limit", f.BLACK, 150, 200)
        self.render_to_screen("Press M to return to the menu", f.BLACK, 375, 517)
