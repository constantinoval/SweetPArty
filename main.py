import pygame, sys
from button import Button
from main_menu import main_menu
from play import play
from commonlib import get_font

pygame.init()
WIDTH, HEIGHT = 1200, 720
FPS = 60

class main_application:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = FPS
        self.main_menu = main_menu(self)
        self.play = play(self)
        self.clock = pygame.time.Clock()
        self.main_menu.run()


if __name__=='__main__':
    app = main_application(WIDTH, HEIGHT)