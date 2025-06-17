from config import *

# radiation particles (not fully implemented yet)
class RadiationParticle:
    def __init__(self, origin, direction, color=DEFAULT_COLOR):
        self.pos = pygame.Vector3(origin)
        self.vx, self.vy, self.vz = direction
        self.color = color
        self.age = 0


    def update(self):
        self.age += 1
        self.pos.x += self.vx
        self.pos.y += self.vy
        self.pos.z += self.vz
        self.pos.y += math.sin(self.age * 0.1) *  0.5

        # THIS PART IS IN TEST, WILL BE CHANGED
        '''
        if (self.pos.y > 1 and self.pos.y < 100):
            self.pos.y-= 1
        if (self.pos.y < -1) and (self.pos.y > -100):
            self.pos.y += 1
        '''
        
    def project(self, cameraDistance):
        scale = 400 / (self.pos.z + cameraDistance)
        x2d =  sunCenter[0] + self.pos.x * scale 
        y2d = sunCenter[1] + self.pos.y * scale
        return int(x2d), int(y2d), scale