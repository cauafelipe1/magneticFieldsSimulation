from config import *

# radiation particles (not fully implemented yet)
class RadiationParticle:
    def __init__(self, origin, direction, color=DEFAULT_COLOR):
        self.pos = pygame.Vector3(origin)
        self.vx, self.vy, self.vz = direction
        self.color = color
        self.age = 0
        self.xponential = 0
        self.pos.z = self.vz

    #update particle position
    def update(self):
        self.age += 1
        self.pos.x += self.vx
        self.pos.y += self.vy 
        self.pos.z += self.vz
        self.pos.y += math.sin(self.age * 0.1) *  0.5
        
        # vector operations on a particle to not hit the magnetic field
        if (self.pos.x > 1180) and (-150 < self.pos.y < 150):
            if (-1 < self.pos.y < 1):  
                if (random.randint(0,1)) == 0:
                    self.pos.y += 1
                else:
                    self.pos.y -= 1
            else:
                if self.pos.y >= 1:
                    self.pos.y +=1
                else:
                    self.pos.y -= 1
            self.pos.x -= 1.3
                          
        

    def project(self, cameraDistance):
        scale = 400 / (self.pos.z + cameraDistance)
        x2d =  sunCenter[0] + self.pos.x * scale 
        y2d = sunCenter[1] + self.pos.y * scale
        return int(x2d), int(y2d), scale