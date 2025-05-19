from SphereSimulation import * #not ideal import strategy

#pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Earth's Magnetic Field simulation (no field at all yet)")
clock = pygame.time.Clock()

#objects instantiation
earth = SphereSimulation(particle_num=500, ray=100, xray=earthCenter[0], yray=earthCenter[1], baseColor=earthColor)
earth.visionRatio = 800
sun = SphereSimulation(particle_num=2000, ray=300, xray=sunCenter[0], yray=sunCenter[1], baseColor=sunColor)

#main loop
on = True
while on:
    screen.fill((0, 0, 0))

    #tests on keyboard controlling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            earth.speed += 0.01
        if keys[pygame.K_DOWN]:
            earth.speed = max(0, earth.speed - 0.01)

        if keys[pygame.K_w]:
            earth.visionRatio = max(100, earth.visionRatio - 10)
        if keys[pygame.K_s]:
            earth.visionRatio += 10

    earth.update()
    earth.draw(screen)
    sun.update()
    sun.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()