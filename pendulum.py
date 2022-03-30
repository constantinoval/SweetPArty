import secrets
import pygame, sys
from math import degrees, radians, sin, cos, pi

FPS = 60

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
run = True
myfont = pygame.font.SysFont('Comic Sans MS', 12)
candy = pygame.image.load('assets/candy.png')


class Pendulum:
    def __init__(self, length, omega, fix_point=(0,0), phi0=45, r=5,
                 line_color = (255, 255, 255), circle_color=(255, 255, 255)):
        self.length = length
        self.fix_point = fix_point
        self.phi0 = radians(phi0)
        self.omega = omega
        self.r = r
        self.line_color = line_color
        self.circle_color = circle_color
        
    def phi(self, t):
        return self.phi0*cos(self.omega*t)
    
    def dphi(self, t):
        return self.phi0*self.omega*sin(self.omega*t)
    
    def velocity(self, t):
        V = self.dphi(t)*self.length
        phi = self.phi(t)
        Vx = -V*cos(phi)
        Vy =  V*sin(phi)
        return Vx, Vy
    
    def coordinates(self, t):
        phi = self.phi(t)
        x = self.fix_point[0] + self.length*sin(phi)
        y = self.fix_point[1] + self.length*cos(phi)
        return x, y

    def draw(self, screen, t):
        x, y = self.coordinates(t)
        Vx, Vy = self.velocity(t)
        pygame.draw.line(
            screen,
            self.line_color,
            start_pos=self.fix_point,
            end_pos=(x, y),
            width=2
        )
        pygame.draw.circle(
            screen,
            self.circle_color,
            (x, y),
            self.r
        )
        pygame.draw.line(
            screen,
            pygame.Color('red'),
            start_pos=(x, y),
            end_pos=(x+Vx/10, y+Vy/10),
            width=2
        )
    
    def draw2(self, screen, image, t):
        x, y = self.coordinates(t)
        pygame.draw.line(
            screen,
            self.line_color,
            start_pos=self.fix_point,
            end_pos=(x, y),
            width=2
        )
        screen.blit(image, (x-image.get_width()/2, y-image.get_height()/2))        
        
t = 0

pend = Pendulum(length=300,
                omega=pi/2,
                fix_point=(400, 0),
                r=20,
                phi0=75,
                circle_color='#16f844'
                )

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    screen.fill((0, 0, 0))
    # pend.draw(screen, t)
    pend.draw2(screen, candy, t)
    Vx, Vy = pend.velocity(t)
    text = f'({Vx:8.1f}, {Vy:8.1f})'
    rendered_text = myfont.render(text, True, (255, 255, 255))
    screen.blit(rendered_text, (0,0))
    pygame.display.flip()
    # pygame.display.update()
    t += clock.tick(FPS)/1000