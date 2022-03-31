import pygame
from math import degrees, radians, sin, cos, pi
import pymunk
import pymunk.pygame_util
from random import randint


FPS = 60
WIDTH, HEIGHT = 800, 600
colors = ('red', 'green', 'blue', 'orange')

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
run = True
myfont = pygame.font.SysFont('Comic Sans MS', 12)
candy = pygame.image.load('candy.png')

pymunk_draw_options = pymunk.pygame_util.DrawOptions(screen)
space = pymunk.Space()
space.gravity = (0, 981)


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

def add_boundaries(space, width, height):
    rects = [
        ((width//2, height-5), (width, 10)),
        ((width//2, 5), (width, 10)),
        ((5, height//2), (10, height)),
        ((width-5, height//2), (10, height)),
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 1
        shape.friction = 0.5
        space.add(body, shape)

def create_ball(space, pos, vel, r, mass):
    body = pymunk.Body()
    body.position = pos
    body.velocity = vel
    shape = pymunk.Circle(body, r)
    shape.mass = mass
    shape.elasticity = 0.6
    shape.friction = 0.5
    space.add(body, shape)
    return shape

def create_box(space, pos, vel, size, mass):
    body = pymunk.Body()
    body.position = pos
    body.velocity = vel
    shape = pymunk.Poly.create_box(body, size, 2)
    shape.mass = mass
    shape.elasticity = 0.6
    shape.friction = 0.5
    shape.color = pygame.Color(colors[randint(0, len(colors)-1)])
    space.add(body, shape)
    return shape    
    
add_boundaries(space, WIDTH, HEIGHT)
        
t = 0

pend = Pendulum(length=300,
                omega=pi,
                fix_point=(400, 0),
                r=20,
                phi0=75,
                circle_color='#16f844'
                )
objects = []

while run:
    screen.fill((0, 0, 0))
    Vx, Vy = pend.velocity(t)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pend.coordinates(t)
                vel = pend.velocity(t)
                if event.button == 1:
                    ball = create_ball(space, pos, vel, 20, 10)
                    objects.append(ball)
                else:
                    box = create_box(space, pos, vel, (randint(40, 80), randint(40,70)), 10)
                    objects.append(box)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                for o in objects:
                    space.remove(o)
                objects = []
    # pend.draw(screen, t)
    pend.draw2(screen, candy, t)
    text = f'({Vx:8.1f}, {Vy:8.1f})'
    rendered_text = myfont.render(text, True, (255, 255, 255))
    screen.blit(rendered_text, (20, 30))
    space.debug_draw(pymunk_draw_options)
    pygame.display.flip()
    # pygame.display.update()
    dt = clock.tick(FPS)/1000
    t += dt
    for i in range(10):
        space.step(dt/10)
pygame.quit()