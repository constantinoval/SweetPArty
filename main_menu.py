import pygame, sys
from button import Button
from commonlib import get_font

class main_menu:
    def __init__(self, parent):
        self.parent = parent
        self.screen = parent.screen
        self.BG = pygame.image.load("assets/Background1.png")
        self.BG_HEADER = pygame.image.load("assets/oval.png")
        self.BASE_COLOR = '#A9FFFA'
        self.HIGHLITE_COLOR = '#FEFF0E'
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.display.set_caption("Main menu")
        _run = True
        while _run:
            self.screen.blit(self.BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = get_font(100).render("Sweet Party", True, "#5B0B8B")
            MENU_RECT = MENU_TEXT.get_rect(center=(self.parent.width//2, 100))
            self.screen.blit(self.BG_HEADER, (2, 20))
            self.screen.blit(MENU_TEXT, MENU_RECT)
            PLAY_BUTTON = Button(image=pygame.image.load("assets/button4.png"),
                                 pos=(self.parent.width//2, 250),
                                 text_input="PLAY", font=get_font(30), base_color=self.BASE_COLOR,
                                 hovering_color=self.HIGHLITE_COLOR)
            SHOP_BUTTON = Button(image=pygame.image.load("assets/button4.png"),
                                 pos=(self.parent.width//2, 310),
                                 text_input="SHOP", font=get_font(30), base_color=self.BASE_COLOR,
                                 hovering_color=self.HIGHLITE_COLOR)
            INVENTORY_BUTTON = Button(image=pygame.image.load("assets/button6.png"),
                                      pos=(self.parent.width//2, 370),
                                      text_input="INVENTORY", font=get_font(30), base_color=self.BASE_COLOR,
                                      hovering_color=self.HIGHLITE_COLOR)
            COMPETITION_BUTTON = Button(image=pygame.image.load("assets/button8.png"),
                                        pos=(self.parent.width//2, 440),
                                        text_input="COMPETITION", font=get_font(30), base_color=self.BASE_COLOR,
                                        hovering_color=self.HIGHLITE_COLOR)
            WINS_BUTTON = Button(image=pygame.image.load("assets/button4.png"),
                                 pos=(self.parent.width//2, 510),
                                 text_input="WINS", font=get_font(30), base_color=self.BASE_COLOR,
                                 hovering_color=self.HIGHLITE_COLOR)
            QUIT_BUTTON = Button(image=pygame.image.load("assets/button4.png"),
                                 pos=(self.parent.width//2, 580),
                                 text_input="QUIT", font=get_font(30), base_color=self.BASE_COLOR,
                                 hovering_color=self.HIGHLITE_COLOR)

            for button in [PLAY_BUTTON, QUIT_BUTTON, SHOP_BUTTON, INVENTORY_BUTTON,
                           COMPETITION_BUTTON, WINS_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.parent.play.run()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            self.parent.clock.tick(self.parent.fps)
            pygame.display.update()
