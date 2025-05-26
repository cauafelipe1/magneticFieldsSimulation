from config import *

class Particle:
    def __init__(self, ray, xray, yray):
        # random particle position generation
        self.theta = random.uniform(0, 2 * math.pi)
        self.phi = random.uniform(0, math.pi)
        self.ray = ray
        self.particleVector = pygame.math.Vector3((ray * math.sin(self.phi) * math.cos(self.theta)),
                                    (ray * math.sin(self.phi) * math.sin(self.theta)), ray * math.cos(self.phi))
        self.xray = xray
        self.yray = yray
        
    def rotate_y(self, angulo):
        #y-axis rotation
        self.particleVector.rotate_y_rad_ip((-1) * angulo)

    def project(self, ratio):
        #3d -> 2d projection
        scale = 400 / (self.particleVector.z + ratio)  # avoid division by zero
        x2d = self.xray + self.particleVector.x * scale
        y2d = self.yray + self.particleVector.y * scale
        return int(x2d), int(y2d), scale
    
  
  
    