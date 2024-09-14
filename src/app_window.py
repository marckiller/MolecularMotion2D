import pygame
import pygame_gui
import multiprocessing

from src.interface_panel import InterfacePanel
from src.arena import Arena
from src.histogram_manager import HistogramManager

class AppWindow:
    """Main application window for the gas simulation."""

    def __init__(self, width: int, height: int) -> None:
        """Initialize the application window, interface, and arena."""
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        # Default simulation parameters
        self.default_particle_count = 60
        self.default_particle_radius = 10
        self.default_particle_speed = 100

        # Load intro logo
        self.logo = pygame.image.load('assets/images/intro.png')

        # Set up interface panel
        self.manager = pygame_gui.UIManager((self.width, self.height))
        panel_width = self.width // 4
        self.interface = InterfacePanel(self.width - panel_width, 0, panel_width, self.height, self.manager)

        # Set up simulation arena
        self.arena = Arena(self.width * 3 // 4, self.height)

        # Set default values in the interface
        self.interface.particle_count_input.set_text(str(self.default_particle_count))
        self.interface.particle_size_input.set_text(str(self.default_particle_radius))

        # Customize the app window
        icon = pygame.image.load('assets/images/icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Gas-tastic!')

        # Histogram manager
        self.histogram_manager = HistogramManager('Energy Histogram', 'Kinetic Energy', 'Frequency', 15)

        # Initialize simulation
        self.reset_simulation()

    def show_logo(self) -> None:
        """Display an intro logo for 3 seconds."""
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

    def reset_simulation(self) -> None:
        """Reset the particle simulation with values from the interface panel."""
        try:
            particle_count = int(self.interface.particle_count_input.get_text())
            particle_radius = int(self.interface.particle_size_input.get_text())
        except ValueError:
            self.interface.add_terminal_message("Invalid input. Please enter valid numbers.")
            return

        self.arena.reset()

        message = self.arena.add_particles(particle_count, particle_radius, self.default_particle_speed)
        self.interface.add_terminal_message(message)

    def display_kinetic_energy_histogram(self) -> None:
        """Display the kinetic energy histogram of particles in the arena."""
        energies = self.arena.get_kinetic_energies()
        histogram_process = multiprocessing.Process(target=self.histogram_manager.show_histogram, args=(energies,))
        histogram_process.start()
        self.interface.add_terminal_message("Displaying kinetic energy histogram.")

    def run(self) -> None:
        """Main loop of the application."""
        self.show_logo()

        while self.running:
            dt = self.clock.tick(60) / 1000.0  # Time between frames

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.manager.process_events(event)

                # Buttons pressing
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if self.interface.check_reset_button(event):
                        self.reset_simulation()
                    elif self.interface.check_histogram_button(event):
                        self.display_kinetic_energy_histogram()

            self.arena.update(dt)

            # Render the frame
            self.window.fill((30, 30, 30))
            self.arena.draw(self.window)
            self.interface.update(self.window, dt)

            pygame.display.flip()

        pygame.quit()
