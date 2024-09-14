import unittest
import pygame
from unittest.mock import patch
from src.app_window import AppWindow


class TestAppWindow(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.app = AppWindow(800, 600)
        self.screen = pygame.display.set_mode((800, 600))

    def tearDown(self):
        pygame.quit()

    @patch('src.app_window.Arena')
    @patch('src.app_window.InterfacePanel')
    def test_initialization(self, mock_interface, mock_arena):
        app = AppWindow(800, 600)
        self.assertEqual(app.width, 800)
        self.assertEqual(app.height, 600)
        self.assertIsNotNone(app.arena)
        self.assertIsNotNone(app.interface)
        self.assertIsNotNone(app.histogram_manager)

    def test_reset_simulation_invalid_input(self):
        self.app.interface.particle_count_input.set_text("invalid")
        self.app.interface.particle_size_input.set_text("invalid")
        self.app.reset_simulation()

        expected_message = "Invalid input. Please enter valid numbers."
        actual_message = self.app.interface.text_box.text.replace("\n", " ")
        self.assertIn(expected_message, actual_message)

    def test_reset_simulation_valid_input(self):
        self.app.interface.particle_count_input.set_text("60")
        self.app.interface.particle_size_input.set_text("10")
        self.app.reset_simulation()

        expected_message = "Successfully placed 60 particles."
        actual_message = self.app.interface.text_box.text.replace("\n", " ")
        self.assertIn(expected_message, actual_message)

    @patch('multiprocessing.Process')
    def test_display_kinetic_energy_histogram(self, mock_process):
        self.app.display_kinetic_energy_histogram()

        mock_process.assert_called()

    def test_show_logo(self):
        with patch('pygame.display.flip') as mock_flip:
            self.app.show_logo()

        mock_flip.assert_called()

    @patch('pygame.event.get')
    def test_run(self, mock_event_get):
        mock_event_get.return_value = [pygame.event.Event(pygame.QUIT)]

        with patch('pygame.display.flip') as mock_flip:
            self.app.run()

        self.assertFalse(self.app.running)
        mock_flip.assert_called()

    def test_draw_arena(self):
        self.app.arena.particles = []
        self.app.arena.draw(self.screen)
        pygame.display.flip()

        self.assertIsNotNone(self.app.arena)

    def test_update_arena(self):
        self.app.arena.add_particles(1, 10, 100)
        initial_x = self.app.arena.particles[0].x
        self.app.arena.update(1.0)
        updated_x = self.app.arena.particles[0].x

        self.assertNotEqual(initial_x, updated_x)