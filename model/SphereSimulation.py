from config import *
from model.Particle import Particle

#sphere simulation sample
class SphereSimulation:
    def __init__(self, particle_num=300, ray=200, xray=DEFAULT_CENTER[0], yray=DEFAULT_CENTER[1], baseColor= DEFAULT_COLOR):
        self.particles = [Particle(ray, xray, yray) for _ in range(particle_num)]
        self.angle = 0
        self.speed = 0.01
        self.visionRatio = 600
        self.baseColor = baseColor
        self.ray = ray

    def update(self):
        #update all particle rotation
        self.angle += self.speed
        for p in self.particles:
            p.rotate_y(self.speed)

    def draw(self, screen):
        #project and draw particles
        for p in self.particles:
            x2d, y2d, scale = p.project(self.visionRatio)
            size = max(1, int(3 * scale))
            color = tuple(min(255, int(c * scale)) for c in self.baseColor)
            pygame.draw.circle(screen, color, (x2d, y2d), size)