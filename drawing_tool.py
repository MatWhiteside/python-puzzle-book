import pygame
import sys

pygame.init()


class DrawingTool:

    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    PAINT_SIZE = 10

    def __init__(self):

        # Create a window
        self.screen = pygame.display.set_mode(
            (DrawingTool.SCREEN_WIDTH, DrawingTool.SCREEN_HEIGHT),
        )
        pygame.display.set_caption("Drawing Tool")

        # Initialise variables
        self.is_drawing = False

    def start(self):

        # Main loop
        while True:

            # Handle any raised events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.is_drawing = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.is_drawing = False

            if self.is_drawing:
                self.draw(pygame.mouse.get_pos())

            # Update the display
            pygame.display.update()

    def draw(self, pos):
        pygame.draw.circle(self.screen, (255, 255, 255), pos, DrawingTool.PAINT_SIZE)


if __name__ == "__main__":
    DrawingTool().start()
