import pygame
from typing import Tuple

class TextBox:
    """A text box to display text on the screen with a background color."""

    def __init__(self, x: int, y: int, width: int, height: int, 
                 bg_color: Tuple[int, int, int] = (30, 30, 30), 
                 text_color: Tuple[int, int, int] = (255, 255, 255)) -> None:
        """Initialize the text box with position, dimensions, and colors."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text_color = text_color
        self.text = ""

        pygame.font.init()
        self.font = pygame.font.Font(None, 24)

    def update_text(self, new_text: str) -> None:
        """Update the text in the box and insert line breaks to fit the width."""
        self.text = self.insert_line_breaks(new_text)

    def insert_line_breaks(self, text: str) -> str:
        """Insert line breaks into the text to ensure it fits within the box width."""
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            text_surface = self.font.render(test_line, True, self.text_color)

            if text_surface.get_width() <= self.width - 20:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "

        lines.append(current_line.strip())
        return '\n'.join(lines)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the text box and the text inside it on the screen."""
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        lines = self.text.split('\n')
        y_offset = self.y + 10
        max_lines = (self.height - 20) // 24

        for i, line in enumerate(lines):
            if i >= max_lines:
                break

            text_surface = self.font.render(line, True, self.text_color)
            screen.blit(text_surface, (self.x + 10, y_offset))
            y_offset += 24
