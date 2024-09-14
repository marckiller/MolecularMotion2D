import pygame
import pygame_gui
import random
import math
import multiprocessing

from src.interface_panel import InterfacePanel
from src.arena import Arena
from src.histogram_manager import HistogramManager

class AppWindow:

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.default_particle_count = 1 #default values when opening the app
        self.default_particle_radius = 100 
        self.default_particle_speed = 100 

        #intro
        self.logo = pygame.image.load('assets/images/intro.png')

        #Interface panel
        self.manager = pygame_gui.UIManager((self.width, self.height))
        panel_width = self.width // 4
        self.interface = InterfacePanel(self.width - panel_width, 0, panel_width, self.height, self.manager)

        #Arena
        self.arena = Arena(self.width * 3 // 4, self.height)

        #Setting default values in the interface
        self.interface.particle_count_input.set_text(str(self.default_particle_count))
        self.interface.particle_size_input.set_text(str(self.default_particle_radius))

        #Customizing the interdace
        icon = pygame.image.load('assets/images/icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Gas-tastic!')

        self.histogram_manager = HistogramManager('Energy Histogram', 'Kinetic Energy', 'Frequency', 15)

        #Running the app
        self.reset_simulation()

    def show_logo(self):
        start_time = pygame.time.get_ticks()

        while pygame.time.get_ticks() - start_time < 3000:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill((30, 30, 30))
            logo_rect = self.logo.get_rect(center=(self.width // 2, self.height // 2))
            self.window.blit(self.logo, logo_rect)
            pygame.display.flip()

            self.clock.tick(60)

        pygame.display.flip()

    def reset_simulation(self):

        try:
            particle_count = int(self.interface.particle_count_input.get_text())
            particle_radius = int(self.interface.particle_size_input.get_text())

        except ValueError:
            self.interface.add_terminal_message("Invalid input. Please enter valid numbers.")
            return

        self.arena.particles = []

        message = self.arena.add_particles(particle_count, particle_radius, self.default_particle_speed)

        self.interface.add_terminal_message(message)

    def display_kinetic_energy_histogram(self):

        energies = self.arena.get_kinetic_energies()
        histogram_process = multiprocessing.Process(target=self.histogram_manager.show_histogram, args=(energies,))
        histogram_process.start()
        self.interface.add_terminal_message("Displaying kinetic energy histogram.")

    def run(self):

        self.show_logo()

        while self.running:
            dt = self.clock.tick(60) / 1000.0 #time between frames

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.manager.process_events(event)

                #Buttons
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.interface.reset_button:
                        self.reset_simulation()
                    elif event.ui_element == self.interface.histogram_button:
                        self.display_kinetic_energy_histogram()

            self.arena.update(dt)

            self.window.fill((30, 30, 30))
            self.arena.draw(self.window)
            self.interface.update(self.window, dt)

            pygame.display.flip()

        pygame.quit()