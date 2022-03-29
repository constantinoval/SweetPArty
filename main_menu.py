import pygame, sys
from button import Button
from commonlib import get_font

pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Background1.png")
BG_HEADER = pygame.image.load("assets/oval.png")

BASE_COLOR = '#A9FFFA'
HIGHLITE_COLOR = '#FEFF0E'


def main_menu(SCREEN, play):
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Sweet Party", True, "#5B0B8B")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(BG_HEADER, (40, 20))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON = Button(image=pygame.image.load("assets/button4.png"),
                             pos=(640, 250),
                             text_input="PLAY", font=get_font(30), base_color=BASE_COLOR, hovering_color=HIGHLITE_COLOR)
        SHOP_BUTTON = Button(image=pygame.image.load("assets/button4.png"),
                             pos=(640, 310),
                             text_input="SHOP", font=get_font(30), base_color=BASE_COLOR, hovering_color=HIGHLITE_COLOR)
        INVENTORY_BUTTON = Button(image=pygame.image.load("assets/button6.png"),
                                  pos=(640, 370),
                                  text_input="INVENTORY", font=get_font(30), base_color=BASE_COLOR,
                                  hovering_color=HIGHLITE_COLOR)
        COMPETITION_BUTTON = Button(image=pygame.image.load("assets/button8.png"),
                                    pos=(640, 440),
                                    text_input="COMPETITION", font=get_font(30), base_color=BASE_COLOR,
                                    hovering_color=HIGHLITE_COLOR)
        WINS_BUTTON = Button(image=pygame.image.load("assets/button4.png"),
                             pos=(640, 510),
                             text_input="WINS", font=get_font(30), base_color=BASE_COLOR, hovering_color=HIGHLITE_COLOR)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/button4.png"),
                             pos=(640, 580),
                             text_input="QUIT", font=get_font(30), base_color=BASE_COLOR, hovering_color=HIGHLITE_COLOR)

        for button in [PLAY_BUTTON, QUIT_BUTTON, SHOP_BUTTON, INVENTORY_BUTTON,
                       COMPETITION_BUTTON, WINS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(SCREEN)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()