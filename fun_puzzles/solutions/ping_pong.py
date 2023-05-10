import pygame
import sys

pygame.init()

# Set constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10
PADDLE_TOP_THRESHOLD = 0
PADDLE_BOTTOM_THRESHOLD = HEIGHT - PADDLE_HEIGHT
BALL_STARTING_POS = pygame.Vector2(395, 295)
BALL_SIZE = 10
BALL_TOP_THRESHOLD = BALL_SIZE
BALL_BOTTOM_THRESHOLD = HEIGHT - BALL_SIZE
LEFT_POINT_SCORING_THRESHOLD = 0
RIGHT_POINT_SCORING_THRESHOLD = WIDTH - BALL_SIZE
FONT = pygame.font.Font(None, 30)


# Set variables
left_paddle_pos = pygame.Vector2(PADDLE_WIDTH, 250)
right_paddle_pos = pygame.Vector2(WIDTH - (PADDLE_WIDTH * 2), 250)
ball_pos = BALL_STARTING_POS
left_score = 0
right_score = 0
ball_speed = pygame.Vector2(7)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
pygame.display.set_caption("Two-Player Ping Pong")

# Create two paddles
left_paddle = pygame.Rect(left_paddle_pos, (PADDLE_WIDTH, PADDLE_HEIGHT))
right_paddle = pygame.Rect(right_paddle_pos, (PADDLE_WIDTH, PADDLE_HEIGHT))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.y = max(PADDLE_TOP_THRESHOLD, left_paddle.y - PADDLE_SPEED)
    if keys[pygame.K_s]:
        left_paddle.y = min(PADDLE_BOTTOM_THRESHOLD, left_paddle.y + PADDLE_SPEED)
    if keys[pygame.K_UP]:
        right_paddle.y = max(PADDLE_TOP_THRESHOLD, right_paddle.y - PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        right_paddle.y = min(PADDLE_BOTTOM_THRESHOLD, right_paddle.y + PADDLE_SPEED)

    # Move the ball
    ball_pos += ball_speed

    # Check for collision with the paddles and reverse ball direction
    ball_inline_with_left_paddle = ball_pos.x - BALL_SIZE <= left_paddle.right
    ball_inline_with_right_paddle = ball_pos.x + BALL_SIZE >= right_paddle.left

    left_paddle_in_correct_pos = ball_pos.y + BALL_SIZE >= left_paddle.top and ball_pos.y <= left_paddle.bottom
    right_paddle_in_correct_pos = ball_pos.y + BALL_SIZE >= right_paddle.top and ball_pos.y <= right_paddle.bottom

    left_paddle_hit = ball_inline_with_left_paddle and left_paddle_in_correct_pos and ball_speed.x < 0
    right_paddle_hit = ball_inline_with_right_paddle and right_paddle_in_correct_pos and ball_speed.x > 0

    if left_paddle_hit or right_paddle_hit:
        ball_speed.x = -ball_speed.x

    # Reverse ball direction if top or bottom of screen hit
    if ball_pos.y <= BALL_TOP_THRESHOLD or ball_pos.y >= BALL_BOTTOM_THRESHOLD:
        ball_speed.y = -ball_speed.y

    # Check for a point scored
    if ball_pos.x <= LEFT_POINT_SCORING_THRESHOLD:
        right_score += 1
        ball_pos = pygame.Vector2(395, 295)
    elif ball_pos.x >= RIGHT_POINT_SCORING_THRESHOLD:
        left_score += 1
        ball_pos = pygame.Vector2(395, 295)

    # Draw the paddles and ball
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)
    pygame.draw.circle(screen, (255, 255, 0), ball_pos, BALL_SIZE)

    # Draw the score
    score_text = FONT.render(str(left_score) + " - " + str(right_score), True, (255, 255, 255))
    screen.blit(score_text, (400 - score_text.get_width() // 2, 50))

    # Update the display
    pygame.display.update()
    clock.tick(FPS)
