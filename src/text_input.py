import pygame
import pygame_gui

class TextInput:
    """A text input field with a label."""

    def __init__(self, x: int, y: int, width: int, height: int, label_text: str, manager: pygame_gui.UIManager) -> None:
        """Initialize a text input field with a label."""
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x, y), (width, height)),
            text=label_text,
            manager=manager
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((x, y + height + 5), (width, height)),
            manager=manager
        )

    def get_text(self) -> str:
        """Return the text entered in the input field."""
        return self.input.get_text()

    def set_text(self, text: str) -> None:
        """Set the text in the input field."""
        self.input.set_text(text)
