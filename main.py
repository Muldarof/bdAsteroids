# this allows us to use code from
# the open-source pygame library
# throughtout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {1280}")
    print(f"Screen height: {720}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    mainCharacter = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        mainCharacter.draw(screen)
        pygame.display.flip()
        time = clock.tick(60)
        dt = time / 1000
        


if __name__ == "__main__":
    main()

