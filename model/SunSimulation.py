from model.SphereSimulation import *
from model.RadiationParticle import RadiationParticle
from model.SunParticle import SunParticle

# almost fully implemented, need to be polished a bit
class SunSimulation(SphereSimulation):
    def __init__(self, particle_num=2000, ray=300, xray=sunCenter[0], yray=sunCenter[1], baseColor=sunColor):
        super().__init__(particle_num=2000, ray=300, xray=sunCenter[0], yray=sunCenter[1], baseColor=sunColor)
        self.particles = [SunParticle(ray, xray, yray) for _ in range(particle_num)]
        self.radiationEmission = []
        self.emissionCounter = 0
        self.emissionInterval = 3

    def update(self, screen_width, screen_height):
      for s in self.particles:
          s.wiggle()
      
      # updates and filters the visible particles
      visible_radiation = []

      for p in self.radiationEmission:
          p.update()
          x2d, y2d, _ = p.project(self.visionRatio)
          if 0 <= x2d < screen_width and 0 <= y2d < screen_height:
              visible_radiation.append(p)
      self.radiationEmission = visible_radiation

      self.emissionCounter += 1
      if self.emissionCounter >= self.emissionInterval:
          y = random.uniform(-(self.ray + 30), (self.ray + 30))
          z = random.uniform(-self.ray / 2, self.ray / 2)
          origin = (self.ray - 100, y, z)
          direction = (2, 0, 0)
          new = RadiationParticle(origin, direction, color=sunColor)
          self.radiationEmission.append(new)
          self.emissionCounter = 0


    #draw sun particles and also its radiation
    def draw(self, screen):
        super().draw(screen)
        for p in self.radiationEmission:
            x2d, y2d, scale = p.project(self.visionRatio)
            size = max(2, int(3 * scale))
            pygame.draw.circle(screen, p.color, (x2d, y2d), size)