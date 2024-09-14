import pygame

class TextBox:

    def __init__(self, x, y, width, height, bg_color=(30, 30, 30), text_color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text_color = text_color
        self.text = ""

        pygame.font.init()
        self.font = pygame.font.Font(None, 24)

    def update_text(self, new_text):
        self.text = self.insert_line_breaks(new_text)

    def insert_line_breaks(self, text):
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            text_surface = self.font.render(test_line, True, self.text_color)

            if text_surface.get_width() <= self.width - 20:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "

        lines.append(current_line)
        return '\n'.join(lines)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))

        lines = self.text.split('\n')
        y_offset = self.y + 10
        for line in lines:
            if y_offset + 24 > self.y + self.height - 10:
                break
            text_surface = self.font.render(line, True, self.text_color)
            screen.blit(text_surface, (self.x + 10, y_offset))
            y_offset += 24
