import pygame
import pygame_gui

class InterfacePanel:

    def __init__(self, x, y, width, height, manager):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.manager = manager

       #particle number
        self.particle_count_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x + 10, y), (width - 20, 30)),
            text='Number of particles:',
            manager=self.manager
        )
        self.particle_count_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((x + 10, y + 30), (width - 20, 30)),
            manager=self.manager
        )

        #Particle size
        self.particle_size_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x + 10, y + 70), (width - 20, 30)),
            text='Particle size (radius):',
            manager=self.manager
        )
        self.particle_size_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((x + 10, y + 100), (width - 20, 30)),
            manager=self.manager
        )

        #Reset button
        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x + 10, y + 140), (width - 20, 60)),
            text='Reset settings',
            manager=self.manager
        )

        #Histogram button
        self.histogram_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x + 10, y + 210), (width - 20, 60)),
            text='Energy Histogram',
            manager=self.manager
        )

        #Output (prompts, errors, etc.)
        self.output_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x + 10, y + 280), (width - 20, 60)),
            text='Lorem Ipsum',
            manager=self.manager
        )

    def update(self, screen, dt):

        self.manager.update(dt)

        pygame.draw.rect(screen, (60, 60, 60), (self.x, self.y, self.width, self.height))

        self.manager.draw_ui(screen)

    def update_output(self, text):
        self.output_label.set_text(text)
    