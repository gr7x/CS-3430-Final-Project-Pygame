import pygame
import os
import FontG
import GameScreen
gs = GameScreen.GameScreen()

class Logic:
    def __init__(self):
            self.love=True
            self.win=500
            self.character="Two Player"
            self.gameExit = False
            self.level = 1

    def checkForWin(self, p1Score, p2Score, character): #moveto Game Logic then clean up

        if((p1Score + p2Score) >= self.win):
            #fix closing segment
            gameDisplay.blit(intro_image,(0,0)) # fix later
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
