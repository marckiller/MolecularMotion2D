import math
import pygame

class Particle:

    def __init__(self, x, y, radius, vx, vy, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = vx # X/Y axis velocity
        self.vy = vy
        self.color = color

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def bounce(self, width, height):
        if self.x - self.radius < 0:
            self.vx = -self.vx
            self.x = self.radius  #set particle on the edge of the wall after bounce
        elif self.x + self.radius > width:
            self.vx = -self.vx
            self.x = width - self.radius

        if self.y - self.radius < 0:
            self.vy = -self.vy
            self.y = self.radius  #set particle on the edge of the wall after bounce
        elif self.y + self.radius > height:
            self.vy = -self.vy
            self.y = height - self.radius
            
    def collide(self, particle):
        dx = self.x - particle.x
        dy = self.y - particle.y
        distance = math.hypot(dx, dy)

        if distance < self.radius + particle.radius:
            nx = dx / distance # Normalized vector
            ny = dy / distance

            dvx = self.vx - particle.vx
            dvy = self.vy - particle.vy
            vn = dvx * nx + dvy * ny

            if vn < 0:
                self.vx -= vn * nx
                self.vy -= vn * ny
                particle.vx += vn * nx
                particle.vy += vn * ny

    def kinetic_energy(self):
        return self.vx ** 2 + self.vy ** 2

    def is_overlapping(self, particle):
        distance = math.hypot(self.x - particle.x, self.y - particle.y)
        return distance < self.radius + particle.radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
