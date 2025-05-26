from model.Particle import *

class SunParticle(Particle):
    def __init__(self, ray, xray, yray):
        super().__init__(ray, xray, yray)

        # slightly movimentation
        self.dtheta = random.uniform(-0.001, 0.01) #still trying to find out how this random "pattern" works
        self.dphi = random.uniform(-0.01, 0.001)
        self.updatePosition()
    
    def updatePosition(self):
        self.particleVector = pygame.math.Vector3 (
            self.ray * math.sin(self.phi) * math.cos(self.theta),
            self.ray * math.sin(self.phi) * math.sin(self.theta),
            self.ray * math.cos(self.phi)
        )

    def wiggle(self):
        self.theta += self.dtheta
        self.phi += self.dphi

        if not 0 < self.phi < math.pi:
            self.dphi *= -1
            self.phi += self.dphi

        if not 0 < self.theta < 2 * math.pi:
            self.dtheta *= -1
            self.theta += self.dtheta

        self.updatePosition()