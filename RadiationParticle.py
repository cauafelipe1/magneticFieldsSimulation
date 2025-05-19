from config import *

#NOT FULLY IMPLEMENTED YET
class RadiationParticle:
    def __init__(self, origin, direction, color=DEFAULT_COLOR):
        self.x, self.y, self.z = origin
        self.vx, self.vy, self.vz = direction
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def project(self, distancia_camera):
        scale = 400 / (self.z + distancia_camera)
        x2d =  sunCenter[0] + self.x * scale #not ideal at all, must be general
        y2d = sunCenter[1] + self.y * scale
        return int(x2d), int(y2d), scale