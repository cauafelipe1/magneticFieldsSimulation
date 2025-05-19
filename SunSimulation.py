from SphereSimulation import *
from RadiationParticle import RadiationParticle

#NOT FULLY IMPLEMENTED YET, a lot of wrong things going on
class SunSimulation(SphereSimulation):
    def __init__(self, particle_num=2000, ray=300, xray=sunCenter[0], yray=sunCenter[1], baseColor=sunColor):
        super().__init__(particle_num=2000, ray=300, xray=sunCenter[0], yray=sunCenter[1], baseColor=sunColor)
        self.radiationEmission = []
    
    def update(self):
        super().update()
        for p in self.radiationEmission:
            p.update()
        origin = (self.ray, 0, 0)
        direction = (2, 0, 0)
        new = RadiationParticle(origin, direction, color=sunColor)
        self.radiationEmission.append(new)
        self.radiationEmission = [p for p in self.radiationEmission if abs(p.x) < 2000] #remove out of vision particles

    def draw(self, screen):
        super().draw(screen)
        for p in self.radiationEmission:
            x2d, y2d, scale = p.project(self.visionRatio)
            size = max(2, int(3 * scale))
            pygame.draw.circle(screen, p.color, (x2d, y2d), size)