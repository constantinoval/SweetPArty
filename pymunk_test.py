import pygame
import pymunk
import pymunk.pygame_util
from random import randint

pygame.init()
window = pygame.display.set_mode((800, 600))
space = pymunk.Space()
space.gravity = (0, 980)
draw_options = pymunk.pygame_util.DrawOptions(window)
run = True
clock = pygame.time.Clock()
fps = 60
colors = ('red', 'green', 'blue', 'orange')

def draw(window, space, draw_options):
    window.fill('white')
    space.debug_draw(draw_options)
    pygame.display.flip()

def create_ball(space, radius, mass, pos=(400, 100)):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 0.5
    shape.friction = 0.5
    space.add(body, shape)
    return space

def create_box(space, size, mass, pos=(400, 100)):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Poly.create_box(body, size, 2)
    shape.mass = mass
    shape.elasticity = 0.5
    shape.friction = 0.5
    shape.color = pygame.Color(colors[randint(0, len(colors)-1)])
    space.add(body, shape)
    return space

def create_floor(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (800/2, 600-5)
    shape = pymunk.Poly.create_box(body, (800, 100))
    shape.elasticity = 1
    shape.friction = 0.5
    space.add(body, shape)
    return shape

# ball = create_ball(space, 50, 10)
floor = create_floor(space)

while run:
    dt = clock.tick(fps) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                create_ball(space, 30, 10, event.pos)
            else:
                create_box(space, (randint(40, 80), randint(40,70)), 10, event.pos)
    for i in range(100):
        space.step(dt/100)
    draw(window, space, draw_options)

pygame.quit()