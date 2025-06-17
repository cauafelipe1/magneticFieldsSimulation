from model.SphereSimulation import *
from model.MagneticField import *

# PlanetSimulation inheriting the SphereSimulation class
class PlanetSimulation(SphereSimulation):
    def __init__(self, particle_num=300, ray=200, xray=DEFAULT_CENTER[0], yray=DEFAULT_CENTER[1], baseColor=(50, 100, 255)):
        super().__init__(particle_num, ray, xray, yray, baseColor)
        self.visionRatio = 600
        self.magneticField = MagneticField(60, self.ray, xray, yray) # has a magnetic field (will be optional in the future)

    # update and draw all particles including the magnetic field
    def update(self):
        super().update()
        self.magneticField.update()

    def draw(self, screen):
        super().draw(screen)
        self.magneticField.draw(screen)
