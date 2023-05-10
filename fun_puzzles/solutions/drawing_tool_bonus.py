import pygame
import sys
from itertools import product

pygame.init()


class DrawingTools:
    PAINT_BRUSH = "Paint Brush"
    LINE_TOOL = "Line Tool"


class ActionButtons:
    CLEAR_CANVAS = "Clear Canvas"
    SAVE_IMAGE = "Save Image"
    PLUS_THICKNESS = "+"
    MINUS_THICKNESS = "-"


class DrawingTool:

    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 700
    SIDEBAR_COLOUR = (200, 200, 200)
    SIDEBAR_BUTTON_COLOUR = (50, 50, 50)
    SIDEBAR_WIDTH = SCREEN_WIDTH // 4
    SIDEBAR_NUM_COLS = 2
    SIDEBAR_BUTTONS_RECT_SIZE = SIDEBAR_WIDTH // SIDEBAR_NUM_COLS
    THICKNESS_INCREMEMT = 1
    BACKGROUND_COLOUR = (255, 255, 255)
    BACKGROUND_Y = 0
    BACKGROUND_X = SIDEBAR_WIDTH

    def __init__(self):

        # Create a window
        self.screen = pygame.display.set_mode(
            (DrawingTool.SCREEN_WIDTH, DrawingTool.SCREEN_HEIGHT),
        )
        pygame.display.set_caption("Drawing Tool")

        # Initialise variables
        self.is_drawing = False
        self.is_draw_line_mode = False
        self.line_initial_point = None
        self.drawing_colour = (0, 255, 255)
        self.drawing_tool = DrawingTools.PAINT_BRUSH
        self.drawing_snapshot = None
        self.thickness = 10

    def start(self):

        self.clear_canvas()

        # Main loop
        while True:

            # Handle any raised events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_button_down()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_button_up()

            if self.is_drawing:
                self.draw(pygame.mouse.get_pos())
            if self.is_draw_line_mode:
                self.screen.blit(
                    self.drawing_snapshot,
                    pygame.Rect(
                        DrawingTool.BACKGROUND_X,
                        DrawingTool.BACKGROUND_Y,
                        DrawingTool.SCREEN_WIDTH - DrawingTool.SIDEBAR_WIDTH,
                        DrawingTool.SCREEN_HEIGHT,
                    ),
                )
                self.draw_line()

            self.clickables = self.render_side_bar()

            # Update the display
            pygame.display.update()

    def render_side_bar(self):
        # Create a dict of clickable rect's that will be returned
        clickables = {"colours": {}, "buttons": {}}

        # Render side bar background
        pygame.draw.rect(
            self.screen,
            DrawingTool.SIDEBAR_COLOUR,
            pygame.Rect(0, 0, DrawingTool.SIDEBAR_WIDTH, DrawingTool.SCREEN_HEIGHT),
        )

        y_pos = -DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE

        # Render side bar colour options
        clickables, y_pos = self.render_sidebar_colour_options(clickables, y_pos)

        # Render side bar tools and buttons
        clickables, y_pos = self.render_sidebar_action_buttons(clickables, y_pos)

        # Render the drawing thickness selector
        self.render_thickness_selector(clickables, y_pos)

        return clickables

    def render_sidebar_action_buttons(self, clickables, y_pos):
        action_buttons_font = pygame.font.Font(None, 20)
        tools = [
            DrawingTools.PAINT_BRUSH,
            DrawingTools.LINE_TOOL,
            ActionButtons.CLEAR_CANVAS,
            ActionButtons.SAVE_IMAGE,
        ]
        for tool_iter, tool in enumerate(tools):
            x_pos = (
                tool_iter % DrawingTool.SIDEBAR_NUM_COLS
            ) * DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE
            y_pos += (
                DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE
                if tool_iter % DrawingTool.SIDEBAR_NUM_COLS == 0
                else 0
            )

            rect = pygame.draw.rect(
                self.screen,
                DrawingTool.SIDEBAR_BUTTON_COLOUR,
                pygame.Rect(
                    x_pos,
                    y_pos,
                    DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE,
                    DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE,
                ),
            )
            clickables["buttons"][tool] = rect
            paint_brush_tool_text = action_buttons_font.render(tool, True, (255, 255, 255))
            paint_brush_tool_text_rect = paint_brush_tool_text.get_rect(
                center=(
                    x_pos + DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE / 2,
                    y_pos + DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE / 2,
                )
            )
            self.screen.blit(paint_brush_tool_text, paint_brush_tool_text_rect)

        return clickables, y_pos

    def render_sidebar_colour_options(self, clickables, y_pos):
        colours = list(product(set([0, 255]), repeat=3))
        for colour_iter, colour in enumerate(colours):
            x_pos = (
                colour_iter % DrawingTool.SIDEBAR_NUM_COLS
            ) * DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE
            y_pos += (
                DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE
                if colour_iter % DrawingTool.SIDEBAR_NUM_COLS == 0
                else 0
            )
            rect = pygame.draw.rect(
                self.screen,
                colour,
                pygame.Rect(
                    x_pos,
                    y_pos,
                    DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE,
                    DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE,
                ),
            )
            clickables["colours"][colour] = rect

        return clickables, y_pos

    def render_thickness_selector(self, clickables, y_pos):

        y_pos += DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE

        plus_minus_font = pygame.font.Font(None, 50)
        thickness_font = pygame.font.Font(None, 50)

        # Render the minus size button
        minus_thickness_text = plus_minus_font.render(ActionButtons.MINUS_THICKNESS, True, (255, 255, 255))
        minus_thickness_text_rect = minus_thickness_text.get_rect(
            center=(DrawingTool.SIDEBAR_WIDTH // 4, y_pos + DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE / 2))
        self.screen.blit(minus_thickness_text, minus_thickness_text_rect)

        # Render the current thickness
        thickness_text = thickness_font.render(str(self.thickness), True, (255, 255, 255))
        thickness_text_rect = thickness_text.get_rect(
            center=(DrawingTool.SIDEBAR_WIDTH // 2, y_pos + DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE / 2))
        self.screen.blit(thickness_text, thickness_text_rect)

        # Render the plus size button
        plus_thickness_text = plus_minus_font.render(ActionButtons.PLUS_THICKNESS, True, (255, 255, 255))
        plus_thickness_text_rect = plus_thickness_text.get_rect(
            center=((DrawingTool.SIDEBAR_WIDTH // 2) + (DrawingTool.SIDEBAR_WIDTH // 4), y_pos + DrawingTool.SIDEBAR_BUTTONS_RECT_SIZE / 2))
        self.screen.blit(plus_thickness_text, plus_thickness_text_rect)

        # Add to clickables
        clickables["buttons"][ActionButtons.MINUS_THICKNESS] = minus_thickness_text_rect
        clickables["buttons"][ActionButtons.PLUS_THICKNESS] = plus_thickness_text_rect

        return clickables, y_pos

    def handle_mouse_button_down(self):
        if self.background.collidepoint(pygame.mouse.get_pos()):
            if self.drawing_tool == DrawingTools.PAINT_BRUSH:
                self.is_drawing = True
            if self.drawing_tool == DrawingTools.LINE_TOOL:
                self.is_draw_line_mode = not self.is_draw_line_mode
                if self.is_draw_line_mode:
                    self.drawing_snapshot = self.save_image(False)
                    self.line_initial_point = pygame.mouse.get_pos()

    def handle_mouse_button_up(self):
        if self.background.collidepoint(pygame.mouse.get_pos()):
            if self.drawing_tool == DrawingTools.PAINT_BRUSH:
                self.is_drawing = False
        else:
            self.action_sidebar_btn_pressed()

    def action_sidebar_btn_pressed(self):
        for colour, rect in self.clickables["colours"].items():
            if rect.collidepoint(pygame.mouse.get_pos()):
                self.drawing_colour = colour

        for button, rect in self.clickables["buttons"].items():
            if rect.collidepoint(pygame.mouse.get_pos()):
                if button == DrawingTools.PAINT_BRUSH:
                    self.drawing_tool = DrawingTools.PAINT_BRUSH
                if button == DrawingTools.LINE_TOOL:
                    self.drawing_tool = DrawingTools.LINE_TOOL
                if button == ActionButtons.CLEAR_CANVAS:
                    self.clear_canvas()
                if button == ActionButtons.SAVE_IMAGE:
                    self.save_image()
                if button == ActionButtons.MINUS_THICKNESS:
                    if self.thickness > 0:
                        self.thickness -= DrawingTool.THICKNESS_INCREMEMT
                if button == ActionButtons.PLUS_THICKNESS:
                    self.thickness += DrawingTool.THICKNESS_INCREMEMT

    def clear_canvas(self):
        self.background = pygame.draw.rect(
            self.screen,
            DrawingTool.BACKGROUND_COLOUR,
            pygame.Rect(
                DrawingTool.BACKGROUND_X,
                DrawingTool.BACKGROUND_Y,
                DrawingTool.SCREEN_WIDTH - DrawingTool.SIDEBAR_WIDTH,
                DrawingTool.SCREEN_HEIGHT,
            ),
        )

    def save_image(self, save_to_disk=True):
        drawing = self.screen.subsurface(self.background).copy()
        if save_to_disk:
            pygame.image.save(drawing, "Drawing Tool Saved Drawing.jpg")
        return drawing

    def draw(self, pos):
        pygame.draw.circle(
            self.screen, self.drawing_colour, pos, self.thickness
        )

    def draw_line(self):
        pygame.draw.polygon(
            self.screen,
            self.drawing_colour,
            [self.line_initial_point, pygame.mouse.get_pos()],
            self.thickness * 2
        )
        pygame.draw.circle(self.screen, self.drawing_colour, self.line_initial_point, self.thickness)
        pygame.draw.circle(self.screen, self.drawing_colour, pygame.mouse.get_pos(), self.thickness)


if __name__ == "__main__":
    DrawingTool().start()
