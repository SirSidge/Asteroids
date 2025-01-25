import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Setting up dt
    clock = pygame.time.Clock()
    dt = 0

    #instantiate player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Groups
    updatable_group = pygame.sprite.Group(player)
    drawable_group = pygame.sprite.Group(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for thing in updatable_group:
            thing.update(dt)
        for thing in drawable_group:
            thing.draw(screen)

        pygame.display.flip()
        
        
        #Positioning matters. Don't draw under the 'tick'
        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()