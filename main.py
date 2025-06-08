from model.Starfield import *
from model.SunSimulation import *
from model.PlanetSimulation import PlanetSimulation
#pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Earth's Magnetic Field simulation (magnetic field still in process of build)")
clock = pygame.time.Clock()

#objects instantiation
earth = PlanetSimulation(particle_num=500, ray=100, xray=earthCenter[0], yray=earthCenter[1], baseColor=earthColor)
sun = SunSimulation(particle_num=10000, ray=300, xray=sunCenter[0], yray=sunCenter[1], baseColor=sunColor)
stars = Starfield(200)


#main loop
def main():
    on = True
    while on:
        screen.fill((0, 0, 0))

        #quit controll
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

        #main simulation objects
        earth.update()
        earth.draw(screen)
        sun.update()
        sun.draw(screen)

        #starry background addition
        fade = pygame.Surface((WIDTH, HEIGHT))
        fade.set_alpha(40)
        fade.fill((0, 0, 0))
        screen.blit(fade, (0, 0))
        stars.update()
        TIME = pygame.time.get_ticks() / 1000
        stars.draw(screen, TIME)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()