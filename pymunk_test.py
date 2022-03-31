def add_boundaries(space, width, height):
    rects = [
        ((width // 2, height - 5), (width, 10)),
        ((width // 2, 5), (width, 10)),
        ((5, height // 2), (10, height)),
        ((width - 5, height // 2), (10, height)),
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
    shape.color = pygame.Color(colors[randint(0, len(colors) - 1)])
    space.add(body, shape)
    return shape


add_boundaries(space, WIDTH, HEIGHT)

t = 0

pend = Pendulum(length=300,
                omega=pi / 4,
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
                box = create_box(space, pos, vel, (randint(40, 80), randint(40, 70)), 10)
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
    dt = clock.tick(FPS) / 1000
    t += dt
    for i in range(10):
        space.step(dt / 10)
pygame.quit()