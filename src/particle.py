import math
import random 

class Particle:

    def __init__(self, x, y, radius, velocity, color):

        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity
        self.angle = random.uniform(0, 2 * math.pi)

        self.vx = self.velocity * math.cos(self.angle)
        self.vy = self.velocity * math.sin(self.angle)

        self.color = color

    def move(self):

        self.x += self.vx
        self.y += self.vy

    def collide(self, particle):
        dx = self.x - particle.x
        dy = self.y - particle.y
        distance = math.hypot(dx, dy)

        if distance < self.radius + particle.radius:
            #masses are equal
            self.vx, particle.vx = particle.vx, self.vx
            self.vy, particle.vy = particle.vy, self.vy

    def kinetic_energy(self):
        return 0.5 * (self.vx ** 2 + self.vy ** 2)
    
    def is_overlapping(self, particle):
        distance = math.hypot(self.x - particle.x, self.y - particle.y)
        return distance < self.radius + particle.radius
    
    def draw(self, screen):
        pass

    
