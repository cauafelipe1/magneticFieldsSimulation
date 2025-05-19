from config import *

class Particle:
    def __init__(self, ray, xray, yray):
        # random particle position generation
        theta = random.uniform(0, 2 * math.pi)
        phi = random.uniform(0, math.pi)
        self.ray = ray
        self.x = ray * math.sin(phi) * math.cos(theta)
        self.y = ray * math.sin(phi) * math.sin(theta)
        self.z = ray * math.cos(phi)
        self.xray = xray
        self.yray = yray
        
    def rotate_y(self, angulo):
        #y-axis rotation
        cos_a = math.cos(angulo)
        sin_a = math.sin(angulo)
        new_X = self.x * cos_a - self.z * sin_a
        new_Z = self.x * sin_a + self.z * cos_a
        self.x, self.z = new_X, new_Z

    def project(self, ratio):
        #3d -> 2d projection
        scale = 400 / (self.z + ratio)  # evita divisão por zero e simula perspectiva
        x2d = self.xray + self.x * scale
        y2d = self.yray + self.y * scale
        return int(x2d), int(y2d), scale