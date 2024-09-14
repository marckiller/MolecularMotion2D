import pygame
import pygame_gui

class Button:

    def __init__(self, x: int, y: int, width: int, height: int, text: str, manager: pygame_gui.UIManager) -> None:
        """Initialize a button with position, dimensions, and text."""
        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (width, height)),
            text=text,
            manager=manager
        )

    def check_pressed(self, event: pygame.event.Event) -> bool:
        """Check if the button is pressed."""
        return event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.button
