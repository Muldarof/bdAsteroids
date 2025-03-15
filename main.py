# this allows us to use code from
# the open-source pygame library
# throughtout this file
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {1280}")
    print(f"Screen height: {720}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    counter = 0
    while True:
        pygame.Surface.fill(screen, (1,1,1))
        pygame.display.flip()
        print(f"Counter = {counter}")
        counter += 1

if __name__ == "__main__":
    main()

