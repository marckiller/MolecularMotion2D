import random
import math
import pygame
from src.particle import Particle
from typing import List

class Arena:

    def __init__(self, width: int, height: int) -> None:
        """Initialize the arena with given width and height."""
        self.width = width
        self.height = height
        self.particles: List[Particle] = []

    def add_particles(self, number: int, radius: float, velocity: float) -> str:
        """
        Try to add a given number of particles with a specific radius and velocity.
        Returns a message indicating success or failure to place all particles.
        """
        max_tries = 1000  # Maximum attempts to place each particle
        not_placed = 0

        for _ in range(number):
            placed = False

            for _ in range(max_tries):
                # Randomize position and velocity direction
                x = random.uniform(radius, self.width - radius)
                y = random.uniform(radius, self.height - radius)
                angle = random.uniform(0, 2 * math.pi)
                vx = velocity * math.cos(angle)
                vy = velocity * math.sin(angle)

                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                new_particle = Particle(x, y, radius, vx, vy, color)

                # Check if new particle is overlapping with existing ones
                if not self.is_overlapping(new_particle):
                    self.particles.append(new_particle)
                    placed = True
                    break

            if not placed:
                not_placed += 1

        if not_placed == 0:
            return f"Successfully placed {number} particles."
        return f"Failed to place {not_placed} out of {number} particles. Decrease particle size."

    def is_overlapping(self, new_particle: Particle) -> bool:
        """Check if a new particle is overlapping with any existing particle."""
        for particle in self.particles:
            distance = math.hypot(new_particle.x - particle.x, new_particle.y - particle.y)
            if distance < new_particle.radius + particle.radius:
                return True
        return False

    def update(self, dt: float) -> None:
        """Update the positions of all particles and handle collisions."""
        for particle in self.particles:
            particle.move(dt)
            particle.bounce(self.width, self.height)

        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                self.particles[i].collide(self.particles[j])

    def draw(self, screen: pygame.Surface) -> None:
        """Draw all particles on the given screen."""
        for particle in self.particles:
            particle.draw(screen)

    def get_kinetic_energies(self) -> List[float]:
        """Return a list of kinetic energies of all particles."""
        return [particle.kinetic_energy() for particle in self.particles]
    
    def reset(self) -> None:
        """Remove all particles from the arena."""
        self.particles = []
