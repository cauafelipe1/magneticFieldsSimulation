from model.Scene import *
import time

#main simulation class
class Simulation:
    def __init__(self, screen, sourceFile="setup.txt"): #gets the screen and setup via source file
        self.scenes = []
        self.currentSceneIndex = 0
        self.sceneTimer = time.time()
        self.loadScene(sourceFile)
        self.screen = screen
    
    def loadScene(self, fileName):
        with open(fileName, "r") as file:
            lines = file.readlines()
        
        sunCounter = 0
        planetCounter = 0
        sunX = []
        planetX = []

        for line in lines:
            line = line.strip().lower()
            if line.startswith("scene"):
                sunCounter = 0
                planetCounter = 0
                sunX = []
                planetX = []
            elif line.startswith("sun ->"):
                sunCounter = int(line.split("->")[1])
            elif line.startswith("sunx ->"):
                values = line.split("->")[1].strip()
                sunX = eval(values)
                if isinstance(sunX[0], int):  # single sun
                    sunX = [sunX]
            elif line.startswith("planet ->"):
                planetCounter = int(line.split("->")[1])
            elif line.startswith("planetx ->"):
                values = line.split("->")[1].strip()
                planetX = eval(values)
                if isinstance(planetX[0], int):  # single planet
                    planetX = [planetX]
            elif line.startswith("---"):
                scene = Scene(sunCounter, planetCounter, sunX, planetX)
                self.scenes.append(scene)

        
    def update(self):
        current_time = time.time()
        if current_time - self.sceneTimer >= 30:
             self.sceneTimer = current_time
             self.currentSceneIndex = (self.currentSceneIndex + 1) % len(self.scenes)


        self.scenes[self.currentSceneIndex].update(WIDTH, HEIGHT)

    def draw(self, screen):
        self.scenes[self.currentSceneIndex].draw(screen)
