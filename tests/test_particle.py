import unittest
import math
import pygame
from src.particle import Particle 

class TestParticle(unittest.TestCase):

    def setUp(self):
        self.particle1 = Particle(50, 50, 10, 5, (255, 0, 0))
        self.particle2 = Particle(70, 50, 10, 5, (0, 255, 0))
        self.screen = pygame.display.set_mode((200, 200))

    def test_move(self):
        initial_x, initial_y = self.particle1.x, self.particle1.y
        self.particle1.move()
        self.assertNotEqual(initial_x, self.particle1.x)
        self.assertNotEqual(initial_y, self.particle1.y)

    def test_collide(self):
        self.particle1.x, self.particle1.y = 50, 50
        self.particle2.x, self.particle2.y = 60, 50
        self.particle1.collide(self.particle2)
        self.assertNotEqual(self.particle1.vx, self.particle2.vx)
        self.assertNotEqual(self.particle1.vy, self.particle2.vy)

    def test_kinetic_energy(self):
        energy1 = self.particle1.kinetic_energy()
        self.assertGreater(energy1, 0)

    def test_is_overlapping(self):
        self.particle1.x, self.particle1.y = 50, 50
        self.particle2.x, self.particle2.y = 55, 50
        self.assertTrue(self.particle1.is_overlapping(self.particle2))

        self.particle2.x, self.particle2.y = 70, 50
        self.assertFalse(self.particle1.is_overlapping(self.particle2))

    def test_draw(self):
        pass

if __name__ == '__main__':
    unittest.main()
