import random
import math
from src.particle import Particle

class Arena:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []

    def add_particles(self, number, radius, velocity):

        for _ in range(number):
            while True:

                x = random.uniform(radius, self.width - radius)
                y = random.uniform(radius, self.height - radius)

                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                new_particle = Particle(x, y, radius, velocity[0], velocity[1], color)

                if not self.is_overlapping(new_particle):
                    #TODO: maybe there is more elegant way to do this
                    self.particles.append(new_particle)
                    break

    def is_overlapping(self, new_particle):

        for particle in self.particles:

            distance = math.hypot(new_particle.x - particle.x, new_particle.y - particle.y)

            if distance < new_particle.radius + particle.radius:
                return True
            
        return False

    def update(self, dt):

        for particle in self.particles:
            particle.move(dt)
            particle.bounce(self.width, self.height)

        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                self.particles[i].collide(self.particles[j])

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
