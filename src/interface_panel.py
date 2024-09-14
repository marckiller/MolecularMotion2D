import pygame
import pygame_gui
from src.text_box import TextBox
from src.button import Button
from src.text_input import TextInput

class InterfacePanel:
    """A communication panel for the gas simulation application."""

    def __init__(self, x: int, y: int, width: int, height: int, manager: pygame_gui.UIManager) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.manager = manager

        # Create particle count and size input fields using TextInput class
        self.particle_count_input = TextInput(x + 10, y, width - 20, 30, 'Number of particles:', manager)
        self.particle_size_input = TextInput(x + 10, y + 70, width - 20, 30, 'Particle size (radius):', manager)

        # Create buttons using Button class
        self._reset_button = Button(x + 10, y + 140, width - 20, 60, 'Reset settings', manager)
        self._histogram_button = Button(x + 10, y + 210, width - 20, 60, 'Energy Histogram', manager)

        # Text box for terminal messages
        self.text_box = TextBox(x + 10, y + 280, width - 20, 150)

    def update(self, screen: pygame.Surface, dt: float) -> None:
        """Update the interface panel and draw the components."""
        self.manager.update(dt)
        self.draw_panel_background(screen)
        self.text_box.draw(screen)
        self.manager.draw_ui(screen)

    def draw_panel_background(self, screen: pygame.Surface) -> None:
        """Draw the background rectangle for the panel."""
        pygame.draw.rect(screen, (60, 60, 60), (self.x, self.y, self.width, self.height))

    def add_terminal_message(self, message: str) -> None:
        """Display a message in the text box."""
        self.text_box.update_text(message)

    def check_reset_button(self, event: pygame.event.Event) -> bool:
        """Check if the reset button is pressed"""
        return self._reset_button.check_pressed(event)
    
    def check_histogram_button(self, event: pygame.event.Event) -> bool:
        """Check if the histogram button is pressed"""
        return self._histogram_button.check_pressed(event)