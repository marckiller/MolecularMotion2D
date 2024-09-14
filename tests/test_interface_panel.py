import unittest
import pygame
import pygame_gui
from src.interface_panel import InterfacePanel

class TestInterfacePanel(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.manager = pygame_gui.UIManager((800, 600))
        self.interface_panel = InterfacePanel(0, 0, 200, 600, self.manager)
        self.clock = pygame.time.Clock()

    def test_initialization(self):
        self.assertIsNotNone(self.interface_panel.particle_count_input)
        self.assertIsNotNone(self.interface_panel.particle_size_input)
        self.assertIsNotNone(self.interface_panel._reset_button)
        self.assertIsNotNone(self.interface_panel._histogram_button)
        self.assertIsNotNone(self.interface_panel.text_box)

    def test_add_terminal_message(self):
        message = "Test message"
        self.interface_panel.add_terminal_message(message)
        self.assertEqual(self.interface_panel.text_box.text, message)

    def test_reset_button_pressed(self):
        reset_event = pygame.event.Event(pygame_gui.UI_BUTTON_PRESSED, ui_element=self.interface_panel._reset_button.button)
        self.assertTrue(self.interface_panel.check_reset_button(reset_event))

    def test_histogram_button_pressed(self):
        histogram_event = pygame.event.Event(pygame_gui.UI_BUTTON_PRESSED, ui_element=self.interface_panel._histogram_button.button)
        self.assertTrue(self.interface_panel.check_histogram_button(histogram_event))

    def test_update_interface(self):
        dt = self.clock.tick(60) / 1000.0
        self.interface_panel.update(self.screen, dt)
        self.assertIsNotNone(self.interface_panel.manager) #check if GUI elements are updated correctly

    def tearDown(self):
        pygame.quit()

