import unittest
from src.particle import Particle

class TestParticle(unittest.TestCase):

    def setUp(self):
        self.particle1 = Particle(50, 50, 10, 5, 0, (255, 0, 0))  # Moving horizontally
        self.particle2 = Particle(100, 50, 10, -5, 0, (0, 255, 0))  # Moving towards particle1

    def test_initialization(self):
        self.assertEqual(self.particle1.x, 50)
        self.assertEqual(self.particle1.y, 50)
        self.assertEqual(self.particle1.radius, 10)
        self.assertEqual(self.particle1.vx, 5)
        self.assertEqual(self.particle1.vy, 0)
        self.assertEqual(self.particle1.color, (255, 0, 0))

    def test_move(self):
        self.particle1.move(1)  # Move for 1 second
        self.assertEqual(self.particle1.x, 55)  # New X position should be 50 + 5*1
        self.assertEqual(self.particle1.y, 50)  # Y position should remain the same

    def test_bounce(self):
        self.particle1.x = 5
        self.particle1.bounce(100, 100)  # Width and height of the arena are 100
        self.assertEqual(self.particle1.vx, -5)

        self.particle1.y = 5
        self.particle1.bounce(100, 100)
        self.assertEqual(self.particle1.vy, 0)

    def test_collision(self):
        self.particle1.x = 0
        self.particle1.y = 0
        self.particle2.x = self.particle1.radius + self.particle2.radius - 0.0001 # Slightly overlapping
        self.particle2.y = 0
        
        self.particle1.vx = 5
        self.particle1.vy = 0
        self.particle2.vx = -5
        self.particle2.vy = 0
        
        self.particle1.collide(self.particle2)
        self.assertEqual(self.particle1.vx, -5)
        self.assertEqual(self.particle2.vx, 5)

    def test_kinetic_energy(self):
        energy = self.particle1.kinetic_energy()
        self.assertEqual(energy, 25)

    def test_is_overlapping(self):
        overlapping_particle = Particle(60, 50, 10, 0, 0, (0, 0, 255))
        non_overlapping_particle = Particle(200, 50, 10, 0, 0, (0, 0, 255))

        self.assertTrue(self.particle1.is_overlapping(overlapping_particle))
        self.assertFalse(self.particle1.is_overlapping(non_overlapping_particle))