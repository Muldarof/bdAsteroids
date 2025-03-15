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
    #create screen with set dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create an instance to keep track of time, used for limiting fps
    clock = pygame.time.Clock()
    dt = 0
    
    #create entities
    mainCharacter = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, 10)

    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw background (black)
        screen.fill("black")
        
        #Draw everything
        mainCharacter.draw(screen)

        #Update drawing to screen
        pygame.display.flip()

        #limit screen updates to 60 fps
        time = clock.tick(60)
        dt = time / 1000
        


if __name__ == "__main__":
    main()

