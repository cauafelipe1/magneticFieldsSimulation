from model.Starfield import *
from model.Simulation import *
#pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Earth's Magnetic Field simulation")
clock = pygame.time.Clock()

#objects instantiation
simulation = Simulation(screen, "setup.txt")
stars = Starfield(200)


#main loop
def main():
    on = True
    while on:

        #quit controll
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

        screen.fill((0, 0, 0))
        #main simulation objects
        simulation.update()
        simulation.draw(screen)

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