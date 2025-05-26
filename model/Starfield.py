from model.Star import *

#background starfield simulation
class Starfield:
    def __init__(self, num, screenWidth=WIDTH, screenHeight=HEIGHT):
        self.stars = [Star(screenWidth, screenHeight) for _ in range(num)]

    def draw(self, surface, time):
        for s in self.stars:
            s.draw(surface, time)

    def update(self):
        for s in self.stars:
            s.update()
            
