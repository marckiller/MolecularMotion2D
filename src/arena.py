import random
import math
from src.particle import Particle

class Arena:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []

    def add_particles(self, number, radius, velocity) -> str:
        
        max_number_of_tries = 1000
        placed = False
        not_placed = 0

        for _ in range(number):

            placed = False

            for _ in range(max_number_of_tries):

                x = random.uniform(radius, self.width - radius)
                y = random.uniform(radius, self.height - radius)

                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                angle = random.uniform(0, 2 * math.pi)
                vx = velocity * math.cos(angle)
                vy = velocity * math.sin(angle)

                new_particle = Particle(x, y, radius, vx, vy, color)

                if not self.is_overlapping(new_particle):
                    self.particles.append(new_particle)
                    placed = True
                    break

            if not placed:
                not_placed += 1
        
        if not_placed == 0:
            return f"Successfully placed {number} particles."
        
        else:
            return f"Failed to place {not_placed} from {number} particles. Decrease the size of praticles."

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

    def get_kinetic_energies(self):
        return [particle.kinetic_energy() for particle in self.particles]
