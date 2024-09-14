import unittest
import random
from src.particle import Particle
from src.arena import Arena

class TestArena(unittest.TestCase):

    def setUp(self):
        self.width = 800
        self.height = 600
        self.arena = Arena(self.width, self.height)
        random.seed(0)

    def test_add_particles_success(self):
        message = self.arena.add_particles(5, 10, 50)
        self.assertEqual(len(self.arena.particles), 5)
        self.assertIn("Successfully placed", message)

    def test_add_particles_failure(self):
        message = self.arena.add_particles(50, 200, 50)
        self.assertLess(len(self.arena.particles), 50)
        self.assertIn("Failed to place", message)

    def test_is_overlapping(self):
        particle1 = Particle(100, 100, 20, 0, 0, (255, 0, 0))
        particle2 = Particle(110, 100, 20, 0, 0, (0, 255, 0))

        self.arena.particles.append(particle1)
        self.assertTrue(self.arena.is_overlapping(particle2))

        particle3 = Particle(200, 200, 20, 0, 0, (0, 0, 255))# no overlap
        self.assertFalse(self.arena.is_overlapping(particle3))

    def test_update(self):
        particle1 = Particle(100, 100, 20, 50, 0, (255, 0, 0))
        particle2 = Particle(200, 200, 20, -50, 0, (0, 255, 0))

        self.arena.particles.append(particle1)
        self.arena.particles.append(particle2)

        # Update arena for 1 second
        self.arena.update(1.0)

        # Check if particles moved
        self.assertNotEqual(particle1.x, 100)
        self.assertNotEqual(particle2.x, 200)

    def test_get_kinetic_energies(self):
        particle = Particle(100, 100, 20, 50, 0, (255, 0, 0))
        self.arena.particles.append(particle)

        energies = self.arena.get_kinetic_energies()
        self.assertEqual(len(energies), 1)
        self.assertAlmostEqual(energies[0], 2500)

    def test_reset(self):
        self.arena.add_particles(5, 10, 50)
        self.assertEqual(len(self.arena.particles), 5)

        self.arena.reset()
        self.assertEqual(len(self.arena.particles), 0)
