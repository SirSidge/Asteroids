import pygame

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
    
    def draw(self, x, y, radius):
        pygame.draw.circle(self.screen, "White", self.position, radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt