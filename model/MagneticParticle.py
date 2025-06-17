from model.Particle import *

# Particle class inheritance
class MagneticParticle(Particle):
    def __init__(self, ray, xray, yray, right=False):
        super().__init__(ray, xray, yray)
        self.theta = random.uniform(math.pi/3, (5 * math.pi)/3) # theta to vary from pi/3 to 5pi/3
        self.xray = xray
        self.yray = yray
        self.right = right
        self.updatePos(0.00)
    
    #incrementing theta and updating particle position
    def updatePos(self, increment):
        if (self.theta + increment) > (5*math.pi/3):
            self.theta = math.pi/3
        self.theta += increment
        self.particleVector = pygame.math.Vector3(
            self.ray * math.cos(self.theta),
            self.ray * math.sin(self.theta),
            0
        )
        if self.right:
            self.rotate_y(math.pi) #rotates on y-axis the right part of the magnetic field simulated



    def project(self, ratio):
        return super().project(ratio)
