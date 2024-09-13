import unittest
import pygame
import pygame_gui
from src.interface_panel import InterfacePanel

class TestInterfacePanel(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.manager = pygame_gui.UIManager((800, 600))
        self.interface = InterfacePanel(600, 0, 200, 600, self.manager)

    def tearDown(self):
        pygame.quit()

    def test_initialization(self):
        self.assertIsNotNone(self.interface.particle_count_label)
        self.assertIsNotNone(self.interface.particle_count_input)
        self.assertIsNotNone(self.interface.particle_size_label)
        self.assertIsNotNone(self.interface.particle_size_input)
        self.assertIsNotNone(self.interface.reset_button)
        self.assertIsNotNone(self.interface.histogram_button)
        self.assertIsNotNone(self.interface.output_label)

    def test_update_output(self):
        self.interface.update_output("Test message")
        self.assertEqual(self.interface.output_label.text, "Test message")

    def test_button_press_event(self):
        reset_button_event = pygame.event.Event(pygame.USEREVENT, {'ui_element': self.interface.reset_button, 'ui_object_id': '#reset_button', 'ui_event_type': pygame_gui.UI_BUTTON_PRESSED})
        pygame.event.post(reset_button_event)

        for event in pygame.event.get():
            self.manager.process_events(event)
        
        # TODO: add more test cases here 

    def test_text_entry_event(self):
        particle_count_event = pygame.event.Event(pygame.USEREVENT, {'ui_element': self.interface.particle_count_input, 'ui_object_id': '#particle_count_input', 'ui_event_type': pygame_gui.UI_TEXT_ENTRY_FINISHED, 'text': '50'})
        pygame.event.post(particle_count_event)

        for event in pygame.event.get():
            self.manager.process_events(event)