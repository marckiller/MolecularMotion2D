import pygame

class AppWindow:

    def __init__(self, wight, height):
        pygame.init()
        self.width = wight
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()