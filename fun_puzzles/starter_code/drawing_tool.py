import pygame
import sys

pygame.init()


class DrawingTool:

    # Set your constants here
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    PAINT_SIZE = 10
    # ...

    def __init__(self):

        # Create a window
        self.screen = pygame.display.set_mode(
            (DrawingTool.SCREEN_WIDTH, DrawingTool.SCREEN_HEIGHT),
        )
        pygame.display.set_caption("Drawing Tool")

        # Set your variables here
        # ...


    def start(self):

        # Main loop
        while True:

            # Handle any raised events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            # Your implementation here...

            # Update the display
            pygame.display.update()

    def draw(self, pos):
        # Your implementation here...


if __name__ == "__main__":
    DrawingTool().start()
