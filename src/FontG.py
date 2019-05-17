import pygame
import os
pygame.init()
class Fonts():
    def __init__(self):
        self.GRAY = (245, 245, 245)
        self.GOLD = (255, 215, 0)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.font = pygame.font.SysFont(None, 45)
        self.font1 = pygame.font.SysFont(None, 60)
