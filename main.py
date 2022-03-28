import pygame, sys
from button import Button
import pygame.gfxdraw

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background1.png")
PLAY_BG = pygame.image.load("assets/play_background.png")
BG_HEADER = pygame.image.load("assets/oval.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(PLAY_BG, (0, 0))

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, HIGHLITE_COLOR)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

BASE_COLOR = '#A9FFFA'
HIGHLITE_COLOR = '#FEFF0E'

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Sweet Party", True, "#5B0B8B")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        # rect = pygame.Rect(640-600, 100-80, 1200, 160)
        # shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        # pygame.draw.rect(SCREEN, (255, 255, 255, 255), shape_surf.get_rect())
        # pygame.draw.rect(SCREEN, color='#CDFF2F', rect=pygame.Rect(640-600, 100-80, 1200, 160),
        #                  border_radius=30)
        # pygame.gfxdraw.box(SCREEN, pygame.Rect(640-600, 100-80, 1200, 160), (175, 255, 0, 150))
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
                                  text_input="INVENTORY", font=get_font(30), base_color=BASE_COLOR, hovering_color=HIGHLITE_COLOR)
        COMPETITION_BUTTON = Button(image=pygame.image.load("assets/button8.png"),
                                  pos=(640, 440),
                                  text_input="COMPETITION", font=get_font(30), base_color=BASE_COLOR, hovering_color=HIGHLITE_COLOR)
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
                    play()
                # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()