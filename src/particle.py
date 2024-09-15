import math
import pygame
from typing import Tuple

class Particle:
    """A particle in the simulation with position, velocity, radius, and color."""
    
    def __init__(self, x: float, y: float, radius: float, vx: float, vy: float, color: Tuple[int, int, int]) -> None:
        """Initialize a particle with position, velocity, radius, and color."""
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = vx  # Velocity in the X axis
        self.vy = vy  # Velocity in the Y axis
        self.color = color

    def move(self, dt: float) -> None:
        """Move the particle according to its velocity and the time delta (dt)."""
        self.x += self.vx * dt
        self.y += self.vy * dt

    def bounce(self, width: float, height: float) -> None:
        """Handle bouncing of the particle when it hits the walls of the arena."""
        # Check for collision with vertical walls (left and right)
        if self.x - self.radius < 0:
            self.vx = -self.vx
            self.x = self.radius  # Set particle on the edge of the wall after bounce
        elif self.x + self.radius > width:
            self.vx = -self.vx
            self.x = width - self.radius

        # Check for collision with horizontal walls (top and bottom)
        if self.y - self.radius < 0:
            self.vy = -self.vy
            self.y = self.radius
        elif self.y + self.radius > height:
            self.vy = -self.vy
            self.y = height - self.radius

    def collide(self, particle: "Particle") -> None:
        """Handle elastic collision between this particle and another particle."""
        dx = self.x - particle.x
        dy = self.y - particle.y
        distance = math.hypot(dx, dy)

        if distance < self.radius + particle.radius:

            if distance < 1e-8: # Prevent division by zero
                distance = 1e-8
            # Normalized collision vector
            nx = dx / distance
            ny = dy / distance

            # Relative velocity in the normal direction
            dvx = self.vx - particle.vx
            dvy = self.vy - particle.vy
            vn = dvx * nx + dvy * ny

            # If particles are moving towards each other, apply elastic collision
            if vn < 0:
                self.vx -= vn * nx
                self.vy -= vn * ny
                particle.vx += vn * nx
                particle.vy += vn * ny

    def kinetic_energy(self) -> float:
        """Return the kinetic energy of the particle."""
        return self.vx ** 2 + self.vy ** 2

    def is_overlapping(self, particle: "Particle") -> bool:
        """Check if this particle is overlapping with another particle."""
        return self._distance_to(particle) < self.radius + particle.radius

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the particle on the screen."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def _distance_to(self, particle: "Particle") -> float:
        """Calculate the distance to another particle."""
        dx = self.x - particle.x
        dy = self.y - particle.y
        return math.hypot(dx, dy)
