import pygame
import sys

pygame.init()

# Set your constants here
WIDTH, HEIGHT = 800, 600
FPS = 60
# ...

# Set your variables here
# ...

screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
pygame.display.set_caption("Two-Player Ping Pong")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Your implementation here...


    screen.fill((0, 0, 0))
    pygame.display.update()
    clock.tick(FPS)
