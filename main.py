import pygame, sys
from button import Button
from main_menu import main_menu
from play import play
from commonlib import get_font

pygame.init()
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
main_menu(SCREEN, play)