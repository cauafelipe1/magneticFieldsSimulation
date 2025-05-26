from config import *

# background stars particles
class Star:
    def __init__(self, screenWidth=WIDTH, screenHeight=HEIGHT, depth=10000):
        self.depth = depth
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.reset()

    def reset(self):
        #r reset particle position
        self.position = pygame.math.Vector3(random.uniform(-self.screenWidth, self.screenWidth), 
                                            random.uniform(-self.screenHeight, self.screenHeight),
                                            self.depth)
        self.phase = random.uniform(0, 2 * math.pi)

    def update(self, angle=0.0001):
        # apply slight rotation o xOy axis
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        x, y = self.position.x, self.position.y
        self.position.x = x * cos_a - y * sin_a
        self.position.y = x * sin_a + y * cos_a


    def draw(self, surface, time):
        x = int(self.position.x + self.screenWidth / 2)
        y = int(self.position.y + self.screenHeight / 2)
        if (0 <= x < self.screenWidth and 0 <= y < self.screenHeight): # draw if a star is on screen
            brightness = int(180 + 75 * math.sin(time + self.phase))
            color = (brightness, brightness, 255)
            pygame.draw.circle(surface, color, (x, y), 1)
    