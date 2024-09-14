import unittest
import pygame
import pygame_gui
from src.text_input import TextInput

class TestTextInput(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.manager = pygame_gui.UIManager((800, 600))
        self.text_input = TextInput(100, 100, 200, 30, "Enter text:", self.manager)

    def tearDown(self):
        pygame.quit()

    def test_initial_text_empty(self):
        self.assertEqual(self.text_input.get_text(), "")

    def test_set_text(self):
        test_string = "Hello, World!"
        self.text_input.set_text(test_string)
        self.assertEqual(self.text_input.get_text(), test_string)
