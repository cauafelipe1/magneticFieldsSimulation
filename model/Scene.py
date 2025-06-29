from model.PlanetSimulation import *
from model.SunSimulation import *

#scene sample class
class Scene:
    def __init__(self, numberOfSuns, numberOfPlanets, sunX, planetX):
        self.suns = []
        self.planets = []
        self.sunX = sunX
        self.planetX = planetX
        self.getSun(numberOfSuns)
        self.getPlanets(numberOfPlanets)

    #get all suns of the scene
    def getSun(self, numberOfSuns):
        for i in range(numberOfSuns):
            x = self.sunX[i][0] * WIDTH // self.sunX[i][1]
            newSun = SunSimulation(particle_num=6000, ray=300, xray=x, yray=HEIGHT // 2)
            self.suns.append(newSun)

    #get all planets of the scene
    def getPlanets(self, numberOfPlanets):
        for i in range(numberOfPlanets):
            x = self.planetX[i][0] * WIDTH // self.planetX[i][1]
            if x == earthCenter[0]:
                newPlanet = PlanetSimulation(ray=100, xray=x, yray=HEIGHT // 2, baseColor=earthColor, hasMagneticField=True) #hardcoded
            else:
                newPlanet = PlanetSimulation(ray=random.uniform(70, 110), xray=x, yray=HEIGHT // 2, baseColor=random.choice(COLORS)[1])
            self.planets.append(newPlanet)

    #functions to draw and update all elements in the scene
    def update(self, screenWidth, screenHeight):
        for sun in self.suns:
            sun.update(screenWidth, screenHeight)
        for planet in self.planets:
            planet.update()

    def draw(self, screen):
        for sun in self.suns:
            sun.draw(screen)
        for planet in self.planets:
            planet.draw(screen)
