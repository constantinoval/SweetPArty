import pygame, sys
from main_menu import main_menu
PLAY_BG = pygame.image.load("assets/play_background.png")

def play(SCREEN):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(PLAY_BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu(SCREEN, play)

        pygame.display.update()