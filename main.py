import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Setting up dt
    clock = pygame.time.Clock()
    dt = 0

    #Groups
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)

    #instantiate player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for obj in updatable_group:
            obj.update(dt)

        for asteroid in asteroids_group:
            if CircleShape.collision_check(player, asteroid):
                print("Game over!")
                raise Exception(SystemExit)
        
        #Not sure why screen.fill is separating the updatable and drawable group. Do you want to make sure you upadte before you draw? The background is top priority though right?
        screen.fill("black")

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()
        
        
        #Positioning matters. Don't draw under the 'tick'
        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()