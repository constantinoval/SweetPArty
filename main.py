import pygame, sys
from button import Button
from main_menu import main_menu
from play import play
from commonlib import get_font

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
main_menu(SCREEN, play)