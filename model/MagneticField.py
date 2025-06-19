from model.MagneticParticle import *

# magnetic field compound of magnetic particles
class MagneticField:
    def __init__(self, particleNum, ray, xray, yray, baseColor= (255, 255, 255)):
        self.leftParticles = [MagneticParticle(ray+30, xray-50, yray) for _ in range(particleNum)]
        self.rightParticles = [MagneticParticle(ray+30, xray+50, yray, right=True) for _ in range(particleNum)]

        self.angle = 0
        self.speed = 0.01
        self.visionRatio = 600
        self.baseColor = baseColor
        self.ray = ray

    #update position of both parts of the magnetic field
    def update(self):
        self.angle += self.speed
        for lp in self.leftParticles:
            lp.updatePos(0.01)

        for rp in self.rightParticles:
            rp.updatePos(0.01)

    def draw(self, screen):
        #project and draw particles just like other simulation classes (CAN BE IMPROVED)
        for p in self.leftParticles:
            x2d, y2d, scale = p.project(self.visionRatio)
            size = max(1, int(3 * scale))
            color = tuple(min(255, int(c * scale)) for c in self.baseColor)
            pygame.draw.circle(screen, color, (x2d, y2d), size)
        for p in self.rightParticles:
            x2d, y2d, scale = p.project(self.visionRatio)
            size = max(1, int(3 * scale))
            color = tuple(min(255, int(c * scale)) for c in self.baseColor)
            pygame.draw.circle(screen, color, (x2d, y2d), size)