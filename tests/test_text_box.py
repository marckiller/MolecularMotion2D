import unittest
import pygame
from src.text_box import TextBox

class TestTextBox(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.text_box = TextBox(50, 50, 300, 100)
    
    def tearDown(self):
        pygame.quit()

    def test_initialization(self):
        self.assertEqual(self.text_box.x, 50)
        self.assertEqual(self.text_box.y, 50)
        self.assertEqual(self.text_box.width, 300)
        self.assertEqual(self.text_box.height, 100)
        self.assertEqual(self.text_box.bg_color, (30, 30, 30))
        self.assertEqual(self.text_box.text_color, (255, 255, 255))
        self.assertEqual(self.text_box.text, "")

    def test_update_text(self):
        self.text_box.update_text("Hello world")
        self.assertEqual(self.text_box.text, "Hello world")

    def test_insert_line_breaks(self):
        long_text = "This is a long text that should wrap into multiple lines if it's too long."
        self.text_box.update_text(long_text)
        lines = self.text_box.text.split('\n')
        self.assertGreater(len(lines), 1)  # Check if the text has been split into multiple lines

    def test_draw(self):
        try:
            self.text_box.draw(self.screen)
        except Exception as e:
            self.fail(f"draw method raised an exception: {e}")
