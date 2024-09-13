import pygame
import pygame_gui
import random
from src.interface_panel import InterfacePanel
from src.arena import Arena
import math

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

        #Interface panel
        self.manager = pygame_gui.UIManager((self.width, self.height))
        panel_width = self.width // 4
        self.interface = InterfacePanel(self.width - panel_width, 0, panel_width, self.height, self.manager)

        #Arena
        self.arena = Arena(self.width * 3 // 4, self.height)

        #Setting default values in the interface
        self.interface.particle_count_input.set_text(str(self.default_particle_count))
        self.interface.particle_size_input.set_text(str(self.default_particle_radius))

        #Running the app
        self.reset_simulation()

    def reset_simulation(self):

        try:
            particle_count = int(self.interface.particle_count_input.get_text())
            particle_radius = int(self.interface.particle_size_input.get_text())

        except ValueError:
            self.interface.update_output("Invalid input. Please enter valid numbers.")
            return

        self.arena.particles = []

        for _ in range(particle_count):
            angle = random.uniform(0, 2 * math.pi)

            vx = self.default_particle_speed * math.cos(angle)
            vy = self.default_particle_speed * math.sin(angle)

            self.arena.add_particles(1, particle_radius, (vx, vy))

        self.interface.update_output(f"Reset: {particle_count} particles, radius {particle_radius}")

    def display_kinetic_energy_histogram(self):
        print("Histogram: button not implemented")
        self.interface.update_output("Histogram:\n button not implemented")

    def run(self):
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
