import pygame
import sys
import math
import random

# Note: this starter code has been left vague and is more designed to give you 
# an idea of how you could structure your own code... Although feel free to use
# it as starter code too!

pygame.init()


class StaticColour:
    # Your implementation here...

class ChangingColour:
    # Your implementation here...

class ColourPicker:
    # Your implementation here...

class Ball:
    # Your implementation here...

class Paddle:
    # Your implementation here...

class PingPong:

    # Set your constants here
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    FPS = 60
    # ...

    def __init__(self):
        # Create a window
        self.screen = pygame.display.set_mode(
            (PingPong.SCREEN_WIDTH, PingPong.SCREEN_HEIGHT),
            flags=pygame.SCALED,
            vsync=1,
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Two-Player Ping Pong")

        # Your implementation here...

    def play(self):

        # Main game loop
        while True:

            # Handle any raised events
            for event in pygame.event.get():
                self.handle_event(event)

            # Your implementation here...

            # Update the screen
            self.draw()

    def draw(self):
        # Your implementation here...

        # Update the display
        pygame.display.update()
        self.clock.tick(PingPong.FPS)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Your implementation here...


if __name__ == "__main__":
    PingPong().play()
