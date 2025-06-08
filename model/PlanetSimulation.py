from model.SphereSimulation import *
from model.MagneticFieldParticles import *

# TO BE IMPLEMENTED
class PlanetSimulation(SphereSimulation):
    def __init__(self, particle_num=300, ray=200, xray=..., yray=..., baseColor=...):
        super().__init__(particle_num, ray, xray, yray, baseColor)
        self.visionRatio = 600
        self.magneticField = [MagneticFieldParticles]

    def update(self):
        return super().update()
    
    def draw(self, screen):
        return super().draw(screen)