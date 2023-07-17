import pygame
import sys
from itertools import product

pygame.init()


class DrawingTools:
    # Your implementation here...


class ActionButtons:
    # Your implementation here...


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

        self.clear_canvas()

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

    def render_side_bar(self):
        # Your implementation here...

    def render_sidebar_action_buttons(self, clickables, y_pos):
        # Your implementation here...

    def render_sidebar_colour_options(self, clickables, y_pos):
        # Your implementation here...

    def render_thickness_selector(self, clickables, y_pos):
        # Your implementation here...

    def handle_mouse_button_down(self):
        # Your implementation here...

    def handle_mouse_button_up(self):
       # Your implementation here...

    def action_sidebar_btn_pressed(self):
        # Your implementation here...

    def clear_canvas(self):
        # Your implementation here...

    def save_image(self, save_to_disk=True):
        # Your implementation here...

    def draw(self, pos):
        # Your implementation here...

    def draw_line(self):
        # Your implementation here...


if __name__ == "__main__":
    DrawingTool().start()
