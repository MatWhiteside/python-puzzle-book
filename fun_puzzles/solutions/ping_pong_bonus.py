import pygame
import sys
import math
import random

pygame.init()


class StaticColour:
    def __init__(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour


class ChangingColour:
    def __init__(self, colours):
        self.colours = colours
        self.current_colour_idx = 0
        pygame.time.set_timer(pygame.USEREVENT, 500)

    def next_colour(self):
        if self.current_colour_idx + 1 < len(self.colours):
            self.current_colour_idx += 1
        else:
            self.current_colour_idx = 0

    def get_colour(self):
        return self.colours[self.current_colour_idx].get_colour()


class ColourPicker:

    RED = StaticColour((255, 0, 0))
    GREEN = StaticColour((0, 255, 0))
    BLUE = StaticColour((0, 0, 255))
    WHITE = StaticColour((255, 255, 255))
    RGB = ChangingColour([RED, GREEN, BLUE])
    RANDOM = ChangingColour(
        [
            StaticColour(
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            )
            for i in range(50)
        ]
    )

    @staticmethod
    def select_colour(
        screen,
        num_cols,
        font=pygame.font.Font(None, 30),
        caption="",
        available_colours=[RED, GREEN, BLUE, WHITE, RGB, RANDOM],
    ):

        # Calculate the size of each sqaure of colour on the screen
        colour_rect_width, colour_rect_height = ColourPicker.calc_colour_rect_size(
            screen, num_cols, available_colours
        )

        # Draw the colour selection squares on the screen
        colour_choices = ColourPicker.draw_colour_choices(
            screen, num_cols, available_colours, colour_rect_width, colour_rect_height
        )

        while True:

            # Redraw any colour selection squares that could have changed colour e.g. RGB
            for colour_choice in colour_choices:
                if isinstance(colour_choice["colour"], ChangingColour):
                    colour_choice["rect"] = pygame.draw.rect(
                        screen,
                        colour_choice["colour"].get_colour(),
                        [
                            colour_choice["rect"].x,
                            colour_choice["rect"].y,
                            colour_choice["rect"].width,
                            colour_choice["rect"].height,
                        ],
                    )

            # Handle any raised events, if the event is a colour being chosen then
            # we return the selected colour
            for event in pygame.event.get():
                event_result = ColourPicker.handle_event(event, colour_choices)
                if event_result is not None:
                    return event_result

            # Render the caption
            caption_text = font.render(caption, True, (255, 100, 100))
            caption_x = (screen.get_width() // 2) - (caption_text.get_width() // 2)
            caption_y = (screen.get_height() // 2) - (caption_text.get_height() // 2)
            screen.blit(caption_text, (caption_x, caption_y))

            pygame.display.update()

    @staticmethod
    def handle_event(event, colour_choices):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for colour_choice in colour_choices:
                if colour_choice["rect"].collidepoint(pygame.mouse.get_pos()):
                    return colour_choice["colour"]
        if event.type == pygame.USEREVENT:
            for colour_choice in colour_choices:
                if isinstance(colour_choice["colour"], ChangingColour):
                    colour_choice["colour"].next_colour()
        return None

    @staticmethod
    def draw_colour_choices(
        screen, num_cols, available_colours, colour_rect_width, colour_rect_height
    ):
        colour_choices = []

        for i, colour in enumerate(available_colours):
            x_pos = (i % num_cols) * colour_rect_width
            y_pos = (i // num_cols) * colour_rect_height

            colour_to_draw = colour.get_colour()

            colour_choices.append(
                {
                    "colour": colour,
                    "rect": pygame.draw.rect(
                        screen,
                        colour_to_draw,
                        [x_pos, y_pos, colour_rect_width, colour_rect_height],
                    ),
                }
            )
        return colour_choices

    @staticmethod
    def calc_colour_rect_size(screen, num_cols, available_colours):
        num_rows = math.ceil(len(available_colours) / num_cols)
        colour_rect_width = screen.get_width() // num_cols
        colour_rect_height = screen.get_height() // num_rows
        return colour_rect_width, colour_rect_height


class Ball:
    def __init__(self, x, y, speed, size, colour):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.colour = colour

    def move(self):
        self.x += self.speed.x
        self.y += self.speed.y

    def reset(self, x, y):
        # Reset the ball and randomise the direction it goes in
        self.speed.x = random.choice([self.speed.x, -self.speed.x])
        self.x = x
        self.y = y

    def switch_x_direction(self):
        self.speed.x = -self.speed.x

    def switch_y_direction(self):
        self.speed.y = -self.speed.y

    def get_colour(self, as_obj=False):
        if as_obj:
            return self.colour
        return self.colour.get_colour()

    def get_pos(self):
        return (self.x, self.y)


class Paddle:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        paddle_bottom_threshold,
        paddle_top_threshold,
        paddle_speed,
        colour,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.paddle_bottom_threshold = paddle_bottom_threshold
        self.paddle_top_threshold = paddle_top_threshold
        self.paddle_speed = paddle_speed
        self.colour = colour

    def move_up(self):
        self.y = max(self.paddle_top_threshold, self.y - self.paddle_speed)

    def move_down(self):
        self.y = min(self.paddle_bottom_threshold, self.y + self.paddle_speed)

    def get_colour(self, as_obj=False):
        if as_obj:
            return self.colour
        return self.colour.get_colour()

    def as_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def left(self):
        return self.x

    def right(self):
        return self.x + self.width

    def top(self):
        return self.y

    def bottom(self):
        return self.y + self.height


class PingPong:

    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    FPS = 60
    PADDLE_PADDING = 5
    PADDLE_WIDTH = 5
    PADDLE_HEIGHT = 100
    PADDLE_SPEED = 10
    PADDLE_TOP_THRESHOLD = 0
    PADDLE_BOTTOM_THRESHOLD = SCREEN_HEIGHT - PADDLE_HEIGHT
    BALL_STARTING_POS = pygame.Vector2(395, 295)
    BALL_SIZE = 10
    BALL_TOP_THRESHOLD = BALL_SIZE
    BALL_BOTTOM_THRESHOLD = SCREEN_HEIGHT - BALL_SIZE
    NUM_BALLS = 2
    LEFT_POINT_SCORING_THRESHOLD = 0
    RIGHT_POINT_SCORING_THRESHOLD = SCREEN_WIDTH - BALL_SIZE
    FONT = pygame.font.Font(None, 30)

    def __init__(self):
        # Create a window
        self.screen = pygame.display.set_mode(
            (PingPong.SCREEN_WIDTH, PingPong.SCREEN_HEIGHT),
            flags=pygame.SCALED,
            vsync=1,
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Two-Player Ping Pong")

        # Fetch game colours
        self.background = ColourPicker.select_colour(
            self.screen, 2, PingPong.FONT, "Background: pick colour"
        )
        left_paddle_colour = ColourPicker.select_colour(
            self.screen, 2, PingPong.FONT, "Left player: pick colour"
        )
        right_paddle_colour = ColourPicker.select_colour(
            self.screen, 2, PingPong.FONT, "Right player: pick colour"
        )
        ball_colour = ColourPicker.select_colour(
            self.screen, 2, PingPong.FONT, "Ball: pick colour"
        )

        # Create game objects
        self.left_paddle = Paddle(
            self.PADDLE_PADDING,
            (self.SCREEN_HEIGHT // 2) - (self.PADDLE_HEIGHT // 2),
            PingPong.PADDLE_WIDTH,
            PingPong.PADDLE_HEIGHT,
            PingPong.PADDLE_BOTTOM_THRESHOLD,
            PingPong.PADDLE_TOP_THRESHOLD,
            PingPong.PADDLE_SPEED,
            left_paddle_colour,
        )
        self.right_paddle = Paddle(
            self.SCREEN_WIDTH - (self.PADDLE_PADDING * 2),
            (self.SCREEN_HEIGHT // 2) - (self.PADDLE_HEIGHT // 2),
            PingPong.PADDLE_WIDTH,
            PingPong.PADDLE_HEIGHT,
            PingPong.PADDLE_BOTTOM_THRESHOLD,
            PingPong.PADDLE_TOP_THRESHOLD,
            PingPong.PADDLE_SPEED,
            right_paddle_colour,
        )
        self.balls = self.create_balls(PingPong.NUM_BALLS, ball_colour)

        # Initialise scores
        self.left_score = 0
        self.right_score = 0

    def play(self):

        # Main game loop
        while True:

            # Handle any raised events
            for event in pygame.event.get():
                self.handle_event(event)

            # Handle paddle movement
            self.handle_paddle_movement(pygame.key.get_pressed())

            for ball in self.balls:
                # Move the ball
                ball.move()

                # Check for a collision with the paddles and reverse ball direction (x)
                if self.ball_is_hit_by_paddle(ball):
                    ball.switch_x_direction()

                # Check for a collision with top/bottom of the screen and reverse ball direction (y)
                if self.ball_touched_top_or_bottom_of_screen(ball):
                    ball.switch_y_direction()

                # Check for a collision with a scoring threshold if a player missed the ball,
                # change the opposing score (if left scoring threshold is hit, then the right
                # player scored a point) and finally reset the ball.
                if self.left_scoring_threshold_hit(ball):
                    self.right_score += 1
                    ball.reset(
                        PingPong.BALL_STARTING_POS.x, PingPong.BALL_STARTING_POS.y
                    )
                elif self.right_scoring_threshold_hit(ball):
                    self.left_score += 1
                    ball.reset(
                        PingPong.BALL_STARTING_POS.x, PingPong.BALL_STARTING_POS.y
                    )

            # Update the screen
            self.draw()

    def draw(self):
        # Draw the paddles and ball
        self.screen.fill(self.background.get_colour())
        pygame.draw.rect(
            self.screen, self.left_paddle.get_colour(), self.left_paddle.as_rect()
        )
        pygame.draw.rect(
            self.screen, self.right_paddle.get_colour(), self.right_paddle.as_rect()
        )
        for ball in self.balls:
            pygame.draw.circle(
                self.screen, ball.get_colour(), ball.get_pos(), ball.size
            )

        # Draw the score
        score_text = PingPong.FONT.render(
            str(self.left_score) + " - " + str(self.right_score), True, (255, 255, 255)
        )
        self.screen.blit(score_text, (400 - score_text.get_width() // 2, 50))

        # Update the display
        pygame.display.update()
        self.clock.tick(PingPong.FPS)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle colour changing
        if event.type == pygame.USEREVENT:
            obj_colours = [ball.get_colour() for ball in self.balls] + [
                self.background,
                self.left_paddle.get_colour(True),
                self.right_paddle.get_colour(True),
            ]
            for colour in obj_colours:
                if isinstance(colour, ChangingColour):
                    colour.next_colour()

    def handle_paddle_movement(self, keys):
        # Left paddle up
        if keys[pygame.K_w]:
            self.left_paddle.move_up()

        # Left paddle down
        if keys[pygame.K_s]:
            self.left_paddle.move_down()

        # Right paddle up
        if keys[pygame.K_UP]:
            self.right_paddle.move_up()

        # Right paddle down
        if keys[pygame.K_DOWN]:
            self.right_paddle.move_down()

    def create_balls(self, num_balls, ball_colour):
        return [
            Ball(
                PingPong.BALL_STARTING_POS.x,
                PingPong.BALL_STARTING_POS.y,
                pygame.Vector2(random.choice([-7, 7]), random.randint(-10, 10)),
                PingPong.BALL_SIZE,
                ball_colour)
            for _ in range(num_balls)]

    def ball_is_hit_by_paddle(self, ball):
        ball_inline_with_left_paddle = (
            ball.x - ball.size <= self.left_paddle.right()
        )
        ball_inline_with_right_paddle = (
            ball.x + ball.size >= self.right_paddle.left()
        )

        left_paddle_in_correct_pos = (
            ball.y + ball.size >= self.left_paddle.top()
            and ball.y <= self.left_paddle.bottom()
        )
        right_paddle_in_correct_pos = (
            ball.y + ball.size >= self.right_paddle.top()
            and ball.y <= self.right_paddle.bottom()
        )

        left_paddle_hit = (
            ball_inline_with_left_paddle
            and left_paddle_in_correct_pos
            and ball.speed.x < 0
        )
        right_paddle_hit = (
            ball_inline_with_right_paddle
            and right_paddle_in_correct_pos
            and ball.speed.x > 0
        )

        return left_paddle_hit or right_paddle_hit

    def ball_touched_top_or_bottom_of_screen(self, ball):
        ball_touched_top_threshold = ball.y <= PingPong.BALL_TOP_THRESHOLD
        ball_touched_bottom_threshold = ball.y >= PingPong.BALL_BOTTOM_THRESHOLD
        return ball_touched_top_threshold or ball_touched_bottom_threshold

    def left_scoring_threshold_hit(self, ball):
        return ball.x <= PingPong.LEFT_POINT_SCORING_THRESHOLD

    def right_scoring_threshold_hit(self, ball):
        return ball.x >= PingPong.RIGHT_POINT_SCORING_THRESHOLD


if __name__ == "__main__":
    PingPong().play()
