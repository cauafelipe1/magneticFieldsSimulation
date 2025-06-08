from config import *

# radiation particles (not fully implemented yet)
class RadiationParticle:
    def __init__(self, origin, direction, color=DEFAULT_COLOR):
        self.x, self.y, self.z = origin
        self.vx, self.vy, self.vz = direction
        self.color = color
        self.age = 0

    def update(self):
        self.age += 1
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        self.y += math.sin(self.age * 0.1) *  0.5

    def project(self, cameraDistance):
        scale = 400 / (self.z + cameraDistance)
        x2d =  sunCenter[0] + self.x * scale 
        y2d = sunCenter[1] + self.y * scale
        return int(x2d), int(y2d), scale