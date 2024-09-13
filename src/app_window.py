import pygame
import pygame_gui
from src.interface_panel import InterfacePanel

class AppWindow:

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        #control panel
        self.manager = pygame_gui.UIManager((self.width, self.height))
        self.particle_count = 10 #dafault settings 
        self.particle_radius = 5
        panel_width = self.width // 4
        self.interface = InterfacePanel(self.width - panel_width, 0, panel_width, self.height, self.manager)

        #arena

        #Arena code here

    def reset_simulation(self):
        print("Reset: button not implemented")
        self.interface.update_output("Reset:\n button not implemented")

    def display_kinetic_energy_histogram(self):
        print("Histogram: button not implemented")
        self.interface.update_output("Histogram:\n button not implemented")

    def run(self):

        while self.running:

            dt = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.manager.process_events(event)

                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    pass  # Implement text input handling here

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.interface.reset_button:
                        self.reset_simulation()
                    elif event.ui_element == self.interface.histogram_button:
                        self.display_kinetic_energy_histogram()

            self.window.fill((30, 30, 30))

            self.interface.update(self.window, dt)

            pygame.display.flip()

        pygame.quit()