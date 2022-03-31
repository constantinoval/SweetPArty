import pygame
import sys
from math import degrees, radians, sin, cos, pi
import pymunk
import pymunk.pygame_util
from random import randint
from pendulum import Pendulum

class play:
    def __init__(self, parent):
        self.parent = parent
        self.screen = self.parent.screen
        self.PLAY_BG = pygame.image.load("assets/play_background.png")
        self.colors = ('red', 'green', 'blue', 'orange')
        self.candy = pygame.image.load('assets/candy.png')
        self.pymunk_draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.pendulum = Pendulum(
            length=300,
            omega=pi / 4,
            fix_point=(self.parent.width//2, 10),
            r=20,
            phi0=75,
            circle_color='#16f844',
            line_color=pygame.Color('darkred')
        )
        self.vscale = 1

    def add_boundaries(self):
        rects = [
            ((self.parent.width // 2, self.parent.height - 5), (self.parent.width, 10)),
            ((self.parent.width // 2, 5), (self.parent.width, 10)),
            ((5, self.parent.height // 2), (10, self.parent.height)),
            ((self.parent.width - 5, self.parent.height // 2), (10, self.parent.height)),
        ]
        for pos, size in rects:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position = pos
            shape = pymunk.Poly.create_box(body, size)
            shape.elasticity = 1
            shape.friction = 0.5
            shape.color = pygame.Color('pink')
            self.space.add(body, shape)

    def create_ball(self, pos, vel, r, mass):
        body = pymunk.Body()
        body.position = pos
        body.velocity = vel
        shape = pymunk.Circle(body, r)
        shape.mass = mass
        shape.elasticity = 0.6
        shape.friction = 0.5
        shape.color = pygame.Color(self.colors[randint(0, len(self.colors) - 1)])
        self.space.add(body, shape)
        return shape

    def create_box(self, pos, vel, size, mass):
        body = pymunk.Body()
        body.position = pos
        body.velocity = vel
        shape = pymunk.Poly.create_box(body, size, 2)
        shape.mass = mass
        shape.elasticity = 0.6
        shape.friction = 0.5
        shape.color = pygame.Color(self.colors[randint(0, len(self.colors) - 1)])
        self.space.add(body, shape)
        return shape

    def draw_scale(self, dt):
        scale = pygame.draw.rect(
            self.screen,
            pygame.Color('red'),
            pygame.Rect(15, 15, int(dt*100), 20)
                                 )

    def run(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        self.objects = []
        pygame.display.set_caption('Play screen')
        self.add_boundaries()
        t = 0
        t0 = 0
        _run = True
        scale_is_visible = False
        while True:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.PLAY_BG, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.parent.main_menu.run()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    t0 = t
                    scale_is_visible = True
                if event.type == pygame.MOUSEBUTTONUP and t>0.1:
                    self.vscale = max(1, 5*(t-t0))
                    scale_is_visible = False
                    pos = self.pendulum.coordinates(t)
                    vel = [v*self.vscale for v in self.pendulum.velocity(t)]
                    if event.button == 1:
                        r = randint(20, 40)
                        ball = self.create_ball(pos, vel, r, r/20.*10.)
                        self.objects.append(ball)
                    else:
                        box = self.create_box(pos, vel, (randint(40, 80), randint(40, 70)), 10)
                        self.objects.append(box)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        for o in self.objects:
                            self.space.remove(o)
                        self.objects = []

            self.pendulum.draw2(self.screen, self.candy, t)
            self.space.debug_draw(self.pymunk_draw_options)
            if scale_is_visible:
                self.draw_scale(t-t0)
            dt = self.parent.clock.tick(self.parent.fps)/1000
            t += dt
            for i in range(10):
                self.space.step(dt/10)
            pygame.display.update()
