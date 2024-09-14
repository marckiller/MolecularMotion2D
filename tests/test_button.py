import unittest
import pygame
import pygame_gui
from src.button import Button

class TestButton(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.window_surface = pygame.display.set_mode((self.width, self.height))
        self.ui_manager = pygame_gui.UIManager((self.width, self.height))
        self.button = Button(100, 100, 200, 50, "Test Button", self.ui_manager)

    def test_button_creation(self):
        self.assertIsNotNone(self.button.button)
        self.assertEqual(self.button.button.text, "Test Button")
        self.assertEqual(self.button.button.relative_rect.x, 100)
        self.assertEqual(self.button.button.relative_rect.y, 100)
        self.assertEqual(self.button.button.relative_rect.width, 200)
        self.assertEqual(self.button.button.relative_rect.height, 50)

    def test_check_pressed(self):
        event = pygame.event.Event(pygame_gui.UI_BUTTON_PRESSED, {'ui_element': self.button.button})
        self.assertTrue(self.button.check_pressed(event))

    def test_check_not_pressed(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN) #any event that is not UI_BUTTON_PRESSED
        self.assertFalse(self.button.check_pressed(event))

    def tearDown(self):
        pygame.quit()